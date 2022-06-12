######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "LEDS-10-X-XXXX-01-bbls")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;0.2")
newPart.addTag("drawItem","template;LEDS-10-X-XXXX-01")
newPart.addTag("drawItem","rectangle;-1.27;0;0.6;0.6;pin1")
newPart.addTag("drawItem","rectangle;1.27;0;0.6;0.6;pin2")
newPart.addTag("drawItem","textB;-1.27;1;2.5;A;pin 1")
newPart.addTag("drawItem","textB;1.27;1;2.5;K;pin 2")
newPart.addTag("drawItem","oompName;0;8.5;23;5;1.33;##name@@")
newPart.addTag("drawItem","oompURL;0;-7;0.75;##hexID@@")

OOMP.parts.append(newPart)
