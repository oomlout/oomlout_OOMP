######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-SO323-X-XXXX-01")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;0.1")
newPart.addTag("drawItem","rectangle;0;0;2.2;1.35;Main Square")
newPart.addTag("drawItem","rectangle;-0.7;-0.887;0.4;0.425;pin 1")
newPart.addTag("drawItem","rectangle;0.7;-0.887;0.4;0.425;pin 2")
newPart.addTag("drawItem","rectangle;0;0.887;0.4;0.425;pin 2")

OOMP.parts.append(newPart)
