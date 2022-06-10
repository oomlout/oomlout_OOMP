######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "ICIC-SP20-X-XXXX-01-bbls")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","template;ICIC-SP20-X-XXXX-01")
newPart.addTag("drawItem","textBR;0;0;6;##ooPackageMarking@@;pin 1")
newPart.addTag("drawItem","oompName;0;10;20;5;##name@@")
newPart.addTag("drawItem","oompURL;0;-7.5;2.835;##hexID@@")

OOMP.parts.append(newPart)
