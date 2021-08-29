import OOMP

newPart = OOMP.oompItem(8762)




newPart.addTag("hexID", "BHS1220")
newPart.addTag("oompSort", "")
newPart.addTag("oompClass", "Surface Mount")
newPart.addTag("oompClassCode", "SMDS")
newPart.addTag("oompType", "BAHO")
newPart.addTag("oompSize", "CR1220")
newPart.addTag("oompColor", "X")
newPart.addTag("oompDesc", "SMDS")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompVersion", "40")
newPart.addTag("ooWidth", "15.06 mm")
newPart.addTag("ooHeight", "4.10 mm")
newPart.addTag("ooLength", "15 mm")
newPart.addTag("ooNumPins", "2")

sourceList = []
manufacturerDetails = []
manufacturerDetails.append(OOMP.oompTag("company", "Unknown"))
manufacturerDetails.append(OOMP.oompTag("companyCode", "C-UNKN"))
manufacturerDetails.append(OOMP.oompTag("name", ""))
manufacturerDetails.append(OOMP.oompTag("partID", "CR1220-2"))
manufacturerDetails.append(OOMP.oompTag("link", ""))
manufacturerDetails.append(OOMP.oompTag("note", ""))
sourceList.append(OOMP.oompTag("manufacturer",manufacturerDetails))
newPart.addTag("sourceList", sourceList)

newPart.addTag("oplSystem", "")
newPart.addTag("oplScheme", "SEEED OPL")
newPart.addTag("oplCode", "C-SEEE")
newPart.addTag("oplName", "SMD Battery Cell Holder Plastic;")
newPart.addTag("oplID", "320170000")
newPart.addTag("oplFootprint", "CR1220-15.06*13.00*H4.1mm")
newPart.addTag("oplPackage", "CR1220-15.06*13.00*H4.1mm")
newPart.addTag("oplLink", "")
newPart.addTag("/oplSystem", "")

newPart.addTag("oompAbout", "A surface mount battery holder for a CR1220 lithium ion button cell. Commonly used as a battery backup for on board clocks.")

oompSchem = []
oompSchem.append(OOMP.oompTag("drawItem", "template;BAHO-XXXX-X-XXXX-XX-schem"))
newPart.addTag("oompSchem", oompSchem)

newPart.addTag("ooDesignator", "BT1")





OOMP.parts.append(newPart)
