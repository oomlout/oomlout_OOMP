import OOMP
import OOMPgenerate
import OOMPinkscapeGenerate
import OOMPeda
from oomBase import *



######  Choose part load method
import OOMP_genPickle
#OOMP.loadParts("pickle")

print("Number of Items: "+ str(len(OOMP.getItems("all"))))
print("Number of Footprints: "+ str(len(OOMP.getItems("footprints"))))
print("Number of Parts: "+ str(len(OOMP.getItems("parts"))))
print("Number of Projects: "+ str(len(OOMP.getItems("projects"))))

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")

######  Images
OOMPgenerate.generateAll(labels=False,scads=False,renders=False,readmes=False,diagrams=False,diagRenders=False,images=True,overwrite=False)
######  All but labels
OOMPgenerate.generateAll(labels=False,scads=True,renders=True,readmes=True,diagrams=False,diagRenders=True,images=True,overwrite=False)
######  Labels
OOMPgenerate.generateAll(labels=True,scads=False,renders=False,readmes=False,diagrams=False,diagRenders=False,images=False,overwrite=False,json=True)
######  Readmes
OOMPgenerate.generateAll(labels=False,scads=False,renders=False,readmes=True,json=True,diagrams=True,diagRenders=False,images=False,overwrite=True)
