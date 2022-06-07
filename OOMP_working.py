import OOMP
import OOMPgenerate

OOMP.printParts()


print(OOMP.parts)
#print(OOMP.getPartByHex("H03R"))


## Generate

#OOMPgenerate.generateAll(labels=False,scads=False,renders=False,readmes=False,diagrams=False,diagRenders=False,images=False)

item = OOMP.parts[3]
OOMPgenerate.generateItem(item, labels=False,scads=False,renders=False,readmes=False,diagrams=False,diagRenders=False,images=False)

