######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-SO23F-X-XXXX-01-simp")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","template;XXXX-SO23F-X-XXXX-01")
newPart.addTag("drawItem","text;0;0.25;1;oom.lt/;pin 1")
newPart.addTag("drawItem","textB;0;-0.25;1;##hexID@@;pin 1")

OOMP.parts.append(newPart)
