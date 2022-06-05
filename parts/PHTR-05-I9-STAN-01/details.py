import OOMP

newPart = OOMP.oompItem(9183)
newPart.addTag("oompType", "PHTR")
newPart.addTag("oompSize", "05")
newPart.addTag("oompColor", "I9")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")

newPart.addTag("hexID","PT5I9")

newPart.addTag("oompClass","Through Hole")
newPart.addTag("oompClassCode","THTH")

newPart.addTag("ooDesignator","Q1")


###### KICAD DETAILS
newPart.addTag("kicadSymbol","Device>R_Photo")
newPart.addTag("kicadFootprint","OptoDevice:R_LDR_10x8.5mm_P7.6mm_Vertical")

OOMP.parts.append(newPart)
