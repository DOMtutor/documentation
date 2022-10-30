# Usage

## DOMjudge Setup

 * Follow `domjudge-deployment/docker/local/README.md`
 * Create a file `db.yml` with:
   ```yml
   host: 127.0.0.1
   port: 3306
   user: domjudge
   password: domjudge
   database: domjudge
   ```
   Can also be found in the `samples` folder

## Using the Upload Script

 * Adapt the json files in `samples` as needed; add/change the problems in repository
 * The `<<judge_upload>>` command now means `judge_upload --db db.yml --instance instance.json --repository repository <command>`
 * Sync settings by `<<judge_upload>> settings` (settings are specified through `instance.json`)
 * Sync users by `<<judge_upload>> users users.json` (the passwords of each user is the user name)
 * Sync contest by `<<judge_upload>> contest contest.json --force` (`--force` since the contest is currently running)

## Automation

The `samples` folder also contains a script which demonstrates how to obtain these files from python objects (i.e. how you can use DOMtutor to automate your setup)
Run `python script.py --pretty settings/users/contest` to create the output.

## Fuzzing

To run the fuzzer, execute `cd fuzzer && python fuzzer.py --repository <path to repo>`.
Open `http://localhost:5000` to view the interface.
Copy-paste code of some submission there, select the problem (and language if autodetection doesn't work), and click submit to start fuzzing.

Note: You need the binaries installed which are used to compile & execute the different languages.
