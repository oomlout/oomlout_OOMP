import OOMP

newPart = OOMP.oompItem(8762)



newPart.addTag("index", "4128")


newPart.addTag("hexID", "BB4C")
newPart.addTag("oompSort", "P400")
newPart.addTag("oompType", "BREB")
newPart.addTag("oompSize", "P400")
newPart.addTag("oompColor", "C")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompVersion", "99")
newPart.addTag("ooWidth", "53 mm")
newPart.addTag("ooHeight", "8.5 mm")
newPart.addTag("ooLength", "82 mm")
newPart.addTag("ooMaxVoltage", "300 v")
newPart.addTag("usageList", "")
newPart.addTag("useItem", "")
newPart.addTag("useID", "1")
newPart.addTag("importance", "1")
newPart.addTag("useTitle", "Prototyping")
newPart.addTag("useDescription", "a base for prototyping new circuits.")
newPart.addTag("/useItem", "")
newPart.addTag("/usageList", "")
newPart.addTag("ooNameLine3of3", "Breadboard ")

sourceList = []
manufacturerDetails = []
manufacturerDetails.append(OOMP.oompTag("company", "Bud Industries"))
manufacturerDetails.append(OOMP.oompTag("companyCode", "C-BUDI"))
manufacturerDetails.append(OOMP.oompTag("name", ""))
manufacturerDetails.append(OOMP.oompTag("partID", "BB-32621"))
manufacturerDetails.append(OOMP.oompTag("link", ""))
manufacturerDetails.append(OOMP.oompTag("note", ""))
sourceList.append(OOMP.oompTag("manufacturer",manufacturerDetails))
newPart.addTag("sourceList", sourceList)

newPart.addTag("oompClass", "Wiring")
newPart.addTag("oompClassCode", "WIRE")

oompBbls = []
oompBbls.append(OOMP.oompTag("drawItem", "template;BREB-P400-C-STAN-01-bbls"))
newPart.addTag("oompBbls", oompBbls)






OOMP.parts.append(newPart)
