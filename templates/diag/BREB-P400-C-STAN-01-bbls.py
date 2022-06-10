######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "BREB-P400-C-STAN-01-bbls")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","template;BREB-P400-C-STAN-01")

newPart.addTag("drawItem","oompName;0;48;40;10;##name@@")
newPart.addTag("drawItem","oompURL;0;-45;12;##hexID@@")

OOMP.parts.append(newPart)
