import OOMP

def generateReadmeIndex():
    outFile = "parts\\Readme.md"
    f = open(outFile, "w")
    for item in OOMP.parts:
        line = item.indexMd()
        if(not "TEMPLATE" in line):
            f.write(line + "  \n")

    f.close()

def generateReadme(item):
    oompID = item.getTag("oompID").value
    outFile = "parts\\" + oompID + "\\Readme.md"
    if not "TEMPLATE" in oompID:
        f = open(outFile, "w")
        f.write(item.mdPage())
        f.close()
