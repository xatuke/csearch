# csearch
Basically csearch will help you search whatever you have on your clipboard using the keyboard shortcut you want.

## Prerequisites
- Python 3
- pip3
- Linux Operating System

## Setup
```
wget https://raw.githubusercontent.com/crowded-geek/csearch/master/setup.sh
chmod +x setup.sh
sudo ./setup.sh
```

## Keyboard shortcut setup
- Go to keyboard shortcuts in your settings
- Add a new keyboard shortcut with following details:
  ```
  Name: <whatever you like>
  Command: /usr/bin/python3 /usr/local/bin/csearch/copysearch.py
  Shortcut: <whatever you like> or Alt+s
  ```
  ### If you want to use DuckDuckGo as your search engine:
  ```
  Name: <whatever you like>
  Command: /usr/bin/python3 /usr/local/bin/csearch/copysearch.py ddg
  Shortcut: <whatever you like> or Alt+s
  ```

### Why run the script as root?
> It needs to create it's folder in `/usr/local/bin` to install itself.
