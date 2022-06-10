######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "BUTA-XXXX-X-02PI-XX-schem")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","corTemplate;BUTA-XXXX-X-02PI-XX-schem")
newPart.addTag("drawItem","oompName;0;13;20;6;##name@@")
newPart.addTag("drawItem","oompURL;0;-8;2.835;##hexID@@")

OOMP.parts.append(newPart)
