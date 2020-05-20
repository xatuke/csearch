#!/bin/bash
cd /usr/local/bin/
#git clone ''
cd copysearch
pip install pyperclip
bind '"\C-m"':'"/usr/bin/python3 /usr/local/bin/copysearch/copysearch.py\n"'
