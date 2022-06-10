######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "BUTP-07-X-STAN-69-bbls")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","corTemplate;BUTP-07-X-STAN-69-bbls")
newPart.addTag("drawItem","oompName;0;11.5;20;5;##name@@")
newPart.addTag("drawItem","oompURL;0;-7.33;5;##hexID@@")

OOMP.parts.append(newPart)
