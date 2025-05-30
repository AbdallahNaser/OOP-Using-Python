import random
import webbrowser

websites=[
    "https://www.facebook.com",
    "https://www.google.com",
    "https://www.instagram.com",
    "https://www.x.com",
    "https://www.python.org"
]

rand=random.choice(websites)
webbrowser.open(rand)