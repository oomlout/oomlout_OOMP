import OOMP
import OOMP_footprints_BASE
import OOMP_footprints_KICAD

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")
OOMP.loadParts("pickle")

#OOMP_footprints_BASE.gitPull()

#OOMP_footprints_BASE.createAllFootprints()
#OOMP.loadParts("all")

#OOMP_footprints_BASE.harvestAllFootprints()





###### SINGLE
id = "FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_Rectangular_W3.9mm_H1.8mm"
footprint = OOMP.getPartByID(id)

#def harvestFootprint(footprint,all=False,copySourceFiles=False,harvestFootprintImages=False,
OOMP_footprints_KICAD.harvestFootprint(footprint,all=True)