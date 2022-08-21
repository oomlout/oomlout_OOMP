import OOMP
import OOMPgenerate
import OOMPinkscapeGenerate
import OOMPeda
from oomBase import *


OOMP.loadParts("pickle")

print("Number of Items: "+ str(len(OOMP.getItems("all"))))
print("Number of Footprints: "+ str(len(OOMP.getItems("footprints"))))
print("Number of Parts: "+         str(len(OOMP.getItems("parts"))))
print("Number of Projects: "+ str(len(OOMP.getItems("projects"))))

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")

filter = "all"
filter = "projects"
filter = "nofootprints"
######  Readmes
OOMPgenerate.generateAll(readmes=True,json=True,overwrite=True,filter=filter)
