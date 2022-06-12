######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-SO23F-X-XXXX-01")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;0.1")
newPart.addTag("drawItem","rectangle;0;0;2.9;1.8;Main Square")
newPart.addTag("drawItem","rectangle;-0.95;-1.05;0.4;0.3;pin 1")
newPart.addTag("drawItem","rectangle;0.95;-1.05;0.4;0.3;pin 2")
newPart.addTag("drawItem","rectangle;0;1.05;0.4;0.3;pin 2")

OOMP.parts.append(newPart)
