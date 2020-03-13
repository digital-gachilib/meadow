# Meadow

Best digital library ever. Uses [poetry](http://poetry.eustace.io) for package-managing, [black](https://github.com/psf/black) and [isort](https://github.com/timothycrosley/isort) with [seed-isort-config](https://github.com/asottile/seed-isort-config) for code-formatting, and [flake8](http://flake8.pycqa.org/en/latest/) with [pylint](https://www.pylint.org) for linting. [Pre-commit](https://pre-commit.com) hooks are installed for every tool.

## Requirements

1. The poetry should be installed in the system. [How to?](https://python-poetry.org/docs/#installation). Or you can run `bash setup.d/install_all.sh`. This script installs poetry and python3.8, if they aren't accessible


## FAQ
# How to

### use poetry?
Read [this](https://python-poetry.org/docs/basic-usage/) and use [this](https://python-poetry.org/docs/cli/) as reference

#### activate virtual environment ?
```poetry shell```

#### add new dependency?
https://python-poetry.org/docs/basic-usage/#installing-dependencies
