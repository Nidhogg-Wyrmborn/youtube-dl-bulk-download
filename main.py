from subprocess import call, STDOUT
import os

with open("links.txt", 'r') as f:
    links = f.readlines()
count = 0
for i in range(len(links)):
    if links[i-count].startswith("//") or links[i-count]=='\n':
        print(f"popping {links[i-count]}")
        links.pop(i-count)
        count+=1
    links[i-count] = links[i-count].replace("\n", "")

print(links)

for link in links:
    a = 1
    while a != 0 and a != 255:
        a = os.system(f"youtube-dl --write-sub \"{link}\"")
        print(a)
