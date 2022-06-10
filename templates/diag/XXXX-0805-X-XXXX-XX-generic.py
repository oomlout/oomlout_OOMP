######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-0805-X-XXXX-XX-generic")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","rectangle;0;0;2.032;1.27;Main Square")
newPart.addTag("drawItem","rectangle;0;0;1.4;1.27;Main Square")

OOMP.parts.append(newPart)
