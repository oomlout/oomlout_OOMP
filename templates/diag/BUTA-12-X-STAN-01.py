######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "BUTA-12-X-STAN-01")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;0.5")
newPart.addTag("drawItem","rectangle;0;0;12.5;12.5;main bounding box")
newPart.addTag("drawItem","circle;0;0;8;8;button circle")
newPart.addTag("drawItem","rectangle;0;0;3;3;central square")


newPart.addTag("drawItem","rectangle;-6.75;2.5;1;1;pins")
newPart.addTag("drawItem","rectangle;6.75;2.5;1;1;pins")
newPart.addTag("drawItem","rectangle;6.75;-2.5;1;1;pins")
newPart.addTag("drawItem","rectangle;-6.75;-2.5;1;1;pins")


OOMP.parts.append(newPart)
