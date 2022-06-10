######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "BUZZ-XXXX-X-XXXX-XX-schem")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","corTemplate;BUZZ-XXXX-X-XXXX-XX-schem")
newPart.addTag("drawItem","oompName;0;7.5;20;5;##name@@")
newPart.addTag("drawItem","oompURL;0;-5;2.835;##hexID@@")

OOMP.parts.append(newPart)
