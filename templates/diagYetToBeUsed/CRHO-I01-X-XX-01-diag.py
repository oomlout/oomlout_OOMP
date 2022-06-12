######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "CRHO-I01-X-XX-01-diag")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;1")
newPart.addTag("drawItem","rectangle;0;0;2.54*%%pins%%;14;Main Square")
newPart.addTag("drawItem","linewidth;0.5")


newPart.addTag("drawItem","oompName;0;11;20;5;1.33;##name@@")
newPart.addTag("drawItem","oompURL;0;-8.5;0.75;##hexID@@")

OOMP.parts.append(newPart)
