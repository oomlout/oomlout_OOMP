######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "LEDS-10-X-XXXX-01-diag")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;0.2")
newPart.addTag("drawItem","corTemplate;LEDS-10-X-XXXX-01-diag")
newPart.addTag("drawItem","textB;-1.14;9.1;5;A;Anode")
newPart.addTag("drawItem","textB;1.14;9.1;5;K;Cathode")
newPart.addTag("drawItem","oompName;0;23;20;5;1.33;##name@@")
newPart.addTag("drawItem","oompURL;0;-21;4;##hexID@@")

OOMP.parts.append(newPart)
