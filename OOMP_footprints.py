import OOMP
import OOMP_footprints_BASE
import OOMP_footprints_KICAD

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")

def working():
    pass
    OOMP.loadParts("pickle")
    print(OOMP.getReport())
    #OOMP_footprints_BASE.gitPull()

    #OOMP_footprints_BASE.gitFullPull()


    #OOMP_footprints_BASE.createAllFootprints()
    #OOMP.loadParts("all")

    #OOMP_footprints_BASE.harvestAllFootprints()

    #OOMP_footprints_BASE.createFootprintLibraries()



    ###### SINGLE
    #id = "FOOTPRINT-kicad-kicad-footprints-LED_THT-LED_Rectangular_W3.9mm_H1.8mm"
    #footprint = OOMP.getPartByID(id)

    #def harvestFootprint(footprint,all=False,copySourceFiles=False,harvestFootprintImages=False,
    #OOMP_footprints_KICAD.harvestFootprint(footprint,all=True)

def refreshFull():
    OOMP.loadParts("all")
    OOMP_footprints_BASE.gitPull()
    OOMP_footprints_BASE.createAllFootprints()    
    OOMP.loadParts("all")    
    OOMP_footprints_BASE.harvestAllFootprints()

#working()
#refreshFull()

 #__import__("sourceFiles.oompLoad") 
#OOMP.loadParts("pickle")
#print(OOMP.getReport())
#OOMP.reset()
#OOMP.loadParts("pickle")
#print(OOMP.getReport())
#OOMP.reset()
#OOMP.loadParts("pickle")
#print(OOMP.getReport())
#OOMP.loadParts("pickle")
#print(OOMP.getReport())

"""
import importlib

name = "sourceFiles.oompLoad"

print(OOMP.getReport())
name = "sourceFiles.oompLoad"
mod = importlib.import_module(name)
importlib.reload(mod)
print(OOMP.getReport())
OOMP.reset()
print(OOMP.getReport())
importlib.reload(mod)
print(OOMP.getReport())
"""

