import OOMP
import OOMP_projects_BASE

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")
OOMP.loadParts("pickle")

print(OOMP.getReport())



#OOMP.loadParts("nofootprints")
#import oomlout_OOMP_projects.test


def create():
    OOMP_projects_BASE.createAllProjects()

def all(filter="",exclusions="NONE"):
    OOMP_projects_BASE.harvestProjects(filter,exclusions)
    OOMP.loadParts("all")
    OOMP_projects_BASE.harvestProjects(filter)
    OOMP.loadParts("all")
    OOMP_projects_BASE.harvestProjects(filter)

def single(oompid):
    d = {"all" :False,
        "gitPull" : False,
        "copyBaseFiles" : False,
        "harvestEagle" : False,
        "harvestKicad" : False,
        "matchParts" : True,
    }
    overwrite = True

    #overwrite = False
    project = OOMP.getPartByID(oompid)
    testID = project.getID()
    if testID != "----":
        #OOMP_projects_BASE.harvestProject(project,overwrite=overwrite, dict={"all" : True} )
        OOMP_projects_BASE.harvestProject(project,dict=d,overwrite=overwrite)
    else:
        print("No Project Found")
    
#create()

#OOMP.loadParts("projects")
#OOMP.loadParts("nofootprints")

#filter = ""
#filter = "DANP"  
#exclusions = "NONE" ## not working yet
#exclusions = "ADAF" ## not working yet
#all(filter,exclusions)

oompID="PROJ-SPAR-15932-STAN-01"
single(oompID)






