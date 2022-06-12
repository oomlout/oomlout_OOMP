######  OOMP Template File
import OOMP

indexA = len(OOMP.parts) + 1
newPart = OOMP.oompItem(indexA)
newPart.addTag("hexID", "RESE-W04-X-XXXX-XX-bbls")
newPart.addTag("oompType", "TEMPLATE")
newPart.addTag("oompSize", "A")
newPart.addTag("oompColor", "A")
newPart.addTag("oompDesc", "A")
newPart.addTag("oompIndex", str(indexA))


newPart.addTag("drawItem","linewidth;0.2")
newPart.addTag("drawItem","template;RESE-W04-X-XXXX-01")
newPart.addTag("drawItem","vLineColor;-1.782;0;1;2.3;##colorBand1@@;band1")
newPart.addTag("drawItem","vLineColor;-0.782;0;1;1.875;##colorBand2@@;band2")
newPart.addTag("drawItem","vLineColor;0.218;0;1;1.75;##colorBand3@@;band3")
newPart.addTag("drawItem","vLineColor;2.218;0;1;2.3;GOLD;band3")
newPart.addTag("drawItem","corTemplate;RESE-W04-X-XXXX-OT")
newPart.addTag("drawItem","oompName;0;5;20;5;1.33;##name@@")
newPart.addTag("drawItem","oompURL;0;-3.5;0.75;##hexID@@")

OOMP.parts.append(newPart)
