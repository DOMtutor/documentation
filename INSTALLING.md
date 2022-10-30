# Initial Setup for DOMtutor

 * Clone all necessary repositories in some folder (all commands below are relative to this folder)
 * Create a virtual environment with `python3 -m venv venv` and activate it with `. ./venv/bin/activate`
 * `pip install <a lot of things>` (There are some requirements.txt files which aren't completely up to date ...)
   * `plastex`
 * Setting up Kattis problemtools - Inside `problemtools`
   * `git submodule init --update --recursive`
   * `make` (may need `libgmp-dev`) to compile `checktestdata`
   * `pip install -e` to install problemtools into the venv
 * Installing pyjudge in the venv: `cd pyjudge && pip install -e`
 * To build problems you may also need `texlive-latex-extra poppler-utils` (or your distribution's equivalent)

## Local Experiments

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
 * Adapt the json files in `samples` as needed; add/change the problems in repository
 * The `<<judge_upload>>` command now means `judge_upload --db db.yml --instance instance.json --repository repository <command>`
 * Sync settings by `<<judge_upload>> settings` (settings are specified through `instance.json`)
 * Sync users by `<<judge_upload>> users users.json` (the passwords of each user is the user name)
 * Sync contest by `<<judge_upload>> contest contest.json --force` (`--force` since the contest is currently running)
 * The `samples` folder also contains a script which demonstrates how to obtain these files from python objects (i.e. how you can use DOMtutor to automate your setup)
   Run `python script.py --pretty settings/users/contest` to create the output.
