######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-1206-X-XXXX-XX-generic")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","rectangle;0;0;3.048;1.524;Main Square")
newPart.addTag("drawItem","rectangle;0;0;2.1;1.524;Main Square")

OOMP.parts.append(newPart)
