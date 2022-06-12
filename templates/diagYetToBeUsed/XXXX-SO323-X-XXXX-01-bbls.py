######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-SO323-X-XXXX-01-bbls")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","template;XXXX-SO323-X-XXXX-01")
newPart.addTag("drawItem","textB;0;0;2.5;##ooPackageMarking@@;pin 1")
newPart.addTag("drawItem","oompName;0;5;20;5;1.33;##name@@")
newPart.addTag("drawItem","oompURL;0;-3.5;0.75;##hexID@@")

OOMP.parts.append(newPart)
