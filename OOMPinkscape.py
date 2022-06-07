import OOMP

def generateDiagrams(item, renders=False):    
    oompID = item.getTag("oompID").value
    print("Drawing item: " + oompID)
    types = ["Bbls"]
    if not "TEMPLATE" in oompID:
        for type in types:
            print("    Type: " + type)
            outFile = "parts\\" + oompID + "\\diag" + type.upper() + ".py" 
            f = open(outFile,"w")
            tags = item.tags
            for tag in tags:
                if tag.name == "oomp" + type:
                    line = tag.value.replace("\n","") 
                    
                    line = processCommand(line)
                    print(line)
                    f.write(line + "\n")

def processCommand(line):
    line= line.replace("%%","")
    details = line.split(";")
    type = details[0]
    print("Details: ", details)
    if(type == "XXXX"):
        type = type
######  LINEWIDTH    
    elif(type == "linewidth"):
        line = "linewidth = " + details[1] + "    #  " + line
######  RECTANGLE    
    elif(type == "rectangle"):
        line2 = line
        line = "x = " + details[1] + "    #  " + line2 + "\n"
        line = line + "y = " + details[2] + "\n"
        line = line + "width = " + details[3] + "\n"
        line = line + "height = " + details[4] + "\n"
        line = line + "x1 = x - width/2 \ny1 = y + height/2 \nx2 = x + width/2 \ny2 = y - height/2 \nrect((x1,y1), (x2,y2),0.1,stroke_width=linewidth)"
######  REPEAT
    elif(type == "repeat"):        
        shorterCommand = ""
        index = 0
        for a in details:
            if index < 2:
                index = index + 1
            else:
                shorterCommand = shorterCommand + a + ";"    
        line2 = line
        line = "for b in range(" + details[1] + "):" + "    # " + line2 + "\n" + "    i = b + 1\n" + "    " + processCommand(shorterCommand).replace("\n","\n    ")
######  TEMPLATE    
    elif(type == "template"):
        line = "# TEMPLATE  " + line + "\n"
        item = OOMP.getPartByHex(details[1])            
        tags = item.tags
        for tag in tags:
            if tag.name == "drawItem":
                line = line + processCommand(tag.value) + "\n"
######  VARIABLE        
    elif(type == "variable"):
        if not details[1] == "clear": 
            line = details[1] + " = " + details[2] + "    #  " + line
        else:
            line = "#  CLEAR " + line
        
    else:
        line = "#  " + line
    return line


