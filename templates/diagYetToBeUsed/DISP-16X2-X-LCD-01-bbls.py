######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "DISP-16X2-X-LCD-01-bbls")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","corTemplate;DISP-16X2-X-LCD-01")
newPart.addTag("drawItem","textB;-32.87;14.375;3.75;##ooPin1@@;pin 1")
newPart.addTag("drawItem","textB;-30.33;13.25;3.75;##ooPin2@@;pin 1")
newPart.addTag("drawItem","textB;-27.79;14.375;3.75;##ooPin3@@;pin 1")
newPart.addTag("drawItem","textB;-25.25;13.25;3.75;##ooPin4@@;pin 1")
newPart.addTag("drawItem","textB;-22.71;14.375;3.75;##ooPin5@@;pin 1")
newPart.addTag("drawItem","textB;-20.17;13.25;3.75;##ooPin6@@;pin 1")
newPart.addTag("drawItem","textB;-17.63;14.375;3.75;##ooPin7@@;pin 1")
newPart.addTag("drawItem","textB;-15.09;13.25;3.75;##ooPin8@@;pin 1")
newPart.addTag("drawItem","textB;-12.55;14.375;3.75;##ooPin9@@;pin 1")
newPart.addTag("drawItem","textB;-10.01;13.25;3.75;##ooPin10@@;pin 1")
newPart.addTag("drawItem","textB;-7.47;14.375;3.75;##ooPin11@@;pin 1")
newPart.addTag("drawItem","textB;-4.93;13.25;3.75;##ooPin12@@;pin 1")
newPart.addTag("drawItem","textB;-2.39;14.375;3.75;##ooPin13@@;pin 1")
newPart.addTag("drawItem","textB;0.15;13.25;3.75;##ooPin14@@;pin 1")
newPart.addTag("drawItem","textB;2.69;14.375;3.75;##ooPin15@@;pin 1")
newPart.addTag("drawItem","textB;5.23;13.25;3.75;##ooPin16@@;pin 1")
newPart.addTag("drawItem","oompName;0;25;40;10;##name@@")
newPart.addTag("drawItem","oompURL;0;-22;12;##hexID@@")

OOMP.parts.append(newPart)
