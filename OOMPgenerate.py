import OOMP




def generateLabel(item):
    oompID = item.getTag("oompID")
    #inventory label
    template = "templates\\OOMP-label-inventory.tmpl.svg"
    output = "parts\\" + oompID.value + "\\label-inventory.svg"
    oompSearchAndReplace(template, output, item)




def oompSearchAndReplace(inFile,outFile,item):
    oompID = item.getTag("oompID")
    
    f = open(inFile, "r")
    template = f.read()

    template = template.replace("%%ID%%", oompID.value)

    toReplace = template.split("@@")

    for x in toReplace:
        print(x)

    
part = OOMP.parts[256]

print(part)
generateLabel(part)
