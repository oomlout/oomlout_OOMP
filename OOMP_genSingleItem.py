import OOMP
import OOMPgenerate
import OOMPinkscapeGenerate
import OOMPeda
from oomBase import *



######  Choose part load method
OOMP.loadParts("pickle")


print(OOMP.getReport())

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")

OOMP.getItems("load",cache=False)



filter = "all"
#filter = "nofootprints"
#filter = "footprints"
#filter = "symbols"
#filter="projects"

OOMP.getItems("load",cache=False)


item = OOMP.getPartByID("PROJ-ADAF-1430-STAN-01")

overwrite=False

labels=False
scads=False
renders=False
readmes=False
diagrams=False
diagRenders=False
images=True
json=False

OOMPgenerate.generateItem(item, labels=labels,scads=scads,renders=renders,readmes=readmes,diagrams=diagrams,diagRenders=diagRenders,images=images,json=json,overwrite=overwrite)

