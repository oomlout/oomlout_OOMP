import OOMP

newPart = OOMP.oompItem(8773)
newPart.addTag("oompType", "BUTA")
newPart.addTag("oompSize", "12")
newPart.addTag("oompColor", "X")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")


newPart.addTag("ooPin1",".")
newPart.addTag("ooPin2",".")
newPart.addTag("ooDesignator","S")

newPart.addTag("hexID","BT12")

newPart.addTag("manufacturer",["Diptronics","C-DIPT","","DTS-24R-V","",""])
newPart.addTag("bigDistributor",["Rapid Electronics","7.3mm Sq 12x12 Tactile Switch 260gf","78-0631","http://www.rapidonline.com/Electronic-Components/7-3mm-Sq-12x12-Tactile-Switch-260gf-78-0631",""])
newPart.addTag("bigDistributor",["Sparkfun","C-SPAR","Tactile Button Assortment","9190","https://www.sparkfun.com/products/10302",""])
newPart.addTag("bigDistributor",["Adafruit","C-ADAF","Colorful Round Tactile Button Switch Assortment - 15 pack","1009","http://www.adafruit.com/products/1009",""])

newPart.addTag("oompClassCode","THTH")
newPart.addTag("oompBbls","template;BUTA-12-X-STAN-01")
newPart.addTag("oompBbls","template;XXXX-XXXX-X-XXXX-XX-bbls-words")
newPart.addTag("oompDiag","template;BUTA-12-X-STAN-01")
newPart.addTag("oompDiag","template;XXXX-XXXX-X-XXXX-XX-diag-words")
newPart.addTag("oompIden","template;BUTA-12-X-STAN-01")
newPart.addTag("oompIden","template;XXXX-XXXX-X-XXXX-XX-iden-words")
newPart.addTag("oompSchem","template;BUTA-XXXX-X-XXXX-XX-schem")
newPart.addTag("oompSimp","template;BUTA-12-X-STAN-01")
newPart.addTag("oompSimp","template;XXXX-XXXX-X-XXXX-XX-simp-words")
newPart.addTag("oompSymbol","twoSidedPackage;##ooNumPins@@/2")			

###### KICAD DETAILS
newPart.addTag("kicadSymbol","Switch>SW_Push")
newPart.addTag("kicadFootprint","Button_Switch_THT:SW_PUSH-12mm")

OOMP.parts.append(newPart)
