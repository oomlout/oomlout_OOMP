######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "DISP-16X2-X-LCD-I2-bbls")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))



newPart.addTag("drawItem","corTemplate;DISP-16X2-X-LCD-I2")
newPart.addTag("drawItem","textB;-35;9.571;5;##ooPin1@@;pin 1")
newPart.addTag("drawItem","textB;-35;7.031;5;##ooPin2@@;pin 2")
newPart.addTag("drawItem","textB;-35;4.491;5;##ooPin3@@;pin 3")
newPart.addTag("drawItem","textB;-35;1.951;5;##ooPin4@@;pin 4")
newPart.addTag("drawItem","oompName;0;25;40;10;##name@@")
newPart.addTag("drawItem","oompURL;0;-22;12;##hexID@@")

OOMP.parts.append(newPart)
