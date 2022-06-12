######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-XXXX-X-XXXX-XX-bbls-wordsSMD")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","oompName;0;6.5;20;6;##name@@")
newPart.addTag("drawItem","oompURL;0;-3.5;0.75;##hexID@@")

OOMP.parts.append(newPart)
