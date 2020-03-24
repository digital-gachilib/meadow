echo "Checking python"
(python3.8 --version && echo "Python3 is already installed!") || (echo "Python3.8 isn't installed" && sleep 3 && bash install_python.sh)
(poetry --version && echo "Poetry is already installed!")|| (echo "Poetry isn't installed" && sleep 3 && bash install_poetry.sh)
(docker --version && echo "Docker is already installed!") || (echo "Docker isn't installed" && sleep 3 && bash install_docker.sh)
