import argparse
import datetime
import json
import logging
import pathlib
import sys

import bcrypt
import pytz
import tzlocal

from pydomjudge.model import (
    JudgeSettings,
    User,
    UserRole,
    Team,
    TeamCategory,
    DefaultCategory,
    SystemCategory,
    Affiliation,
    Contest,
    ContestProblem,
)
from pydomjudge.model.settings import (
    JudgeInstance,
    ClarificationSettings,
    DisplaySettings,
    ScoringSettings,
    JudgingSettings,
)
from pydomjudge.repository.kattis import Repository
from pydomjudge.scripts.upload import UsersDescription


def make_settings():
    judge_settings = JudgeSettings(
        judging=JudgingSettings(),
        scoring=ScoringSettings(),
        display=DisplaySettings(),
        clarification=ClarificationSettings(),
    )
    return JudgeInstance(
        identifier="local",
        settings=judge_settings,
        base_time=1.5,
        user_whitelist=set(),
        allowed_language_keys=["c", "java", "python"],
        team_categories=[DefaultCategory.Participants],
    ).serialize()


def make_contest():
    repository = Repository(pathlib.Path("repository"))
    problem = repository.problems.load_problem("helloworld")
    contest_problem = ContestProblem(
        name="helloworld", points=4, color="blue", problem=problem
    )

    base_time = datetime.datetime.now(tzlocal.get_localzone()).replace(
        minute=0, second=0, microsecond=0
    )
    return Contest(
        key="sample",
        name="Sample Contest",
        activation_time=base_time,
        start_time=base_time + datetime.timedelta(hours=1),
        freeze_time=None,
        end_time=base_time + datetime.timedelta(days=14),
        deactivation_time=base_time + datetime.timedelta(days=15),
        problems=[contest_problem],
        access=None,
        public_scoreboard=False,
    ).serialize(repository.problems)


def make_users():
    salt = bcrypt.gensalt()
    affiliation = Affiliation(
        short_name="foo", name="Foo University of Bar", country=None
    )

    user = User(
        login_name="user",
        display_name="User",
        email="user@localhost",
        password_hash=bcrypt.hashpw(b"user", salt).decode(),
        role=UserRole.Participant,
    )
    admin = User(
        login_name="admin",
        display_name="Admin",
        email="admin@localhost",
        password_hash=bcrypt.hashpw(b"admin", salt).decode(),
        role=UserRole.Admin,
    )
    user_team = Team(
        "user_team",
        display_name="Awesome!",
        members=[user],
        category=DefaultCategory.Participants,
        affiliation=affiliation,
    )
    admin_team = Team(
        "admin_team",
        display_name="Admin",
        members=[admin],
        category=SystemCategory.Jury,
        affiliation=None,
    )

    return UsersDescription(
        users=[user, admin], affiliations=[affiliation], teams=[user_team, admin_team]
    ).serialize()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-O",
        "--output",
        type=argparse.FileType("w"),
        default=sys.stdout,
        help="File output",
    )
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON")

    subparsers = parser.add_subparsers(help="Help for commands")
    settings = subparsers.add_parser("settings", help="Create settings")
    settings.set_defaults(func=make_settings)

    users = subparsers.add_parser("users", help="Create users")
    users.set_defaults(func=make_users)

    contest = subparsers.add_parser("contest", help="Create contest")
    contest.set_defaults(func=make_contest)

    args = parser.parse_args()
    with args.output as f:
        json.dump(args.func(), f, indent=2 if args.pretty else None)
