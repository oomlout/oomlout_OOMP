import OOMP
import OOMP_projects_BASE

OOMP.setBaseDir("C:/GH/oomlout_OOMP/")
OOMP.loadParts("pickle")

#OOMP_projects_BASE.createAllProjects()

#OOMP.loadParts("nofootprints")
#import oomlout_OOMP_projects.test

OOMP_projects_BASE.harvestProjects()
OOMP.loadParts("all")
OOMP_projects_BASE.harvestProjects()
OOMP.loadParts("all")
OOMP_projects_BASE.harvestProjects()




