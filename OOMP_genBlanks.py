import OOMP
import OOMPgenerate
import OOMPinkscapeGenerate
import OOMPeda
from oomBase import *



######  Choose part load method
#import OOMP_genPickle
OOMP.loadParts("pickle")

print("Number of Items: "+ str(len(OOMP.getItems("all"))))
print("Number of Symbols: "+ str(len(OOMP.getItems("symbols"))))
print("Number of Footprints: "+ str(len(OOMP.getItems("footprints"))))
print("Number of Parts: "+ str(len(OOMP.getItems("parts"))))
print("Number of Projects: "+ str(len(OOMP.getItems("projects"))))

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")



filter = "all"
#filter = "nofootprints"
#filter = "footprints"
#filter = "symbols"
#filter="projects"

OOMP.getItems("load",cache=False)

######  Images
OOMPgenerate.generateAll(filter=filter,images=True,overwrite=False)
######  All but labels
OOMPgenerate.generateAll(filter =filter,scads=True,renders=True,readmes=True,diagrams=False,diagRenders=True,images=True,overwrite=False)
######  Labels
OOMPgenerate.generateAll(filter =filter,labels=True)
######  Overwrite Readme and JSON
OOMPgenerate.generateAll(filter =filter,readmes=True,json=True,overwrite=True)

