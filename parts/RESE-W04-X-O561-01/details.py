import OOMP

newPart = OOMP.oompItem(9507)
newPart.addTag("oompType", "RESE")
newPart.addTag("oompSize", "W04")
newPart.addTag("oompColor", "X")
newPart.addTag("oompDesc", "O561")
newPart.addTag("oompIndex", "01")

newPart.addTag("hexID","R4561")
newPart.addTag("oompSort","0W040000560")
newPart.addTag("oompType","RESE")
newPart.addTag("oompSize","W04")
newPart.addTag("oompColor","X")
newPart.addTag("oompDesc","O561")
newPart.addTag("oompIndex","01")
newPart.addTag("oompVersion","21")
newPart.addTag("ooWidth","62.8 mm")
newPart.addTag("ooDiameter","2.5 mm")
newPart.addTag("ooLength","6.8 mm")
newPart.addTag("ooMaterial","Carbon")
newPart.addTag("ooMaxVoltage","500 V")
newPart.addTag("ooTolerance","5%")
newPart.addTag("ooDesignator","R1")

newPart.addTag("oompClass","Through Hole Component")
newPart.addTag("oompClassCode","THTH")

newPart.addTag("colorBand1","GREEN")
newPart.addTag("colorBand2","BLUE")
newPart.addTag("colorBand3","BROWN")

newPart.addTag("oompBbls","template;RESE-W04-X-XXXX-XX-bbls")
newPart.addTag("oompDiag","template;RESE-W04-X-XXXX-XX-diag")
newPart.addTag("oompIden","template;RESE-W04-X-XXXX-XX-iden")
newPart.addTag("oompSchem","template;RESE-XXXX-X-XXXX-XX-schem")
newPart.addTag("oompSimp","template;RESE-W04-X-XXXX-XX-simp")


###### KICAD DETAILS
newPart.addTag("kicadSymbol","Device>R")
newPart.addTag("kicadFootprint","Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal")

OOMP.parts.append(newPart)
