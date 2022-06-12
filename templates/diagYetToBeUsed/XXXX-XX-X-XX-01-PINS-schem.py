######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-XX-X-XX-01-PINS-schem")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;0")
newPart.addTag("drawItem","rectangle;0;10;20;10*%%pins%% + 20;OutlineSquare")
newPart.addTag("drawItem","linewidth;1")
newPart.addTag("drawItem","rectangle;-1.5;10;13;10*%%pins%%;Square")
newPart.addTag("drawItem","repeat;%%pins%%;hLine;7.5;(%%pins%%*10/2)-(%%i%%-1)*10;5;0;pin %%i%%")
newPart.addTag("drawItem","repeat;%%pins%%;textb;2;(%%pins%%*10/2)-(%%i%%-1)*10;3.5;PIN %%i%%")
newPart.addTag("drawItem","oompURL;0;-(%%pins%%*10/2)+3.5;0.75;##hexID@@")
newPart.addTag("drawItem","oompName;0;(%%pins%%*10/2)+10;20;5;1.33;##name@@")


OOMP.parts.append(newPart)
