# Meadow
![Python application](https://github.com/digital-gachilib/meadow/workflows/Python%20application/badge.svg)

Best digital library ever. Uses [black](https://github.com/psf/black) and [isort](https://github.com/timothycrosley/isort) with [seed-isort-config](https://github.com/asottile/seed-isort-config) for code-formatting, and [flake8](http://flake8.pycqa.org/en/latest/) for linting. [Pre-commit](https://pre-commit.com) hooks are installed for every tool.

## How to develop?

#### Commit messages' style
The project follows [conventional commits](https://www.conventionalcommits.org/en/v1.0.0-beta.2/) style for commit messages. 
This naming isn't mandatory for regular commits but very appreciated among team members. However, for Pull Request's titles this style is **very-very** recommended.

#### Project first setup
All commands should be runned inside project's directory

1. Create virtual environment
`python3 -m venv .venv`
2. Activate venv
`. .venv/bin/activate`
3. Install all libraries
`pip install -r requirements.txt`
4. Install pre-commit hooks
`pre-commit install`
5. Everything is installed! Run `python meadow/manage.py migrate` to apply migrations and `python meadow/manage.py runserver` to run server locally. (the database should listen on port ('localhost', 5432), you can run it using [run_postgres.sh](init.d/run_postgres.sh) script.

## New dependency?

1. Add it to [requirements.txt](requirements.txt) with `pip freeze > requirements.txt`
2. Add it to stage in git
`git add requirements.txt`
3. Commit
`git commit -m "feat: add *library_name* to requirements.txt"`
4. Push
`git push --set-upstream origin $(git_current_branch)`
5. Open pull-request. You can use a web GUI of github, or with [hub](https://hub.github.com) with command `hub pull-request -op -m "New cool PR!"`

## Some Q&A

* How to update locally project?
`git pull --rebase --autostash`
