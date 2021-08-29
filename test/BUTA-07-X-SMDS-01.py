import OOMP

newPart = OOMP.oompItem(8762)



newPart.addTag("index", "4296")


newPart.addTag("hexID", "B7S")
newPart.addTag("oompSort", "0707")
newPart.addTag("oompType", "BUTA")
newPart.addTag("oompSize", "07")
newPart.addTag("oompColor", "X")
newPart.addTag("oompDesc", "SMDS")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompVersion", "99")
newPart.addTag("ooHeight", "3.55 mm")
newPart.addTag("ooLength", "7 mm")
newPart.addTag("ooManufacturer", "C-BEST")
newPart.addTag("ooManufacturerPartNumber", "Shenzhen Best Electronics")
newPart.addTag("useItem", "")
newPart.addTag("useID", "1")
newPart.addTag("importance", "1")
newPart.addTag("useTitle", "Reset Button")
newPart.addTag("useDescription", "a reset button for a microcontroller.")
newPart.addTag("/useItem", "")
newPart.addTag("ooSEEEDsku", "3100060P1")
newPart.addTag("ooSEEEDdesc", "SMD Button	")
newPart.addTag("manufacturer", "")
newPart.addTag("company", "Shenzhen Best")
newPart.addTag("companyCode", "C-BEST")

newPart.addTag("partID", "TS-1188E")
newPart.addTag("link", "")
newPart.addTag("note", "")
newPart.addTag("/manufacturer", "")
newPart.addTag("company", "")
newPart.addTag("companyCode", "")

newPart.addTag("partID", "")
newPart.addTag("link", "")
newPart.addTag("note", "")
newPart.addTag("/bigDistributor", "")


oplList = []
oplSystemDetails = []
oplSystemDetails.append(OOMP.oompTag("oplScheme", "SEED OPL"))
oplSystemDetails.append(OOMP.oompTag("oplCode", "C-SEEE"))
oplSystemDetails.append(OOMP.oompTag("oplName", "SMD Button"))
oplSystemDetails.append(OOMP.oompTag("oplID", "311020023"))

oplSystemDetails.append(OOMP.oompTag("oplPackage", "4P-SMD-7.0X3.5X3.5H-90D"))
oplSystemDetails.append(OOMP.oompTag("oplLink", ""))
sourceList.append(OOMP.oompTag("oplSystem",oplSystemDetails))
newPart.addTag("oplList", oplList)

newPart.addTag("ooSEEED3dModel", "http://www.seeedstudio.com/wiki/File:4P-SMD-7.0X3.5X3.5H-90D.zip")
newPart.addTag("oompClassCode", "SMDS")

oompSchem = []
oompSchem.append(OOMP.oompTag("drawItem", "template;BUTA-XXXX-X-02PI-XX-schem"))
newPart.addTag("oompSchem", oompSchem)

newPart.addTag("ooDesignator", "S")
newPart.addTag("oompSymbol", "twoSidedPackage;##ooNumPins@@/2")

newPart.addTag("ooPin1", ".")
newPart.addTag("ooPin2", ".")





OOMP.parts.append(newPart)
