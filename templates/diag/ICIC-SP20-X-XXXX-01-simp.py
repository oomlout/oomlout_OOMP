######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "ICIC-SP20-X-XXXX-01-simp")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","template;ICIC-SP20-X-XXXX-01")
newPart.addTag("drawItem","textR;-1.75;0;2;oom.lt/;pin 1")
newPart.addTag("drawItem","textBR;1.75;0;2;##hexID@@;pin 1")

OOMP.parts.append(newPart)
