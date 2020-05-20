import webbrowser
import pyperclip
import sys
query = pyperclip.paste();
if(len(sys.argv)>1):
    if(str(sys.argv[1])=="ddg"):
        webbrowser.open("https://duckduckgo.com/?q="+query)
else:
    webbrowser.open("https://google.com/search?q="+query)
