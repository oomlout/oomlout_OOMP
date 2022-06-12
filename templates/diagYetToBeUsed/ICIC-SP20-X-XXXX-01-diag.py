######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "ICIC-SP20-X-XXXX-01-diag")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","template;ICIC-SP20-X-XXXX-01")
newPart.addTag("drawItem","textB;-1.319;5.715;1;##ooPin1@@;pin 1")
newPart.addTag("drawItem","textB;-2.325;4.445;1;##ooPin2@@;pin 2")
newPart.addTag("drawItem","textB;-2.325;3.175;1;##ooPin3@@;pin 3")
newPart.addTag("drawItem","textB;-2.325;1.905;1;##ooPin4@@;pin 4")
newPart.addTag("drawItem","textB;-2.325;0.635;1;##ooPin5@@;pin 5")
newPart.addTag("drawItem","textB;-2.325;-5.715;1;##ooPin10@@;pin 10")
newPart.addTag("drawItem","textB;-2.325;-4.445;1;##ooPin9@@;pin 9")
newPart.addTag("drawItem","textB;-2.325;-3.175;1;##ooPin8@@;pin 8")
newPart.addTag("drawItem","textB;-2.325;-1.905;1;##ooPin7@@;pin 7")
newPart.addTag("drawItem","textB;-2.325;-0.635;1;##ooPin6@@;pin 6")
newPart.addTag("drawItem","textB;2.325;5.715;1;##ooPin20@@;pin 20")
newPart.addTag("drawItem","textB;2.325;4.445;1;##ooPin19@@;pin 19")
newPart.addTag("drawItem","textB;2.325;3.175;1;##ooPin18@@;pin 18")
newPart.addTag("drawItem","textB;2.325;1.905;1;##ooPin17@@;pin 17")
newPart.addTag("drawItem","textB;2.325;0.635;1;##ooPin16@@;pin 16")
newPart.addTag("drawItem","textB;2.325;-5.715;1;##ooPin11@@;pin 11")
newPart.addTag("drawItem","textB;2.325;-4.445;1;##ooPin12@@;pin 12")
newPart.addTag("drawItem","textB;2.325;-3.175;1;##ooPin13@@;pin 13")
newPart.addTag("drawItem","textB;2.325;-1.905;1;##ooPin14@@;pin 14")
newPart.addTag("drawItem","textB;2.325;-0.635;1;##ooPin15@@;pin 15")
newPart.addTag("drawItem","oompName;0;10;20;5;1.33;##name@@")
newPart.addTag("drawItem","oompURL;0;-7.5;0.75;##hexID@@")

OOMP.parts.append(newPart)
