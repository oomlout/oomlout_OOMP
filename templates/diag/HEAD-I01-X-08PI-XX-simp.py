######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "HEAD-I01-X-08PI-XX-simp")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","template;HEAD-I01-X-08PI-XX")
newPart.addTag("drawItem","text;0,0.355;2;oom.lt/")
newPart.addTag("drawItem","textB;0,-0.355;2;##hexID@@")

OOMP.parts.append(newPart)
