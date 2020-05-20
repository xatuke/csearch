import webbrowser
import pyperclip
query = pyperclip.paste();
webbrowser.open('https://www.google.com/search?&q='+query)
