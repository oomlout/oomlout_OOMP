######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-XX-X-XX-01-PINS-simp")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","repeat;8;hLine;(2.54*%%pins%%/2-2.54/2)-2.54*(%%i%%+1);-2;1.2;5;pin %%i%%")

newPart.addTag("drawItem","linewidth;0")
newPart.addTag("drawItem","rectangle;0;5;10;10*%%pins%%+10;OutlineSquare")
newPart.addTag("drawItem","linewidth;1")
newPart.addTag("drawItem","rectangle;-1;0;6;10*%%pins%%-6;OutlineSquare")

newPart.addTag("drawItem","oompName;0;11;20;5;1.33;##name@@")
newPart.addTag("drawItem","oompURL;0;-8.5;0.75;##hexID@@")

OOMP.parts.append(newPart)
