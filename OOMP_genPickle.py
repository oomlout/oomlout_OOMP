import OOMP

print("Generating Pickle Files:")

OOMP.loadParts("all")
#OOMP.loadParts("nofootprints")
#OOMP.loadParts("parts")

#__import__("sourceFiles.oompLoad")  
#exportPickle() 


print(OOMP.getReport())

#import OOMP_genBlanks



input("ALL DONE")

for part in OOMP.parts:
    pass
    #print(part.getID())