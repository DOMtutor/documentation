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
