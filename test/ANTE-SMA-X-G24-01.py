import OOMP

newPart = OOMP.oompItem(8762)




newPart.addTag("hexID", "AN24SM")
newPart.addTag("oompSort", "ANTESMAM4X4")
newPart.addTag("oompType", "ANTE")
newPart.addTag("oompSize", "SMA")
newPart.addTag("oompColor", "X")
newPart.addTag("oompDesc", "G24")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompVersion", "98")

sourceList = []
manufacturerDetails = []
manufacturerDetails.append(OOMP.oompTag("company", "DYRH"))
manufacturerDetails.append(OOMP.oompTag("companyCode", "C-DYRH"))
manufacturerDetails.append(OOMP.oompTag("name", ""))
manufacturerDetails.append(OOMP.oompTag("partID", "RH0111-30002"))
manufacturerDetails.append(OOMP.oompTag("link", ""))
manufacturerDetails.append(OOMP.oompTag("note", ""))
sourceList.append(OOMP.oompTag("manufacturer",manufacturerDetails))
newPart.addTag("sourceList", sourceList)

newPart.addTag("oplSystem", "")
newPart.addTag("oplScheme", "SEEED OPL")
newPart.addTag("oplCode", "C-SEEE")
newPart.addTag("oplName", "SMA External 2.4G Antenna")
newPart.addTag("oplID", "318020010")

newPart.addTag("oplPackage", "")
newPart.addTag("oplLink", "")
newPart.addTag("/oplSystem", "")


oompSchem = []
oompSchem.append(OOMP.oompTag("drawItem", "template;ANTE-XXXX-X-XXXX-XX-schem"))
newPart.addTag("oompSchem", oompSchem)

newPart.addTag("ooDesignator", "AE1")





OOMP.parts.append(newPart)
