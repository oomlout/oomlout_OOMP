import OOMP

newPart = OOMP.oompItem(8762)




newPart.addTag("hexID", "BHS1220M")
newPart.addTag("oompSort", "BAHOCR1220SMDS")
newPart.addTag("oompType", "BAHO")
newPart.addTag("oompSize", "CR1220")
newPart.addTag("oompColor", "M")
newPart.addTag("oompDesc", "SMDS")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompVersion", "98")
newPart.addTag("oplSystem", "")
newPart.addTag("oplScheme", "SEEED OPL")
newPart.addTag("oplCode", "C-SEEE")
newPart.addTag("oplName", "DIP CR1220 Cell Battery Holder")
newPart.addTag("oplID", "320170002")

newPart.addTag("oplPackage", "")
newPart.addTag("oplLink", "")
newPart.addTag("/oplSystem", "")


oompSchem = []
oompSchem.append(OOMP.oompTag("drawItem", "template;BAHO-XXXX-X-XXXX-XX-schem"))
newPart.addTag("oompSchem", oompSchem)

newPart.addTag("ooDesignator", "BT1")





OOMP.parts.append(newPart)
