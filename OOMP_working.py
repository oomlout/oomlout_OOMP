import OOMP
import OOMPgenerate
import OOMPinkscapeGenerate
import OOMPeda
from oomBase import *
import json


#OOMP.loadParts("all")
#OOMP.exportPickle()

OOMP.loadParts("pickle")

#OOMP.printParts()
OOMP.setBaseDir("C:/GH/oomlout_OOMP/")

#for part in OOMP.parts:
    #print(part)
#print(OOMP.getPartByHex("H03R"))



## Generate

OOMPgenerate.generateAll(labels=False,scads=False,renders=False,readmes=False,json=True,diagrams=False,diagRenders=False,images=False,overwrite=False)


#OOMPgenerate.generateAll(labels=True,scads=True,renders=True,readmes=True,diagrams=True,diagRenders=True,images=True,overwrite=False)

#item = OOMP.parts[517]
#OOMPgenerate.generateItem(item, labels=False,scads=False,renders=False,readmes=False,json=True,diagrams=False,diagRenders=False,images=False,overwrite=True)

print(item)

#OOMPinkscapeGenerate.generateDiagram(item)

#OOMPinkscapeGenerate.generateDiagrams()

        
######  KICAD AND EAGLE THINGS

#OOMPeda.harvestEagleLibraries()
#OOMPeda.harvestKicadLibraries()


#library="C:/EAGLE 9.6.2/cache/lbr/pinhead.lbr"
#libraryName="pinhead"
#OOMPeda.harvestEagleFootprint(library,libraryName)

# search
## image.png -imageZ1 -imageZ2 -imageZ3 -imagez4 -imagez5 -imagez6 -imagez7 -imagez8 -imagez9
#OOMPeda.harvestEagleLibraries()

#oomDelay(2)
#oomMouseScrollWheel(movement=-50)


#oomScreenCapture("temp1.png",crop=[560,105,900,900])


#json testing
#item = OOMP.parts[517]

#print(json.dumps(item,default=lambda o: o.__dict__, sort_keys=True, indent=4))
#print(item.__dict__)