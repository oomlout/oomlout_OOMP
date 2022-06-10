######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-T220-X-XXXX-01-diag")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;0.2")
newPart.addTag("drawItem","template;XXXX-T220-X-XXXX-01")
newPart.addTag("drawItem","textB;-2.54;1;4;##ooPin1@@;pin 1")
newPart.addTag("drawItem","textB;0;1;4;##ooPin2@@;pin 2")
newPart.addTag("drawItem","textB;2.54;1;4;##ooPin3@@;pin 3")
newPart.addTag("drawItem","textB;0;6;6;##ooPackageMarking@@;id")

newPart.addTag("drawItem","oompName;0;18;20;5;##name@@")
newPart.addTag("drawItem","oompURL;0;-17.5;2.835;##hexID@@")

OOMP.parts.append(newPart)
