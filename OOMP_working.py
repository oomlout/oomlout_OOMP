import OOMP
import OOMPgenerate
import OOMPinkscapeGenerate
import OOMPeda
from oomBase import *

OOMP.printParts()


#print(OOMP.parts)
#print(OOMP.getPartByHex("H03R"))


## Generate

#OOMPgenerate.generateAll(labels=True,scads=False,renders=False,readmes=False,diagrams=False,diagRenders=False,images=False)

item = OOMP.parts[3]
#OOMPgenerate.generateItem(item, labels=False,scads=False,renders=False,readmes=True,diagrams=False,diagRenders=False,images=False)

#print(item)

#OOMPinkscapeGenerate.generateDiagram(item)

#OOMPinkscapeGenerate.generateDiagrams()

        
#item = OOMP.parts[2]
#OOMPinkscapeGenerate.generateDiagram(item)
#item = OOMP.parts[3]
#OOMPinkscapeGenerate.generateDiagram(item)

OOMPeda.harvestKicadFootprintImages()
#OOMPeda.harvestKicadSymbolImages()

#library="C:/EAGLE 9.6.2/cache/lbr/pinhead.lbr"
#libraryName="pinhead"
#OOMPeda.harvestEagleFootprint(library,libraryName)
#OOMPeda.harvestEagleLibraries()

#oomDelay(2)
#oomMouseScrollWheel(movement=-50)

#oomScreenCapture("temp1.png",crop=[560,105,900,900])

