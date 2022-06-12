######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-0805-X-XXXX-XX-simp")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","template;XXXX-0805-X-XXXX-XX-generic")
newPart.addTag("drawItem","text;0;0.16;0.75;oom.lt/")
newPart.addTag("drawItem","textb;0;-0.16;0.75;##hexID@@")

OOMP.parts.append(newPart)
