######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-T220-X-XXXX-01-bbls")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;0.2")
newPart.addTag("drawItem","rectangle;0;0;10.16;4.35;Main Square")
newPart.addTag("drawItem","rectangle;-2.54;-0.675;0.6;0.6;pin1")
newPart.addTag("drawItem","rectangle;0;-0.675;0.6;0.6;pin2")
newPart.addTag("drawItem","rectangle;2.54;-0.675;0.6;0.6;pin3")
newPart.addTag("drawItem","hLine;0;0.925;10.16;1;top line")
newPart.addTag("drawItem","textB;-3.54;-0.675;5;##ooPin1@@;pin 1")
newPart.addTag("drawItem","textB;-1;-0.675;5;##ooPin2@@;pin 1")
newPart.addTag("drawItem","textB;1.54;-0.675;5;##ooPin3@@;pin 1")
newPart.addTag("drawItem","oompName;0;5;20;5;##name@@")
newPart.addTag("drawItem","oompURL;0;-3.5;2.835;##hexID@@")

OOMP.parts.append(newPart)
