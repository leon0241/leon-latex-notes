from TexSoup import TexSoup
import re

INPUT_FILE = "algebra-6p/raw.tex"
OUTPUT_FILE = "algebra-6p/algebra-6p.tex"

rawdoc = ""

with open(INPUT_FILE,'r') as f:
    rawdoc = f.readlines()
    print(rawdoc)

doc_start = 0
for i in range(len(rawdoc)):
    if rawdoc[i] == "\\begin{document}":
        doc_start == i
        break

thmboxes = ["thm", "dfn", "xmp", "rem"]

newdoc = []

in_thm = False

for i in range(doc_start, len(rawdoc)):
    line = rawdoc[i]
    
    print(line)
    if line.startswith("\\section"):
        newdoc.append(line)
        continue
    elif re.findall("\\begin\\{(thm|dfn|xmp|rem)}", line) != []:
        in_thm = True
        newdoc.append(line)
        continue
    elif re.findall("\\end\\{(thm|dfn|xmp|rem)}", line) != []:
        in_thm = False
        newdoc.append(line)
        continue
    elif in_thm == True:
        newdoc.append(line)
        continue

print(newdoc)
