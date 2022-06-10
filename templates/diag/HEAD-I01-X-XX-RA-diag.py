######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "HEAD-I01-X-XX-RA-diag")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;0.2")
newPart.addTag("drawItem","rectangle;0;1.5;2.54*%%pins%%;2.54;Main Square")
newPart.addTag("drawItem","repeat;%%pins%%;rectangle;(2.54*%%pins%%/2-2.54/2)-2.54*(%%i%%-1);1.5;0.64;0.64;pin %%i%%")
newPart.addTag("drawItem","repeat;%%pins%%;rectangle;(2.54*%%pins%%/2-2.54/2)-2.54*(%%i%%-1);-1.27;0.64;3;pin %%i%%")
newPart.addTag("drawItem","linewidth;1")
newPart.addTag("drawItem","oompName;0;6;20;5;##name@@")
newPart.addTag("drawItem","oompURL;0;-3.5;2.835;##hexID@@")

OOMP.parts.append(newPart)
