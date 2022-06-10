######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "BUTA-06-X-STAN-01")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;0.5")
newPart.addTag("drawItem","rectangle;0;0;6.2;6.2;main bounding box")
newPart.addTag("drawItem","circle;0;0;3;3;button circle")

newPart.addTag("drawItem","rectangle;-3.25;2.25;1;1;pins")
newPart.addTag("drawItem","rectangle;3.25;2.25;1;1;pins")
newPart.addTag("drawItem","rectangle;3.25;-2.25;1;1;pins")
newPart.addTag("drawItem","rectangle;-3.25;-2.25;1;1;pins")


OOMP.parts.append(newPart)
