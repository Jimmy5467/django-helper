################ dont forget to add {% load static %} in head section ###############3

import fileinput
import re

fileToSearch = input("> ")
fin = open(fileToSearch, "rt")  # for e.g: ../dummy.html
fout = open("../out.html", "wt")

for line in fin:
    pattern = r'\".*?\"'
    if re.findall(pattern, line):
        ori = re.findall(pattern, line)[0]
        if ori.find("svg") or ori.find("jpg") or ori.find("jepg") or ori.find("png") or ori.find("css") or ori.find("scss") or ori.find("html") or ori.find("js"):
            changed = "'{% static " + ori + " %}'"
            # read replace the string and write to output file
            fout.write(line.replace(ori, changed))
    else:
        fout.write(line)
# close input and output files
fin.close()
fout.close()


# 1. make requiremnet.txt
# 2. make dajngo webiste
# 3. use heroku
# 4. make user interface