######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-I01-X-XX-RA-bbls")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;0.2")
newPart.addTag("drawItem","rectangle;0;-3;2.54*%%pins%%;2.54;Main Square")
newPart.addTag("drawItem","linewidth;0.2")
newPart.addTag("drawItem","repeat;%%pins%%;rectangle;(2.54*%%pins%%/2-2.54/2)-2.54*(%%i%%-1);-3;0.64;0.64;pin %%i%%")
newPart.addTag("drawItem","repeat;%%pins%%;rectangle;(2.54*%%pins%%/2-2.54/2)-2.54*(%%i%%-1);0.795;0.64;6.95;pin %%i%%")
newPart.addTag("drawItem","oompName;0;7;20;5;##name@@")
newPart.addTag("drawItem","oompURL;0;-5.5;2.835;##hexID@@")

OOMP.parts.append(newPart)
