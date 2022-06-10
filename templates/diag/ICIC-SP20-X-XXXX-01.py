######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "ICIC-SP20-X-XXXX-01")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;0.1")
newPart.addTag("drawItem","rectangle;0;0;7.65;12.7;Main Square")
newPart.addTag("drawItem","circle;-3;5.5;0.25;0.25;Pin 1 marker")
newPart.addTag("drawItem","rectangle;-4.525;-5.715;1.4;0.4;pin 10")
newPart.addTag("drawItem","rectangle;-4.525;-4.445;1.4;0.4;pin 9")
newPart.addTag("drawItem","rectangle;-4.525;-3.175;1.4;0.4;pin 8")
newPart.addTag("drawItem","rectangle;-4.525;-1.905;1.4;0.4;pin 7")
newPart.addTag("drawItem","rectangle;-4.525;-0.635;1.4;0.4;pin 6")
newPart.addTag("drawItem","rectangle;-4.525;0.635;1.4;0.4;pin 5")
newPart.addTag("drawItem","rectangle;-4.525;1.905;1.4;0.4;pin 4")
newPart.addTag("drawItem","rectangle;-4.525;3.175;1.4;0.4;pin 3")
newPart.addTag("drawItem","rectangle;-4.525;4.445;1.4;0.4;pin 2")
newPart.addTag("drawItem","rectangle;-4.525;5.715;1.4;0.4;pin 1")
newPart.addTag("drawItem","rectangle;4.525;-5.715;1.4;0.4;pin 11")
newPart.addTag("drawItem","rectangle;4.525;-4.445;1.4;0.4;pin 12")
newPart.addTag("drawItem","rectangle;4.525;-3.175;1.4;0.4;pin 13")
newPart.addTag("drawItem","rectangle;4.525;-1.905;1.4;0.4;pin 14")
newPart.addTag("drawItem","rectangle;4.525;-0.635;1.4;0.4;pin 15")
newPart.addTag("drawItem","rectangle;4.525;0.635;1.4;0.4;pin 16")
newPart.addTag("drawItem","rectangle;4.525;1.905;1.4;0.4;pin 17")
newPart.addTag("drawItem","rectangle;4.525;3.175;1.4;0.4;pin 18")
newPart.addTag("drawItem","rectangle;4.525;4.445;1.4;0.4;pin 19")
newPart.addTag("drawItem","rectangle;4.525;5.715;1.4;0.4;pin 20")



OOMP.parts.append(newPart)
