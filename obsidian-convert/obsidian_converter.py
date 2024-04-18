import re

INPUT_FILE = "file.txt"


print("test")
with open(INPUT_FILE,'r') as f:
    rawdoc = f.readlines()


in_itemize = False


newdoc = []
for line in rawdoc:
    newline = line[:-1]
    
    # if it's a theorem title box then skip
    if newline.startswith("> [!"):
        continue
    # get rid of floating box thing
    if newline.startswith("> "):
        newline = newline[2:]
    # convert proper math mode
    if newline.startswith("$$") and newline.endswith("$$"):
        newline = "\\[" + newline[2:-2] + "\\]"
    elif newline.startswith("$$"):
        newline = "\\[" + newline[2:]
    elif newline.endswith("$$"):
        newline = newline[:-2] + "\\]"




    # start itemize environment
    if not in_itemize and newline.startswith("- "):
        in_itemize = True
        newdoc.append("\\begin{itemize}")
        newdoc.append("\t\\setlength\\itemsep{0em}")
        newline = re.sub("\-", r"\\item", newline)
        newline = "\t" + newline
    # end of itemize
    elif in_itemize and newline == "":
        in_itemize = False
        newdoc.append("\\end{itemize}")
    # itemize - add an item
    elif in_itemize and newline.startswith("- "):
        newline = re.sub("^\-", r"\\item", newline)
        newline = "\t" + newline
    # itemize - inline item
    elif in_itemize:
        newline = "\t" + newline

    newline = re.sub("\*\*([^\*]*)\*\*", r"\\textbf{\1}", newline)
    newline = re.sub("\*([^\*]*)\*", r"\\textbf{\1}", newline)
    newline = re.sub("\[\[[^\]]*\|([^\]]*)\]\]", r"\1", newline)

    newdoc.append(newline)

# if eof and still in itemize, close
if in_itemize:
    in_itemize = False
    newdoc.append("\\end{itemize}")

with open(INPUT_FILE,'w') as f:
    for i in range(len(newdoc) - 1):
        f.write(f"\t{newdoc[i]}\n")
    f.write(f"\t{newdoc[-1]}")
