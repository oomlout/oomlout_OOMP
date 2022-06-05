import OOMP

newPart = OOMP.oompItem(8962)
newPart.addTag("hexID", "H03R")
newPart.addTag("oompType", "HEAD")
newPart.addTag("oompSize", "I01")
newPart.addTag("oompColor", "X")
newPart.addTag("oompDesc", "PI03")
newPart.addTag("oompIndex", "RA")
newPart.addTag("oompSort", "HEADI0103PI")
newPart.addTag("ooPitch", 2.54)
newPart.addTag("ooPinHeight", 11.60)
newPart.addTag("ooPinWidth", 0.64)
newPart.addTag("ooPinOffset", 1.53)
newPart.addTag("ooNumPins", 3)
newPart.addTag("ooFootprint", "OOMP-HEAD-I01-X-PI03-RA")
newPart.addTag("ooDesignator", "J1")

#####  Sourcing
newPart.addTag("manufacturer", {"YXCON","C-YXCO","","P125-1103A0BR138A1","",""})
newPart.addTag("opl", {"SEEED OPL","C-SEEE","DIP Black Male Header R/A","320020061","","https://www.seeedstudio.com/opl.html"})

###### KICAD DETAILS
newPart.addTag("kicadSymbol","Connector:Conn_01x03_Male")
newPart.addTag("kicadFootprint","Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Horizontal")

OOMP.parts.append(newPart)
