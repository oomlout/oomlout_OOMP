import OOMP
import os

def addTags(newPart,filter,pins=0,pitch=0,hexID=None,oompType=None,oompSize=None,oompColor=None,oompDesc=None,oompIndex=None):
    if(filter == ""):
        x=0
    if oompType == "FOOTPRINT":
        footprintHex = getFootprintHex(filter)    
        newPart.addTag("hexID",footprintHex)  
    elif("RESE-0603" in filter):
        newPart.addTag("footprintEagle","Adafruit-Eagle-Library/adafruit/R0603")  
        newPart.addTag("footprintKicad","kicad-footprints/Resistor_SMD/R_0603_1608Metric_Pad0.98x0.95mm_HandSolder")  
        newPart.addTag("footprintKicad","kicad-footprints/Resistor_SMD/R_0603_1608Metric")  
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

        ###### FOOTPRINTS
        newPart.addTag("kicadSymbol","Connector/Conn_01x" + pinss + "_Male")
        ##newPart.addTag("kicadFootprint","Connector_PinHeader_2.54mm/PinHeader_1x" + pinss + "_P2.54mm_Vertical")
        ######  Sparkfun footprints
        sparkfunStyles = ["", "_BIG", "_LOCK", "_LOCK_LONGPADS", "_NO_SILK", "_PP_HOLES_ONLY"]
        for style in sparkfunStyles: 
            imageFile = "oomlout_OOMP_eda/footprints/eagle/SparkFun-Eagle-Libraries/Sparkfun-Connectors/1X" + pinss + style + "/image.png"
            #print("Image File: " + imageFile)
            if os.path.isfile(imageFile):
                newPart.addTag("footprintEagle","SparkFun-Eagle-Libraries/Sparkfun-Connectors/1X" + pinss + style)
        
        newPart.addTag("footprintKicad","kicad-footprints/Connector_PinHeader_2.54mm/PinHeader_1x" + pinss + "_P2.54mm_Vertical")
        
    return newPart

def getFootprintHex(filter):
    replaceList = []
    replaceList.append(["FOOTPRINT-","FZ"])
    ### adafruit ones
    ######  Library
    replaceList.append(["eagle-Adafruit-Eagle-Library-adafruit-","A"])
    ######  additions
    replaceList.append(["-CLEANBIG","CB"])
    replaceList.append(["-CB","CB"])
    replaceList.append(["-BIGPOGO","BP"])
    replaceList.append(["-3.5MM","35"])
    replaceList.append(["-BIG","B"])
    replaceList.append(["-SMT","S"])
    replaceList.append(["_SMT","S"])
    replaceList.append(["-LOCK","L"])
    replaceList.append(["-0.7MM","07"])
    replaceList.append(["-0.5MM","05"])

    ### sparkfun ones
    replaceList.append(["eagle-SparkFun-Eagle-Libraries-","S"])
    replaceList.append(["LilyPad-Wearables-","LW"])
    replaceList.append(["SparkFun-Aesthetics-","A"])
    replaceList.append(["SparkFun-Batteries-","B"])
    replaceList.append(["SparkFun-Boards-","BO"])
    replaceList.append(["SparkFun-Buzzard-","BU"])
    replaceList.append(["SparkFun-Capacitors-","C"])
    replaceList.append(["SparkFun-Clocks-","CL"])
    replaceList.append(["SparkFun-Coils-","CO"])
    replaceList.append(["Sparkfun-Connectors-","CN"])
    replaceList.append(["SparkFun-DiscreteSemi-","DS"])
    replaceList.append(["SparkFun-Displays-","D"])
    replaceList.append(["SparkFun-Electromechanical-","E"])
    replaceList.append(["SparkFun-Fuses-","F"])
    replaceList.append(["SparkFun-GPS-","G"])
    replaceList.append(["SparkFun-Hardware-","H"])
    replaceList.append(["SparkFun-IC-Amplifiers-","IA"])
    replaceList.append(["SparkFun-IC-Comms-","IC"])
    replaceList.append(["SparkFun-IC-Conversion-","IV"])
    replaceList.append(["SparkFun-IC-Logic-","IL"])
    replaceList.append(["SparkFun-IC-Memory-","IM"])
    replaceList.append(["SparkFun-IC-Microcontroller-","IU"])
    replaceList.append(["SparkFun-IC-Power-","IP"])
    replaceList.append(["SparkFun-IC-Special-Function-","IS"])
    replaceList.append(["SparkFun-Jumpers-","J"])
    replaceList.append(["SparkFun-LED-","L"])
    replaceList.append(["SparkFun-MicroMod-","M"])
    replaceList.append(["SparkFun-PowerSymbols-","P"])
    replaceList.append(["SparkFun-Resistors-","R"])
    replaceList.append(["SparkFun-Retired-","RT"])
    replaceList.append(["SparkFun-RF-","RF"])
    replaceList.append(["SparkFun-Sensors-","S"])
    replaceList.append(["SparkFun-Switches-","W"])
    replaceList.append(["User-Submitted-","U"])

    ###### sparkfun resistors
    replaceList.append(["",""])
    replaceList.append(["_MURATA","M"])
    replaceList.append(["_NO_CREAM","NC"])
    replaceList.append(["-TIGHT","T"])
    replaceList.append(["_RA","RA"])
    replaceList.append(["-KIT","K"])
    replaceList.append(["AXIAL-","A"])
    replaceList.append(["TRIMPOT-SMD","TS"])
    

    ### common ones
    replaceList.append(["",""])
    replaceList.append(["0204","24"])
    replaceList.append(["0207","27"])
    replaceList.append(["0204","24"])
    replaceList.append(["0402","42"])
    replaceList.append(["0603","63"])
    ###### MM
    for x in range(9):
        xs = str(x)
        replaceList.append("-0" + xs + "MM",xs)
        replaceList.append("-0" + xs + "mm",xs)
        replaceList.append("-" + xs + "MM",xs)
        replaceList.append("-" + xs + "mm",xs)
        replaceList.append(xs + "MM",xs)
        replaceList.append(xs + "MM",xs)



    for replace in replaceList:
        filter = filter.replace(replace[0],replace[1])
    return filter