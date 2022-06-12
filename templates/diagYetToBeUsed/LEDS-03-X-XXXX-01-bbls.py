######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "LEDS-03-X-XXXX-01-bbls")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;0.2")
newPart.addTag("drawItem","template;LEDS-03-X-XXXX-01")
newPart.addTag("drawItem","rectangle;-1.14;0;0.6;0.6;pin1")
newPart.addTag("drawItem","rectangle;1.14;0;0.6;0.6;pin2")
newPart.addTag("drawItem","textB;-0.64;0.75;2.5;A;pin 1")
newPart.addTag("drawItem","textB;0.64;0.75;2.5;K;pin 2")
newPart.addTag("drawItem","oompName;0;6;20;5;1.33;##name@@")
newPart.addTag("drawItem","oompURL;0;-4;0.75;##hexID@@")

OOMP.parts.append(newPart)
