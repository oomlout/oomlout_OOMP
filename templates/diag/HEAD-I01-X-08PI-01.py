######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "HEAD-I01-X-08PI-01")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;1")
newPart.addTag("drawItem","rectangle;0;0;2.54*8;2.54;Main Square")
newPart.addTag("drawItem","rectangle;2.54*4-2.54/2;0;0.64;0.64;pin 28")
newPart.addTag("drawItem","rectangle;(2.54*4-2.54/2)-2.54*1;0;0.64;0.64;pin 28")
newPart.addTag("drawItem","rectangle;(2.54*4-2.54/2)-2.54*2;0;0.64;0.64;pin 28")
newPart.addTag("drawItem","rectangle;(2.54*4-2.54/2)-2.54*3;0;0.64;0.64;pin 28")
newPart.addTag("drawItem","rectangle;(2.54*4-2.54/2)-2.54*4;0;0.64;0.64;pin 28")
newPart.addTag("drawItem","rectangle;(2.54*4-2.54/2)-2.54*5;0;0.64;0.64;pin 28")
newPart.addTag("drawItem","rectangle;(2.54*4-2.54/2)-2.54*6;0;0.64;0.64;pin 28")
newPart.addTag("drawItem","rectangle;(2.54*4-2.54/2)-2.54*7;0;0.64;0.64;pin 28")

OOMP.parts.append(newPart)
