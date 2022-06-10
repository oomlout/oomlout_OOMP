######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "HEAD-I01-X-08PI-XX-bbls")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","template;HEAD-I01-X-08PI-XX")
newPart.addTag("drawItem","oompName;0;6;20;7;##name@@")
newPart.addTag("drawItem","oompURL;0;-3;2.835;##hexID@@")

OOMP.parts.append(newPart)
