######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "ICIC-DI08-X-XXXX-01")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))



newPart.addTag("drawItem","rectangle;0;0;7.25;4*2.54;Main Square")


newPart.addTag("drawItem","rectangle;-4.125;2.54/2+1*2.54;1;1;pin 1")
newPart.addTag("drawItem","rectangle;-4.125;2.54/2+0*2.54;1;1;pin 2")
newPart.addTag("drawItem","rectangle;-4.125;-2.54/2-1*2.54;1;1;pin 3")
newPart.addTag("drawItem","rectangle;-4.125;-2.54/2-0*2.54;1;1;pin 4")

newPart.addTag("drawItem","textB;-7.125;2.54/2+1*2.54;2.5;##ooPin1@@;pin 1")
newPart.addTag("drawItem","textB;-7.125;2.54/2+0*2.54;2.5;##ooPin2@@;pin 2")
newPart.addTag("drawItem","textB;-7.125;-2.54/2-1*2.54;2.5;##ooPin3@@;pin 3")
newPart.addTag("drawItem","textB;-7.125;-2.54/2-0*2.54;2.5;##ooPin4@@;pin 4")



newPart.addTag("drawItem","rectangle;4.125;2.54/2+1*2.54;1;1;pin 8")
newPart.addTag("drawItem","rectangle;4.125;2.54/2+0*2.54;1;1;pin 7")
newPart.addTag("drawItem","rectangle;4.125;-2.54/2-1*2.54;1;1;pin6")
newPart.addTag("drawItem","rectangle;4.125;-2.54/2-0*2.54;1;1;pin 5")

newPart.addTag("drawItem","textB;7.125;2.54/2+1*2.54;2.5;##ooPin8@@;pin 8")
newPart.addTag("drawItem","textB;7.125;2.54/2+0*2.54;2.5;##ooPin7@@;pin 7")
newPart.addTag("drawItem","textB;7.125;-2.54/2-1*2.54;2.5;##ooPin6@@;pin 6")
newPart.addTag("drawItem","textB;7.125;-2.54/2-0*2.54;2.5;##ooPin5@@;pin 5")


newPart.addTag("drawItem","oompName;0;2.54/2+3*2.54;20;5;1.33;##name@@")
newPart.addTag("drawItem","oompURL;0;-2.54/2-3*2.54;0.75;##hexID@@")

OOMP.parts.append(newPart)
