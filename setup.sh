#!/bin/bash
if [ "$EUID" -ne 0 ]
then echo "Please run the script as root :)"
  exit
fi
cd /usr/local/bin/
git clone 'https://github.com/crowded-geek/csearch'
cd csearch
pip install pyperclip
cd
