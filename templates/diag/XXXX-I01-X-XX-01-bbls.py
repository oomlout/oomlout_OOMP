import OOMP

indexA = 8998
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-I01-X-XX-01-bbls")

newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;0.75")
newPart.addTag("drawItem","pinHolder;0;0;2.54*%%pins%%;2.54;Main Square")
newPart.addTag("drawItem","linewidth;0.75")
newPart.addTag("drawItem","repeat;%%pins%%;pin;(2.54*%%pins%%/2-2.54/2)-2.54*(%%i%%-1);0;0.64;0.64;pin %%i%%")
newPart.addTag("drawItem","oompName;0;4;20;5;5;##name@@")
newPart.addTag("drawItem","oompURL;0;-6;20;5;3;##hexID@@")


OOMP.parts.append(newPart)
