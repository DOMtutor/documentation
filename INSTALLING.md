# Initial Setup for DOMtutor

 * Clone all necessary repositories in some folder, say `<root>`
 * Create a virtual environment in `<root>`: `python3 -m venv venv` and activate it: `. ./venv/bin/activate`
 * `pip install <a lot of things>` (There are some requirements.txt files which aren't completely up to date ...)
 * Setting up Kattis problemtools -- Inside `<root>/problemtools`
   * `git submodule init --update --recursive`
   * `make` (may need `libgmp-dev`) to compile `checktestdata`
   * `pip install -e` to install problemtools into the venv
 * Installing pyjudge: `cd <root>/pyjudge && pip install -e`

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

Now you can run `judge_upload --db <db settings> --instance <path to instance.json> --repository repository <actual command>`


