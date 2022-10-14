import OOMP
import OOMP_footprints_BASE

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")
OOMP.loadParts("pickle")

#OOMP_footprints_BASE.gitPull()

#OOMP_footprints_BASE.createAllFootprints()
#OOMP.loadParts("all")

OOMP_footprints_BASE.harvestAllFootprints()





###### SINGLE
id = ""
footprint = OOMP.getPartByID(id)

#harvestFootprint(footprint,all=False,copySourceFiles=False,harvestFootprintImages=False,
harvestFootprint(footprint,all=True)