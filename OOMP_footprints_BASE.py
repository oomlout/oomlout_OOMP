import OOMP
import OOMPeda
from oomBase import *

import OOMP_footprints_KICAD

def gitPull():
    dir = "sourceFiles/git/"
    oomMakeDir(dir)
    ###### Kicad Base Footprints
    gitLoc = "https://gitlab.com/kicad/libraries/kicad-footprints";    oomGitPull(gitLoc,dir)
    ###### oomlout_OOMP_modules    
    gitLoc = "https://github.com/oomlout/oomlout_OOMP_kicad";    oomGitPull(gitLoc,dir)
    ###### oomlout_OOMP_modules
    gitLoc = "https://github.com/Digi-Key/digikey-kicad-library";    oomGitPull(gitLoc,dir)
    

def createAllFootprints():
    OOMP_footprints_KICAD.createFootprints()

def harvestAllFootprints():
    OOMP_footprints_KICAD.harvestFootprints()    


