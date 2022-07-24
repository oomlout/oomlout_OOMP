import OOMP
import os

def addTags(newPart,filter,pins=0,pitch=0,hexID=None,oompType=None,oompSize=None,oompColor=None,oompDesc=None,oompIndex=None):
    if(filter == ""):
        x=0
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

