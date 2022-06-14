######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "ICIC-QFN28-X-XXXX-01-iden")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","template;ICIC-QFN28-X-XXXX-01")
newPart.addTag("drawItem","textB;0;0;2.5;##ooDesignator@@;pin 1")

OOMP.parts.append(newPart)