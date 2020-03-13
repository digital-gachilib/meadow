echo "installing poetry..."
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
echo "poetry is installed!"
poetry --version
sleep 3
poetry env use python3.8
poetry env info
sleep 5
