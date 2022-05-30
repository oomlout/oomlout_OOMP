import OOMP

newPart = OOMP.oompItem(8762)




newPart.addTag("hexID", "AN2440")
newPart.addTag("oompSort", "ANTEG2440")
newPart.addTag("oompType", "ANTE")
newPart.addTag("oompSize", "40")
newPart.addTag("oompColor", "X")
newPart.addTag("oompDesc", "G24")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompVersion", "98")

sourceList = []
manufacturerDetails = []
manufacturerDetails.append(OOMP.oompTag("company", "FEIYUXIN"))
manufacturerDetails.append(OOMP.oompTag("companyCode", "C-FEIY"))
manufacturerDetails.append(OOMP.oompTag("name", ""))
manufacturerDetails.append(OOMP.oompTag("partID", "3020-1766"))
manufacturerDetails.append(OOMP.oompTag("link", ""))
manufacturerDetails.append(OOMP.oompTag("note", ""))
sourceList.append(OOMP.oompTag("manufacturer",manufacturerDetails))
newPart.addTag("sourceList", sourceList)

newPart.addTag("oplSystem", "")
newPart.addTag("oplScheme", "SEEED OPL")
newPart.addTag("oplCode", "C-SEEE")
newPart.addTag("oplName", "PCB External 2.4 Antenna;With I-PEX Cable")
newPart.addTag("oplID", "318020019")

newPart.addTag("oplPackage", "")
newPart.addTag("oplLink", "")
newPart.addTag("/oplSystem", "")


oompSchem = []
oompSchem.append(OOMP.oompTag("drawItem", "template;ANTE-XXXX-X-XXXX-XX-schem"))
newPart.addTag("oompSchem", oompSchem)

newPart.addTag("ooDesignator", "AE1")





OOMP.parts.append(newPart)
