import OOMP

newPart = OOMP.oompItem(9187)
newPart.addTag("oompType", "POTE")
newPart.addTag("oompSize", "95D")
newPart.addTag("oompColor", "L")
newPart.addTag("oompDesc", "O103")
newPart.addTag("oompIndex", "01")


newPart.addTag("hexID","PTA103")

newPart.addTag("oompClass","Through Hole Component")
newPart.addTag("oompClassCode","THTH")

newPart.addTag("ooDesignator","VR1")


###### KICAD DETAILS
newPart.addTag("kicadSymbol","Device>R_Potentiometer")


OOMP.parts.append(newPart)
