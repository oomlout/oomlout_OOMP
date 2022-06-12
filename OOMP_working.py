import OOMP
import OOMPgenerate
import OOMPinkscapeGenerate

OOMP.printParts()


#print(OOMP.parts)
#print(OOMP.getPartByHex("H03R"))


## Generate

#OOMPgenerate.generateAll(labels=False,scads=False,renders=False,readmes=False,diagrams=False,diagRenders=True,images=False)

item = OOMP.parts[5]
#OOMPgenerate.generateItem(item, labels=False,scads=False,renders=False,readmes=False,diagrams=True,diagRenders=False,images=False)

print(item)

#OOMPinkscapeGenerate.generateDiagram(item)

#OOMPinkscapeGenerate.generateDiagrams()

#item = OOMP.parts[2]
#OOMPinkscapeGenerate.generateDiagram(item)
#item = OOMP.parts[3]
#OOMPinkscapeGenerate.generateDiagram(item)