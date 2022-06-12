######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-XX-X-XX-01-PINS-EVEN-schem")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


#newPart.addTag("drawItem","linewidth;0")
#newPart.addTag("drawItem","rectangle;0;10;20;10*%%pins%% + 20;OutlineSquare")
newPart.addTag("drawItem","linewidth;1")
newPart.addTag("drawItem","rectangle;0;5;13;10*%%pins%%;Square")
newPart.addTag("drawItem","repeat;%%pins%%;hLine;7.5;(%%pins%%*10/2)-(%%i%%-1)*10;5;0;pin %%i%%")
newPart.addTag("drawItem","repeat;%%pins%%;textB;2;(%%pins%%*10/2)-(%%i%%-1)*10;3.5;PIN %%i%%")
newPart.addTag("drawItem","oompURL;0;-(%%pins%%*10/2)+2;20;3.5;3;##hexID@@")
newPart.addTag("drawItem","oompName;0;(%%pins%%*10/2)+8;20;5;5;##name@@")


OOMP.parts.append(newPart)
