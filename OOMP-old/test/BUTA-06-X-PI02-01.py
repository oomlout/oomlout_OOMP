import OOMP

newPart = OOMP.oompItem(8762)





newPart.addTag("hexID", "BT62")
newPart.addTag("oompSort", "")
newPart.addTag("oompClass", "Through Hole")
newPart.addTag("oompClassCode", "THTH")
newPart.addTag("oompSize", "06")
newPart.addTag("oompColor", "X")
newPart.addTag("oompDesc", "PI02")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompVersion", "40")
newPart.addTag("ooWidth", "6 mm")
newPart.addTag("ooHeight", "3.5 mm")
newPart.addTag("ooDepth", "3.5 mm")
newPart.addTag("ooNumPins", "2")
newPart.addTag("ooLifetime", "50 000 cycles")

sourceList = []
manufacturerDetails = []
manufacturerDetails.append(OOMP.oompTag("company", "Shenzhen Best"))
manufacturerDetails.append(OOMP.oompTag("companyCode", "C-BEST"))
manufacturerDetails.append(OOMP.oompTag("name", ""))
manufacturerDetails.append(OOMP.oompTag("partID", "TS-1101F"))
manufacturerDetails.append(OOMP.oompTag("link", ""))
manufacturerDetails.append(OOMP.oompTag("note", ""))
sourceList.append(OOMP.oompTag("manufacturer",manufacturerDetails))
newPart.addTag("sourceList", sourceList)


oplList = []
oplSystemDetails = []
oplSystemDetails.append(OOMP.oompTag("oplScheme", "SEEED OPL"))
oplSystemDetails.append(OOMP.oompTag("oplCode", "C-SEEE"))
oplSystemDetails.append(OOMP.oompTag("oplName", "DIP Button Front -white;"))
oplSystemDetails.append(OOMP.oompTag("oplID", "311020025"))
oplSystemDetails.append(OOMP.oompTag("oplFootprint", "2P-L6.0*W3.0*H4.3mm-90D"))
oplSystemDetails.append(OOMP.oompTag("oplPackage", "2P-L6.0*W3.0*H4.3mm-90D"))
oplSystemDetails.append(OOMP.oompTag("oplLink", ""))
sourceList.append(OOMP.oompTag("oplSystem",oplSystemDetails))
newPart.addTag("oplList", oplList)

newPart.addTag("oompAbout", "A simple tactile pushbutton with two pins. This button is not commonly used. However it is imcluded in OOMP due to it being a part in the SEEED OPL. For a more commonly used through hole button we recommend (BUTA-06-X-STAN-01)")

oompSchem = []
oompSchem.append(OOMP.oompTag("drawItem", "template;BUTA-XXXX-X-PI02-XX-schem"))
newPart.addTag("oompSchem", oompSchem)

newPart.addTag("ooDesignator", "S")
newPart.addTag("oompSymbol", "twoSidedPackage;##ooNumPins@@/2")

newPart.addTag("ooPin1", ".")
newPart.addTag("ooPin2", ".")





OOMP.parts.append(newPart)
