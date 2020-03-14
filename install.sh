#!/bin/bash
for i in "$@"; do
    case $i in
    -n=* | --name=*)
        DIR_NAME="${i#*=}"
        ;;
    esac
done

git clone --progress git@github.com:digital-gachilib/meadow.git &&
    cd meadow && sudo bash init.d/install_all.sh
