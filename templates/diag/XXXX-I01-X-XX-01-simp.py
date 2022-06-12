######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-I01-X-XX-01-simp")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;1")
newPart.addTag("drawItem","rectangle;0;0;2.54*%%pins%%;2.54;Main Square")
newPart.addTag("drawItem","oompURL;0;0;20;1;2;##hexID@@")

OOMP.parts.append(newPart)
