######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "CRHO-I01-X-08PI-01")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;1")
newPart.addTag("drawItem","rectangle;0;0;2.54*8;14;Main Square")
newPart.addTag("drawItem","rectangle;(2.54*4-2.54/2)-2.54*0;-2;1.2;5;pin 1")
newPart.addTag("drawItem","rectangle;(2.54*4-2.54/2)-2.54*1;-2;1.2;5;pin 1")
newPart.addTag("drawItem","rectangle;(2.54*4-2.54/2)-2.54*2;-2;1.2;5;pin 1")
newPart.addTag("drawItem","rectangle;(2.54*4-2.54/2)-2.54*3;-2;1.2;5;pin 1")
newPart.addTag("drawItem","rectangle;(2.54*4-2.54/2)-2.54*4;-2;1.2;5;pin 1")
newPart.addTag("drawItem","rectangle;(2.54*4-2.54/2)-2.54*5;-2;1.2;5;pin 1")
newPart.addTag("drawItem","rectangle;(2.54*4-2.54/2)-2.54*6;-2;1.2;5;pin 1")
newPart.addTag("drawItem","rectangle;(2.54*4-2.54/2)-2.54*7;-2;1.2;5;pin 1")

OOMP.parts.append(newPart)
