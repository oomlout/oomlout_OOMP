######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "XXXX-SO23-X-XXXX-01-diag")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","template;XXXX-SO23-X-XXXX-01")
newPart.addTag("drawItem","textB;-0.95;-0.3;1;##ooPin1@@;pin 1")
newPart.addTag("drawItem","textB;0.95;-0.3;1;##ooPin2@@;pin 2")
newPart.addTag("drawItem","textB;0;0.3;1;##ooPin3@@;pin 3")
newPart.addTag("drawItem","oompName;0;5;20;5;1.33;##name@@")
newPart.addTag("drawItem","oompURL;0;-3.5;0.75;##hexID@@")

OOMP.parts.append(newPart)
