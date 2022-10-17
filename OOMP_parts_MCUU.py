import OOMP

import OOMP_parts_BASE

def addParts():
##############################
    ######  MCUU
    if True:
        type = "MCUU";size = "";color = "84";desc = "ATTINY";index = "01";hexID = "MCAT84SC14"
        datasheet = "sourceDatasheets/MCUU-SC14-84-ATTINY-01.pdf"
        
        ss = {}
        id = "QFN14"
        ss[id] = {}
        ss[id]["SYMBOL"] = "SYMBOL-kicad-kicad-symbols-MCU_Microchip_ATtiny-ATtiny84-20M"
        ss[id]["FOOTPRINT"] = "FOOTPRINT-kicad-kicad-footprints-Package_DFN_QFN-QFN-20-1EP_4x4mm_P0.5mm_EP2.6x2.6mm"
        id = "DI14"
        ss[id] = {}
        ss[id]["SYMBOL"] = "SYMBOL-kicad-kicad-symbols-MCU_Microchip_ATtiny-ATtiny84-20P"
        ss[id]["FOOTPRINT"] = "FOOTPRINT-kicad-kicad-footprints-Package_DIP-DIP-14_W7.62mm"
        id = "SC14"
        ss[id] = {}
        ss[id]["SYMBOL"] = "SYMBOL-kicad-kicad-symbols-MCU_Microchip_ATtiny-ATtiny20-SS"
        ss[id]["FOOTPRINT"] = "FOOTPRINT-kicad-kicad-footprints-Package_SO-SOIC-14_3.9x8.7mm_P1.27mm"
        for s in ss:
            size = s
            extraTags = []
            extraTags.append(OOMP.oompTag("footprintKicad",ss[s]["FOOTPRINT"]))
            extraTags.append(OOMP.oompTag("symbolKicad",ss[s]["SYMBOL"]))
            d = {"type" : type, "size" : size, "color" : color, "desc" : desc, "index" : index, "hexID" : hexID, "datasheet" : datasheet, "extraTags" : extraTags}
            OOMP_parts_BASE.makePart(dict = d)   
