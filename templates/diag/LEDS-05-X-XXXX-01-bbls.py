######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "LEDS-05-X-XXXX-01-bbls")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;0.2")
newPart.addTag("drawItem","template;LEDS-05-X-XXXX-01")
newPart.addTag("drawItem","rectangle;-1.27;0;0.6;0.6;pin1")
newPart.addTag("drawItem","rectangle;1.27;0;0.6;0.6;pin2")
newPart.addTag("drawItem","textB;-1.27;1;2.5;A;pin 1")
newPart.addTag("drawItem","textB;1.27;1;2.5;K;pin 2")
newPart.addTag("drawItem","oompName;0;6;20;5;##name@@")
newPart.addTag("drawItem","oompURL;0;-4;2.835;##hexID@@")

OOMP.parts.append(newPart)
