import OOMP

print("Generating Pickle Files:")
OOMP.loadParts("all")
#OOMP.loadParts("nofootprints")
#OOMP.loadParts("parts")

print(OOMP.getReport())

#import OOMP_genBlanks

input("ALL DONE")

for part in OOMP.parts:
    print(part.getID())