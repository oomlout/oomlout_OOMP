import OOMP

newPart = OOMP.oompItem(8771)
newPart.addTag("oompType", "BUTA")
newPart.addTag("oompSize", "06")
newPart.addTag("oompColor", "X")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")

newPart.addTag("hexID","BT6")
newPart.addTag("oompSort","0606")
newPart.addTag("ooWidth","6.2 mm")
newPart.addTag("ooHeight","3.5 mm")
newPart.addTag("ooLength","6.2 mm")
newPart.addTag("oompAbout","The most commonly used through hole tactile pushbutton. It's often more difficult to find a PCB without one of these than with.")
newPart.addTag("oompClass","Through Hole Component")
newPart.addTag("oompClassCode","THTH")
newPart.addTag("oompBbls","template;BUTA-06-X-STAN-01")
newPart.addTag("oompBbls","template;XXXX-XXXX-X-XXXX-XX-bbls-words")
newPart.addTag("oompDiag","template;BUTA-06-X-STAN-01")
newPart.addTag("oompIden","template;BUTA-06-X-STAN-01")			
newPart.addTag("oompSchem","template;BUTA-XXXX-X-XXXX-XX-schem")

newPart.addTag("ooDesignator","S")
newPart.addTag("oompSymbol","twoSidedPackage;##ooNumPins@@/2")
newPart.addTag("ooPin1",".")
newPart.addTag("ooPin2",".")

###### KICAD DETAILS
newPart.addTag("kicadSymbol","Switch>SW_Push")
newPart.addTag("kicadFootprint","Button_Switch_THT:SW_PUSH_6mm")

OOMP.parts.append(newPart)
