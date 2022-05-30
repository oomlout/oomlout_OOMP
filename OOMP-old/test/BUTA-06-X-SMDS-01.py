import OOMP

newPart = OOMP.oompItem(8762)



newPart.addTag("index", "4315")


newPart.addTag("hexID", "B06")
newPart.addTag("oompSort", "0606")
newPart.addTag("oompType", "BUTA")
newPart.addTag("oompSize", "06")
newPart.addTag("oompColor", "X")
newPart.addTag("oompDesc", "SMDS")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompVersion", "99")
newPart.addTag("ooHeight", "3.5 mm")
newPart.addTag("ooLength", "6.2 mm")
newPart.addTag("usageList", "")
newPart.addTag("useItem", "")
newPart.addTag("useID", "1")
newPart.addTag("importance", "1")
newPart.addTag("useTitle", "Reset Button")
newPart.addTag("useDescription", "a reset button for a microcontroller.")
newPart.addTag("/useItem", "")
newPart.addTag("useItem", "")
newPart.addTag("useID", "2")
newPart.addTag("importance", "2")
newPart.addTag("useTitle", "Keypad Button")
newPart.addTag("useDescription", "a button on a keypad.")
newPart.addTag("/useItem", "")
newPart.addTag("/usageList", "")

sourceList = []
manufacturerDetails = []
manufacturerDetails.append(OOMP.oompTag("company", "Diptronics"))
manufacturerDetails.append(OOMP.oompTag("companyCode", "C-DIPT"))
manufacturerDetails.append(OOMP.oompTag("name", ""))
manufacturerDetails.append(OOMP.oompTag("partID", "DTSM-62K-S-V-T/R(SN431)"))
manufacturerDetails.append(OOMP.oompTag("link", ""))
manufacturerDetails.append(OOMP.oompTag("note", ""))
sourceList.append(OOMP.oompTag("manufacturer",manufacturerDetails))
newPart.addTag("sourceList", sourceList)


oplList = []
oplSystemDetails = []
oplSystemDetails.append(OOMP.oompTag("oplScheme", "Circuithub.com"))
oplSystemDetails.append(OOMP.oompTag("oplCode", "C-CIRC"))
oplSystemDetails.append(OOMP.oompTag("oplName", "OMRON/B3S-1000"))
oplSystemDetails.append(OOMP.oompTag("oplID", "OMRON/B3S-1000"))

oplSystemDetails.append(OOMP.oompTag("oplPackage", ""))
oplSystemDetails.append(OOMP.oompTag("oplLink", ""))
sourceList.append(OOMP.oompTag("oplSystem",oplSystemDetails))
newPart.addTag("oplList", oplList)

newPart.addTag("oompClass", "Surface Mount")
newPart.addTag("oompClassCode", "SMDS")

oompDiag = []
oompDiag.append(OOMP.oompTag("drawItem", "rectangle;0;0;6.2;6.2;Main Square"))
oompDiag.append(OOMP.oompTag("drawItem", "circle;0;0;3.5;3.5;Main Button"))
oompDiag.append(OOMP.oompTag("drawItem", "circle;2.15;2.15;0.75;0.75;Circle Nub 1"))
oompDiag.append(OOMP.oompTag("drawItem", "circle;-2.15;-2.15;0.75;0.75;Circle Nub 2"))
oompDiag.append(OOMP.oompTag("drawItem", "circle;2.15;-2.15;0.75;0.75;Circle Nub 3"))
oompDiag.append(OOMP.oompTag("drawItem", "circle;-2.15;2.15;0.75;0.75;Circle Nub 4"))
oompDiag.append(OOMP.oompTag("drawItem", "rectangle;3.8;2.25;1.4;0.7;pad 1"))
oompDiag.append(OOMP.oompTag("drawItem", "rectangle;-3.8;-2.25;1.4;0.7;pad 2"))
oompDiag.append(OOMP.oompTag("drawItem", "rectangle;-3.8;2.25;1.4;0.7;pad 3"))
oompDiag.append(OOMP.oompTag("drawItem", "rectangle;3.8;-2.25;1.4;0.7;pad 4"))
oompDiag.append(OOMP.oompTag("drawItem", "name;0;5;20;5;##name@@"))
oompDiag.append(OOMP.oompTag("drawItem", "oompURL;0;-5;2.835;##hexID@@"))
newPart.addTag("oompDiag", oompDiag)



oompSchem = []
oompSchem.append(OOMP.oompTag("drawItem", "template;BUTA-XXXX-X-XXXX-XX-schem"))
newPart.addTag("oompSchem", oompSchem)

newPart.addTag("ooDesignator", "S")
newPart.addTag("oompSymbol", "twoSidedPackage;##ooNumPins@@/2")

newPart.addTag("ooPin1", ".")
newPart.addTag("ooPin2", ".")





OOMP.parts.append(newPart)
