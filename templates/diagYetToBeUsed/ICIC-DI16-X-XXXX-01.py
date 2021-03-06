######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "ICIC-DI16-X-XXXX-01")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))




newPart.addTag("drawItem","rectangle;0;0;7.25;19.26;Main Square")
newPart.addTag("drawItem","rectangle;4.125;8.89;1;1;pin 1")
newPart.addTag("drawItem","rectangle;4.125;6.35;1;1;pin 1")
newPart.addTag("drawItem","rectangle;4.125;3.81;1;1;pin 1")
newPart.addTag("drawItem","rectangle;4.125;1.27;1;1;pin 1")
newPart.addTag("drawItem","rectangle;4.125;-1.27;1;1;pin 1")
newPart.addTag("drawItem","rectangle;4.125;-3.81;1;1;pin 1")
newPart.addTag("drawItem","rectangle;4.125;-6.35;1;1;pin 1")
newPart.addTag("drawItem","rectangle;4.125;-8.89;1;1;pin 1")

newPart.addTag("drawItem","textB;7.125;8.89;2.5;##ooPin1@@;pin 1")
newPart.addTag("drawItem","textB;7.125;6.35;2.5;##ooPin2@@;pin 1")
newPart.addTag("drawItem","textB;7.125;3.81;2.5;##ooPin3@@;pin 1")
newPart.addTag("drawItem","textB;7.125;1.27;2.5;##ooPin4@@;pin 1")
newPart.addTag("drawItem","textB;7.125;-1.27;2.5;##ooPin5@@;pin 1")
newPart.addTag("drawItem","textB;7.125;-3.81;2.5;##ooPin6@@;pin 1")
newPart.addTag("drawItem","textB;7.125;-6.35;2.5;##ooPin7@@;pin 1")
newPart.addTag("drawItem","textB;7.125;-8.89;2.5;##ooPin8@@;pin 1")


newPart.addTag("drawItem","rectangle;-4.125;8.89;1;1;pin 1")
newPart.addTag("drawItem","rectangle;-4.125;6.35;1;1;pin 1")
newPart.addTag("drawItem","rectangle;-4.125;3.81;1;1;pin 1")
newPart.addTag("drawItem","rectangle;-4.125;1.27;1;1;pin 1")
newPart.addTag("drawItem","rectangle;-4.125;-1.27;1;1;pin 1")
newPart.addTag("drawItem","rectangle;-4.125;-3.81;1;1;pin 1")
newPart.addTag("drawItem","rectangle;-4.125;-6.35;1;1;pin 1")
newPart.addTag("drawItem","rectangle;-4.125;-8.89;1;1;pin 1")

newPart.addTag("drawItem","textB;-7.125;8.89;2.5;##ooPin9@@;pin 1")
newPart.addTag("drawItem","textB;-7.125;6.35;2.5;##ooPin10@@;pin 1")
newPart.addTag("drawItem","textB;-7.125;3.81;2.5;##ooPin11@@;pin 1")
newPart.addTag("drawItem","textB;-7.125;1.27;2.5;##ooPin12@@;pin 1")
newPart.addTag("drawItem","textB;-7.125;-1.27;2.5;##ooPin13@@;pin 1")
newPart.addTag("drawItem","textB;-7.125;-3.81;2.5;##ooPin14@@;pin 1")
newPart.addTag("drawItem","textB;-7.125;-6.35;2.5;##ooPin15@@;pin 1")
newPart.addTag("drawItem","textB;-7.125;-8.89;2.5;##ooPin16@@;pin 1")

newPart.addTag("drawItem","oompName;0;13;20;5;1.33;##name@@")
newPart.addTag("drawItem","oompURL;0;-11;0.75;##hexID@@")

OOMP.parts.append(newPart)
