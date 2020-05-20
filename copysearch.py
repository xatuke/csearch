import webbrowser
import pyperclip
query = pyperclip.paste();
web= webbrowser.open('https://www.google.com/search?&q='+query)
exit()
