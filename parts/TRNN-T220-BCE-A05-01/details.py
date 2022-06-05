import OOMP

newPart = OOMP.oompItem(9547)
newPart.addTag("oompType", "TRNN")
newPart.addTag("oompSize", "T220")
newPart.addTag("oompColor", "BCE")
newPart.addTag("oompDesc", "A05")
newPart.addTag("oompIndex", "01")

newPart.addTag("hexID","TN120")
newPart.addTag("oompSort","TRNNT220A05")
newPart.addTag("ooPitch","2.54")
newPart.addTag("ooNumPins","3")
newPart.addTag("ooMaxCurrent","5 Amp")
newPart.addTag("ooPin1","B")
newPart.addTag("ooPin2","C")
newPart.addTag("ooPin3","E")

newPart.addTag("oompBbls","template;XXXX-T220-X-XXXX-01-bbls")
newPart.addTag("oompDiag","template;XXXX-T220-X-XXXX-01-diag")
newPart.addTag("oompIden","template;XXXX-T220-X-XXXX-01-iden")
newPart.addTag("oompSimp","template;XXXX-T220-X-XXXX-01-simp")

newPart.addTag("ooPackageMarking","TIP120")
newPart.addTag("ooDesignator","Q1")


###### KICAD DETAILS
newPart.addTag("kicadSymbol","Transistor_BLT>TIP120")
newPart.addTag("kicadFootprint","Package_TO_SOT_THT:TO-220-3_Vertical")

OOMP.parts.append(newPart)
