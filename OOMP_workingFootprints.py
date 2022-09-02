import OOMP
import OOMPgenerate
import OOMPinkscapeGenerate
import OOMPeda
from oomBase import *
import json
        
#OOMP.loadParts("all")
#OOMP.exportPickle()

OOMP.loadParts("pickle")

print("Number of Items: "+ str(len(OOMP.getItems("all"))))
print("Number of Symbols: "+ str(len(OOMP.getItems("symbols"))))
print("Number of Footprints: "+ str(len(OOMP.getItems("footprints"))))
print("Number of Parts: "+ str(len(OOMP.getItems("parts"))))
print("Number of Projects: "+ str(len(OOMP.getItems("projects"))))

#OOMP.printParts()
OOMP.setBaseDir("C:/GH/oomlout_OOMP/")

#oomDelay(5)

### ### Single is for doing default libraries

#OOMPeda.harvestEagleLibraries(footprint=True,files=True,single=True, overwrite=False)
harvestKicadSymbolsFiles = False
harvestKicadSymbolsImages = True
harvestEagleLibraries = False
overwrite=True
overwrite=False
filter="all"
filter="symbols"
OOMPeda.doTasks(overwrite=overwrite,harvestKicadSymbolsFiles=harvestKicadSymbolsFiles, harvestKicadSymbolsImages=harvestKicadSymbolsImages,harvestEagleLibraries=harvestEagleLibraries)

#OOMPeda.eagleSetLibrary("19inch")
#OOMPeda.eagleResetLibrary()

#import OOMP_genPickle

#OOMPeda.harvestKicadLibraries()

#owner = "kicad-footprints"
#OOMPEDA.harvestKicadFootprintImages(owner)
#library="C:/EAGLE 9.6.2/cache/lbr/pinhead.lbr"
#libraryName="pinhead"
#OOMPeda.harvestEagleFootprint(library,libraryName)

# search
## image.png -imageZ1 -imageZ2 -imageZ3 -imagez4 -imagez5 -imagez6 -imagez7 -imagez8 -imagez9 -_140 -_450 -_600
#OOMPeda.harvestEagleLibraries()

#oomDelay(2)
#oomMouseScrollWheel(movement=-50)


#oomScreenCapture("temp1.png",crop=[560,105,900,900])


#json testing
#item = OOMP.parts[517]

#print(json.dumps(item,default=lambda o: o.__dict__, sort_keys=True, indent=4))
#print(item.__dict__)