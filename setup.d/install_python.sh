echo "Installing python3.8..."
apt update
apt install -y software-properties-common
add-apt-repository -y ppa:deadsnakes/ppa
apt install python3.8
echo "Python3.8 is accessible by python3.8 command. Running python3.8 --version: "
python3.8 --version
sleep 5
