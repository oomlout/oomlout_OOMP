######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-T220-X-XXXX-01-iden")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;0.2")
newPart.addTag("drawItem","rectangle;0;0;10.16;4.35;Main Square")
newPart.addTag("drawItem","hLine;0;0.925;10.16;1;top line")
newPart.addTag("drawItem","textB;0;-0.75;6;##ooDesignator@@;pin 1")



OOMP.parts.append(newPart)
