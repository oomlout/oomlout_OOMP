######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "RESA-XXXX-X-XXX4-XX-schem")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","corTemplate;RESA-XXXX-X-XXX4-XX-schem")
newPart.addTag("drawItem","oompName;0;40;20;6;##name@@")
newPart.addTag("drawItem","oompURL;0;-6;2.835;##hexID@@")

OOMP.parts.append(newPart)
