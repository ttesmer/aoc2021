#!/usr/bin/python
import datetime as dt
import time
from advent import *
import requests

"""
1. Paste session cookie from adventofcode.com into string below.
2. Create an alias in ~/.zshrc or ~/.bash_profile to `python $HOME/path/to/wait.py`.
"""

SESSION_COOKIE = ""

URL = lambda y, d: f"https://adventofcode.com/{y}/day/{d}/input"

def get_input(day, *kwargs):
    with open("i", "wb") as f:
        res = requests.get(url=URL("2021",day), cookies={'session': SESSION_COOKIE})
        if res.status_code == 200:
            print("Response:", res.status_code, "✅")
            f.write(res.content)
            #print("\n\033[92mInput dump complete. Good luck!\033[0m")
            #print("*--- INPUT INFO ---* ")
            #print("\nNumber of rows:", len(res.text.strip().split("\n")))
            #print("\nHead of input:")
            #for j in res.text.strip().split("\n")[0:2]:
            #    print("\033[96m", j)
            #    print("\033[0m", ints(j), "<= 'ints'")
            #    print("", words(j), "<= 'words'")
            f.close()
        else:
            print("\033[91m(ERROR) Response:", res.status_code, "❌")




def wait():
    while True:
        print(dt.datetime.now().time())
        if dt.datetime.now().time() >= dt.time(6,0,0,0):
            day = dt.datetime.now().day
            print("Getting input..")
            time.sleep(1)
            try:
                get_input(day)
                break
            except:
                print("Failed to get input.. trying again")
                pass

if __name__ == "__main__":
    wait()
