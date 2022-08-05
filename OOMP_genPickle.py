import OOMP
import OOMPgenerate
import OOMPinkscapeGenerate
import OOMPeda
from oomBase import *
import json




OOMP.parts = []
OOMP.details = []
print("Generating Pickle Files:")
OOMP.loadParts("all")

print("Number of Items: "+ str(len(OOMP.getItems("all"))))
print("Number of Footprints: "+ str(len(OOMP.getItems("footprints"))))
print("Number of Parts: "+ str(len(OOMP.getItems("parts"))))
print("Number of Projects: "+ str(len(OOMP.getItems("projects"))))

OOMP.exportPickle()

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")

######  Readmes
#OOMPgenerate.generateAll(labels=False,scads=False,renders=False,readmes=True,json=True,diagrams=True,diagRenders=False,images=False,overwrite=True)

