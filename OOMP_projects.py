import OOMP
import OOMP_projects_BASE

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")
OOMP.loadParts("pickle")

print(OOMP.getReport())



#OOMP.loadParts("nofootprints")
#import oomlout_OOMP_projects.test


def create():
    OOMP_projects_BASE.createAllProjects()

def all(filter=""):
    OOMP_projects_BASE.harvestProjects(filter)
    OOMP.loadParts("all")
    OOMP_projects_BASE.harvestProjects(filter)
    OOMP.loadParts("all")
    OOMP_projects_BASE.harvestProjects(filter)

def single(oompid):
    overwrite = False
    project = OOMP.getPartByID(oompid)
    testID = project.getID()
    if testID != "----":
        OOMP_projects_BASE.harvestProject(project,overwrite=overwrite, all=True)
    else:
        print("No Project Found")
    

#create()

#OOMP.loadParts("projects")
#OOMP.loadParts("nofootprints")


#all()
filter = "IBBC"
filter = ""
all(filter)

#oompID="PROJ-SIRB-0002-STAN-01"
#single(oompID)






