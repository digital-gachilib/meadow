# Meadow

Best digital library ever. Uses [black](https://github.com/psf/black) and [isort](https://github.com/timothycrosley/isort) with [seed-isort-config](https://github.com/asottile/seed-isort-config) for code-formatting, and [flake8](http://flake8.pycqa.org/en/latest/) with [pylint](https://www.pylint.org) for linting. [Pre-commit](https://pre-commit.com) hooks are installed for every tool.

## How to develop?

1. Create virtual environment
`python3 -m venv .venv`
2. Activate venv
`. .venv/bin/activate`
3. Install all libraries
`pip install -r requirements.txt`
4. Everything is installed! Run `python meadow/manage.py migrate` to apply migrations and `python meadow/manage.py runserver` to run server locally

## New dependency?

1. Add it to [requirements.txt](requirements.txt) with `pip freeze > requirements.txt`
2. Add it to stage in git
`git add requirements.txt`
3. Commit
`git commit -m "feat: add *library_name* to requirements.txt"`
4. Push
`git push --set-upstream origin $(git_current_branch)`
5. Open pull-request. You can use a web GUI of github, or with [hub](https://hub.github.com) with command `hub pull-request -op -m "New cool PR!"`
