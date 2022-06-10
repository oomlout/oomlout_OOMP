######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "LEDS-10-X-XXXX-01-simp")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;0.2")
newPart.addTag("drawItem","template;LEDS-10-X-XXXX-01")
newPart.addTag("drawItem","text;0;1;5;oom.lt/;pin 1")
newPart.addTag("drawItem","textB;0;-1;5;##hexID@@;pin 1")


OOMP.parts.append(newPart)
