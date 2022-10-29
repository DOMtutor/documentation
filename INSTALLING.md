# Initial Setup for DOMtutor

 * Clone all necessary repositories in some folder, say `<root>`
 * Create a virtual environment in `<root>`: `python3 -m venv venv` and activate it: `. ./venv/bin/activate`
 * `pip install <a lot of things>` (There are some requirements.txt files which aren't completely up to date ...)
   * `plastex`
 * Setting up Kattis problemtools -- Inside `<root>/problemtools`
   * `git submodule init --update --recursive`
   * `make` (may need `libgmp-dev`) to compile `checktestdata`
   * `pip install -e` to install problemtools into the venv
 * Installing pyjudge: `cd <root>/pyjudge && pip install -e`
 * To build problems you may also need `texlive-latex-extra poppler-utils` (or your distribution's equivalent)

## Local Experiments

 * Follow `domjudge-deployment` / `local`
 * Create a file `<root>/db.yml` with:
   ```yml
   host: 127.0.0.1
   port: 3306
   user: domjudge
   password: domjudge
   database: domjudge
   ```
 * Adapt the json files in `samples` as needed; add/change the problems in repository
 * The `<<judge_upload>>` command now means `judge_upload --db db.yml --instance instance.json --repository repository <command>`
 * Sync settings by `<<judge_upload>> settings` (settings are specified through `instance.json`)
 * Sync users by `<<judge_upload>> users users.json`
 * Sync contest by `<<judge_upload>> contest contest.json`

