import OOMP

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

