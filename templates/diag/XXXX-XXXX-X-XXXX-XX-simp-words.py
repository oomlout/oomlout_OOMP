######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-XXXX-X-XXXX-XX-simp-words")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","text;0,1.25;4;oom.lt/")
newPart.addTag("drawItem","text;0,-1.25;4;##hexID@@")
newPart.addTag("drawItem","oompName;0;10.5;20;7;##name@@")
newPart.addTag("drawItem","oompURL;0;-7.5;2.835;##hexID@@")

OOMP.parts.append(newPart)
