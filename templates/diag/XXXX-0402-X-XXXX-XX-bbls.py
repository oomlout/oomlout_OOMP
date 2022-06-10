######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-0402-X-XXXX-XX-bbls")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","template;XXXX-0402-X-XXXX-XX-generic")
newPart.addTag("drawItem","template;XXXX-XXXX-X-XXXX-XX-bbls-wordsSMD")

OOMP.parts.append(newPart)
