import OOMP

types = ["Bbls","Diag","Iden","Schem","Simp"]

def generateDiagrams(item, renders=False):   
    print(item.fullString()) 
    oompID = item.getTag("oompID").value
    print("Drawing item: " + oompID)
    global types
    types = types
    if not "TEMPLATE" in oompID:
        for type in types:
            print("    Type: " + type)
            folder = "parts/" + oompID + "/"
            outFile = folder + "diag" + type.upper() + ".py" 
            f = open(outFile,"w")
            tags = item.tags
            for tag in tags:
                if tag.name == "oomp" + type:
                    line = tag.value.replace("\n","") 
                    
                    line = processCommand(line,item)
                    print(line)
                    f.write(line + "\n")
            f.write('os.chdir("C:/GH/oomlout-OOMP/' + folder + '")\n')                
            f.write("inkex.command.write_svg(svg_root, 'diag" + type.upper() + ".svg')")
            f.close()

def processCommand(line,item):
    line2 = line
    hexID = item.getTag("hexID").value
    name = item.getTag("name").value
    line= line.replace("%%","")
    details = line.split(";")
    if len(details) > 0:
        type = details[0]
    if len(details) > 1:
        x = details[1] 
    if len(details) > 2:    
        y = details[2]
    if len(details) > 3:    
        width = details[3]
    if len(details) > 4:            
        height = details[4]
    print("Details: ", details)
    if(type == "XXXX"):
        type = type
######  LINEWIDTH    
    elif(type == "linewidth"):
        line = "linewidth = " + details[1] + "    #  " + line
######  OOMPURL    
    elif(type == "oompURL"):
        text = '"http://oom.lt/' + hexID + '"'       
        line = "x = " + x + "    #  " + line2 + "\n"
        line = line + "y = " + y + "\n"
        line = line + "width = " + "20" + "\n"
        line = line + "height = " + "5" + "\n"
        line = line + "x1 = x - width/2 \ny1 = y + height/2 \nx2 = x + width/2 \ny2 = y - height/2 \nshape = rect((x1,y1), (x2,y2),0.1,stroke_width=0)\n"
        line = line + "x = " + x + "    #  " + line2 + "\n"
        line = line + "y = " + y + "\n"
        line = line + "width = " + "0" + "\n"
        line = line + "height = " + "0" + "\n"        
        line = line + "x1 = x - width/2 \ny1 = y + height/2 \nx2 = x + width/2 \ny2 = y - height/2 \nshape = text(" + text + ", (0, 0),stroke_width=0.2,font_size='2.835pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)"        
        #shape = rect()
        #t = text()

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
        line = "for b in range(" + details[1] + "):" + "    # " + line2 + "\n" + "    i = b + 1\n" + "    " + processCommand(shorterCommand,item).replace("\n","\n    ")
######  TEMPLATE    
    elif(type == "template"):
        line = "# TEMPLATE  " + line + "\n"
        item = OOMP.getPartByHex(details[1])            
        tags = item.tags
        print("Tag Length:" ,len(tags))
        if(len(tags) > 1):
            for tag in tags:
                if tag.name == "drawItem":
                    line = line + processCommand(tag.value,item) + "\n"
        else:
            line = "# MISSING TEMPLATE " + line
######  VARIABLE        
    elif(type == "variable"):
        if not details[1] == "clear": 
            line = details[1] + " = " + details[2] + "    #  " + line
        else:
            line = "#  CLEAR " + line
        
    else:
        line = "#  " + line
    return line


def addTags(newPart,filter,pins=0):
    if(filter == ""):
        x=0
    elif(filter == "HEAD-I01-X-X-X"):
        pinss = "{:02d}".format(pins)
        newPart.addTag("oompType", "HEAD")
        newPart.addTag("oompSize", "I01")
        newPart.addTag("oompColor", "X")
        newPart.addTag("oompDesc", "PI" + pinss)
        newPart.addTag("oompIndex", "01")

        newPart.addTag("hexID","H" + pinss)
        newPart.addTag("oompSort","")

        newPart.addTag("oompClass","Through Hole")
        newPart.addTag("oompClassCode","THTH")
        newPart.addTag("ooPitch","2.54")
        newPart.addTag("ooPinHeight","11.60")
        newPart.addTag("ooPinWidth","0.64")
        newPart.addTag("ooPinOffset","1.53")
        newPart.addTag("oompBbls","variable;pins;" + str(pins) )
        newPart.addTag("oompBbls","template;XXXX-I01-X-XX-01-bbls")
        newPart.addTag("oompDiag","variable;pins;" + str(pins) )
        newPart.addTag("oompDiag","template;HEAD-I01-X-XX-01-diag")
        newPart.addTag("oompIden","variable;pins;" + str(pins) )
        newPart.addTag("oompIden","template;XXXX-I01-X-XX-01-iden")
        newPart.addTag("oompSchem","variable;pins;" + str(pins) )
        if pins % 2 == 1:
            newPart.addTag("oompSchem","template;XXXX-XX-X-XX-01-PINS-ODD-schem")
        else:
            newPart.addTag("oompSchem","template;XXXX-XX-X-XX-01-PINS-EVEN-schem")
        newPart.addTag("oompSimp","variable;pins;" + str(pins) )
        newPart.addTag("oompSimp","template;XXXX-I01-X-XX-01-simp")
        newPart.addTag("ooNumPins",str(pins))
        newPart.addTag("ooFootprint","OOMP-HEAD-I01-X-PI" + pinss + "-01")

        newPart.addTag("ooDesignator","J1")
        newPart.addTag("schematicSymbol","HEAD-XX-X-PI" + pinss + "-XX")
        newPart.addTag("pcbFootprint","HEAD-I01-X-PI" + pinss + "-01")

        ###### KICAD DETAILS
        newPart.addTag("kicadSymbol","Connector>Conn_01x" + pinss + "_Male")
        newPart.addTag("kicadFootprint","Connector_PinHeader_2.54mm:PinHeader_1x" + pinss + "_P2.54mm_Vertical")


    return newPart