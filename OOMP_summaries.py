import OOMP
import OOMP_summaries_BASE
import OOMP_summaries_COLLECTIONS

OOMP.loadParts("pickle")

def all(filter = ""):
    OOMP_summaries_BASE.createAllSummaries(all=True,filter=filter,overwrite=True)

def single(oompid):
    overwrite = False
    item = OOMP.getPartByID(oompid)
    testID = project.getID()
    if testID != "----":
        OOMP_cummaries_BASE.createSummary(item,overwrite=overwrite, all=True)
    else:
        print("No Item Found")
    

#create()

#OOMP.loadParts("projects")
#OOMP.loadParts("nofootprints")


#all()
filter = ""
#filter = ""
#all(filter)

#oompID="PROJ-SIRB-0002-STAN-01"
#single(oompID)

OOMP_summaries_COLLECTIONS.generateCollections()