echo "Checking python"
(python3.8 --version || (echo "Python3.8 isn't installed" && bash install_python.sh))
(poetry --version || (echo "Poetry isn't installed" && bash install_poetry.sh))
echo "Installing venv"
poetry install
poetry run pre-commit install
