######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "ANTE-XXXX-X-XXXX-XX-schem")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","corTemplate;ANTE-XXXX-X-XXXX-XX-schem")
newPart.addTag("drawItem","oompName;0;6.5;20;7;##name@@")
newPart.addTag("drawItem","oompURL;0;-5;0.75;##hexID@@")

OOMP.parts.append(newPart)
