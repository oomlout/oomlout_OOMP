import OOMP

newPart = OOMP.oompItem(9147)
newPart.addTag("oompType", "LEDS")
newPart.addTag("oompSize", "10")
newPart.addTag("oompColor", "R")
newPart.addTag("oompDesc", "FROS")
newPart.addTag("oompIndex", "01")

newPart.addTag("hexID","L10R")
newPart.addTag("oompSort","1010R")

newPart.addTag("ooPitch","2.54 mm")
newPart.addTag("ooLensColor","Frosted")
newPart.addTag("ooForwardVoltage",">2.0 V")
newPart.addTag("ooForwardCurrent","15 mA")
newPart.addTag("ooIntensity","1,000 mcd")
newPart.addTag("ooPowerAngle","50 deg")
newPart.addTag("ooWavelength","623 nm")
newPart.addTag("ooDesignator","D1")


newPart.addTag("oompClass","Through Hole Component")
newPart.addTag("oompClassCode","THTH")

newPart.addTag("oompBbls","template;LEDS-10-X-XXXX-01-bbls")
newPart.addTag("oompDiag","template;LEDS-10-X-XXXX-01-diag")
newPart.addTag("oompIden","template;LEDS-10-X-XXXX-01-iden")
newPart.addTag("oompSchem","template;LEDS-XXXX-X-XXXX-XX-schem")
newPart.addTag("oompSimp","template;LEDS-10-X-XXXX-01-simp")


###### KICAD DETAILS
newPart.addTag("kicadSymbol","Device>LED")
newPart.addTag("kicadFootprint","LED_THT>LED_D10.0mm")

OOMP.parts.append(newPart)
