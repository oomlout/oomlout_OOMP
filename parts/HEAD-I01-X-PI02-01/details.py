import OOMP

newPart = OOMP.oompItem(8959)
newPart.addTag("oompType", "HEAD")
newPart.addTag("oompSize", "I01")
newPart.addTag("oompColor", "X")
newPart.addTag("oompDesc", "PI02")
newPart.addTag("oompIndex", "01")

newPart.addTag("hexID","H02")
newPart.addTag("oompClass","Through Hole")
newPart.addTag("oompClassCode","THTH")
newPart.addTag("ooPitch","2.54")
newPart.addTag("ooPinHeight","11.60")
newPart.addTag("ooPinWidth","0.64")
newPart.addTag("ooPinOffset","1.53")
newPart.addTag("ooNumPins","2")
newPart.addTag("oompBbls","variable;clear")
newPart.addTag("oompBbls","variable;pins;2")
newPart.addTag("oompBbls","template;XXXX-I01-X-XX-01-bbls")

newPart.addTag("oompDiag","variable;clear")
newPart.addTag("oompDiag","variable;pins;2")
newPart.addTag("oompDiag","template;HEAD-I01-X-XX-01-diag")

newPart.addTag("oompIden","variable;clear")
newPart.addTag("oompIden","variable;pins;2")
newPart.addTag("oompIden","template;XXXX-I01-X-XX-01-iden")

newPart.addTag("oompSchem","variable;clear")
newPart.addTag("oompSchem","variable;pins;2")
newPart.addTag("oompSchem","template;XXXX-XX-X-XX-01-PINS-EVEN-schem")

newPart.addTag("oompSimp","variable;clear")
newPart.addTag("oompSimp","variable;pins;2")
newPart.addTag("oompSimp","template;XXXX-I01-X-XX-01-simp")

newPart.addTag("ooDesignator","J1")


###### KICAD DETAILS
newPart.addTag("kicadSymbol","Connector>Conn_01x02_Male")
newPart.addTag("kicadFootprint","Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical")

OOMP.parts.append(newPart)
