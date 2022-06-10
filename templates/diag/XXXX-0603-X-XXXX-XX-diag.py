######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-0603-X-XXXX-XX-diag")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","template;XXXX-0603-X-XXXX-XX-generic")
newPart.addTag("drawItem","textb;0;0;1;##ooPackageMarking@@")

OOMP.parts.append(newPart)
