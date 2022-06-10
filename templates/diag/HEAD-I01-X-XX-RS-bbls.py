######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "HEAD-I01-X-XX-RS-bbls")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;0.2")
newPart.addTag("drawItem","linewidth;0.2")
newPart.addTag("drawItem","repeat;%%pins%%;rectangle;(2.54*%%pins%%/2-2.54/2)-2.54*(%%i%%-1);-4.525;0.64;2.03;pin %%i%%")
newPart.addTag("drawItem","repeat;%%pins%%;rectangle;(2.54*%%pins%%/2-2.54/2)-2.54*(%%i%%-1);-3.255;0.64;0.51;pin %%i%%")
newPart.addTag("drawItem","repeat;%%pins%%;rectangle;(2.54*%%pins%%/2-2.54/2)-2.54*(%%i%%-1);2.54;0.64;6;pin %%i%%")
newPart.addTag("drawItem","rectangle;0;-1.73;2.54*%%pins%%;2.54;Main Square")
newPart.addTag("drawItem","oompName;0;9.75;20;5;##name@@")
newPart.addTag("drawItem","oompURL;0;-6.75;2.835;##hexID@@")

OOMP.parts.append(newPart)
