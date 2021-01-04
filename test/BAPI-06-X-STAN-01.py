import OOMP

newPart = OOMP.oompItem(8762)




newPart.addTag("hexID", "BAPI")
newPart.addTag("oompSort", "BAPI06THTH")
newPart.addTag("oompType", "BAPI")
newPart.addTag("oompSize", "06")
newPart.addTag("oompColor", "X")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompVersion", "98")

sourceList = []
manufacturerDetails = []
manufacturerDetails.append(OOMP.oompTag("company", "JJWJ"))
manufacturerDetails.append(OOMP.oompTag("companyCode", "C-JJWJ"))
manufacturerDetails.append(OOMP.oompTag("name", ""))
manufacturerDetails.append(OOMP.oompTag("partID", "0"))
manufacturerDetails.append(OOMP.oompTag("link", ""))
manufacturerDetails.append(OOMP.oompTag("note", ""))
sourceList.append(OOMP.oompTag("manufacturer",manufacturerDetails))
newPart.addTag("sourceList", sourceList)


oplList = []
oplSystemDetails = []
oplSystemDetails.append(OOMP.oompTag("oplScheme", "SEEED OPL"))
oplSystemDetails.append(OOMP.oompTag("oplCode", "C-SEEE"))
oplSystemDetails.append(OOMP.oompTag("oplName", "Folding Clasps"))
oplSystemDetails.append(OOMP.oompTag("oplID", "323050000"))

oplSystemDetails.append(OOMP.oompTag("oplPackage", ""))
oplSystemDetails.append(OOMP.oompTag("oplLink", ""))
sourceList.append(OOMP.oompTag("oplSystem",oplSystemDetails))
newPart.addTag("oplList", oplList)






OOMP.parts.append(newPart)
