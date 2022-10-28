from subprocess import call, STDOUT
import os, sys
import subprocess
import argparse
import time

def isen(link):
    print(link.split(" ")[1:])
    if "-l" in link.split(" ")[1:]:
        return True
    else:
        return False

def switch(link):
    print(link.split(" ")[1:])
    if "-f" in link.split(" ")[1:]:
        return True
    else:
        return False

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
spectype = str(input("please input language code (e.g. en-US):\n- "))
for link in links:
    a = 1
    count = 0
    if not hasaudio(link):
        if isen(link):
            lang = link.split("-l")[-1:][0].split(" ")[1]
            link = removeSwitch(link)
            while a != 0 and a != 255:
                if count < 5:
                    a = os.system(f"youtube-dl --write-sub --embed-subs --sub-langs \"{lang}\" \"{link}\"")
                if count >= 5:
                    if "win" in sys.platform:
                        os.system("cls")
                    else:
                        os.system("clear")
                    a = os.system(f"youtube-dl -v --write-sub --embed-subs --sub-langs \"{lang}\" \"{link}\"")
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
        if switch(link):
            lang = None
            if isen(link):
                lang = link.split("-l")[-1:][0].split(" ")[1]
            spec = ''
            a = subprocess.getoutput(f"youtube-dl -F \"{link}\"")
            #print(a)
            a = a.split("resolution note\n")[1]
            #print(a)
            a = a.split("\n")
            a.reverse()
            for i in a:
                if spectype in i:
                    spec = i.split(" ")[0]
                    break
            print(f"Selected Format: {spec}")
            link = removeSwitch(link)
            while a != 0 and a != 255:
                if count < 5:
                    if lang:
                        a = os.system(f"youtube-dl -f {spec} --write-sub --embed-subs --sub-langs \"{lang}\" \"{link}\"")
                    else:
                        print(f"youtube-dl -f {spec} \"{link}\"")
                        a = os.system(f"youtube-dl -f {spec} \"{link}\"")
                if count >= 5:
                    if "win" in sys.platform:
                        os.system("cls")
                    else:
                        os.system("clear")
                    if lang:
                        a = os.system(f"youtube-dl -v -f {spec} --write-sub --embed_subs --sub-langs \"{lang}\" \"{link}\"")
                    if not lang:
                        a = os.system(f"youtube-dl -v -f {spec} \"{link}\"")
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

        else:
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
