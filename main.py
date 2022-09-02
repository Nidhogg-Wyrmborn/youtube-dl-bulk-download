from subprocess import call, STDOUT
import os, sys
from datetime import datetime
import argparse
import time

def hasaudio(link):
    if "-x" in link.split(" ")[1:]:
        return True
    else:
        return False

def removeSwitch(link):
    return link.split(" ")[0]

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="show verbose information for debug", action="store_true")
args = parser.parse_args()

if args.verbose:
    print("Running with verbose")

if "win" in sys.platform:
    os.system("cls")
else:
    os.system("clear")
if args.verbose:
    print("checking for updates for youtube-dl")
    print(f"currently running on {sys.platform}")
    os.system("youtube-dl --version")
print()
os.system("youtube-dl -U")
print()
with open("links.txt", 'r') as f:
    links = f.readlines()
count = 0
for i in range(len(links)):
    if links[i-count].startswith("//") or links[i-count]=='\n':
        if args.verbose:
            print(f"popping {links[i-count]}")
        links.pop(i-count)
        count+=1
    links[i-count] = links[i-count].replace("\n", "")

if args.verbose:
    print(f"\n{links}\n")
success = []
for link in links:
    a = 1
    count = 0
    if not hasaudio(link):
        link = removeSwitch(link)
        while a != 0 and a != 255:
            if count < 5:
                a = os.system(f"youtube-dl --write-sub --embed-subs \"{link}\"")
            if count >= 5:
                if "win" in sys.platform:
                    os.system("cls")
                else:
                    os.system("clear")
                a = os.system(f"youtube-dl -v --write-sub --embed-subs \"{link}\"")
                if a != 0:
                    print("please copy and paste the above result into an issue on YOUTUBE-DLs github")
                    print("\nyoutube-dl version: ", end="")
                    os.system("youtube-dl --version")
                    print("\nhttps://github.com/ytdl-org/youtube-dl")
                    print()
                    print("this program is a custom script to make using youtube-dl easier and more efficient with less babysitting")
                    print("please create an issue in this script's github in the event that it is related to this program")
                    print("\nhttps://github.com/Nidhogg-Wyrmborn/youtube-dl-bulk-download\n")
                    print("please include these last lines in all issues created as it will help the developers of youtube-dl to ascertain whether it is their program or mine at fault")
                    print("\nthank you\n\nplease be aware that some errors are caused by lack of internet, if these errors persist in 10-20 minutes please report them\n\n")
                    print(f"Current download: {link}"+"\n\n")
                    print(f"List of succesful downloads:\n"+('\n- '.join(success) if len(success) >= 1 else "NONE"))
                    time.sleep(5)
                    quit()
            count += 1
            print(f"\nError Code: {a}\n")
    if hasaudio(link):
        link = removeSwitch(link)
        while a != 0 and a != 255:
            if count < 5:
                a = os.system(f"youtube-dl -x --audio-format mp3 \"{link}\"")
            if count >= 5:
                if "win" in sys.platform:
                    os.system("cls")
                else:
                    os.system("clear")
                a = os.system(f"youtube-dl -v -x --audio-format mp3 \"{link}\"")
                if a != 0:
                    print("please copy and paste the above result into an issue on YOUTUBE-DLs github")
                    print("\nyoutube-dl version: ", end="")
                    os.system("youtube-dl --version")
                    print("\nhttps://github.com/ytdl-org/youtube-dl")
                    print()
                    print("this program is a custom script to make using youtube-dl easier and more efficient with less babysitting")
                    print("please create an issue in this script's github in the event that it is related to this program")
                    print("\nhttps://github.com/Nidhogg-Wyrmborn/youtube-dl-bulk-download\n")
                    print("please include these last lines in all issues created as it will help the developers of youtube-dl to ascertain whether it is their program or mine at fault")
                    print("\nthank you\n\nplease be aware that some errors are caused by lack of internet, if these errors persist in 10-20 minutes please report them\n\n")
                    print(f"Current download: {link}"+"\n\n")
                    print(f"List of succesful downloads:\n"+('\n- '.join(success) if len(success) >= 1 else "NONE"))
                    time.sleep(5)
                    quit()
    success.append(link)
