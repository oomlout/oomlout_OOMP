import OOMP
import OOMPproject
from oomBase import *

######  Company Files
import OOMP_projects_ELLA

def createAllProjects():
    OOMP_projects_ELLA.createProjects()

def makeProject(d):
    type = d["oompType"]
    size = d["oompSize"]
    color = d["oompColor"]
    desc = d["oompDesc"]
    index = d["oompIndex"]

    hexID = d["hexID"]

    oompID = type + "-" + size + "-" + color + "-" + desc + "-" + index

    inputFile = "templates/projectsTemplate.py"
    outputDir = "C:/GH/oomlout_OOMP/oomlout_OOMP_projects/" + oompID + "/"
    outputFile = outputDir + "details.py"

    print("Making: " + outputFile)

    contents = oomReadFileToString(inputFile)
    contents = contents.replace("TYPEZZ",type)
    contents = contents.replace("SIZEZZ",size)
    contents = contents.replace("COLORZZ",color)
    contents = contents.replace("DESCZZ",desc)
    contents = contents.replace("INDEXZZ",index)
    contents = contents.replace("HEXZZ",hexID)


    sp = d["gitRepo"].split("/")
    repoName = sp[len(sp)-1]

    extraTags = []
    tagString = ""
    extraTags.append(OOMP.oompTag("name",d["name"]))
    extraTags.append(OOMP.oompTag("gitRepo",d["gitRepo"]))
    extraTags.append(OOMP.oompTag("gitName",repoName))
    extraTags.append(OOMP.oompTag("eagleBoard",d["eagleBoard"]))
    extraTags.append(OOMP.oompTag("eagleSchem",d["eagleSchem"]))
    for tag in extraTags:
        tagString = tagString + tag.getPythonLine() + "\n"

    contents = contents.replace("EXTRAZZ",tagString)

    oomWriteToFile(outputFile,contents)

def harvestProjects():
    for project in OOMP.getItems("projects"):
        test = project.getTag("gitRepo").value
        if test != "":
            harvestProject(project,all=True)

def harvestProject(project,all=False,gitPull=False,copyBaseFiles=False,harvestEagle=False,harvestKicad=False,overwrite=False):
    oompID = project.getID()
    print("Harvesting Project: " + oompID)

    if all or gitPull:
        pass
        #gitPullProject(project)
    if all or copyBaseFiles:
        pass
        #copyBaseFilesProject(project)
    if all or harvestEagle:        
        pass
        #harvestEagleProject(project,overwrite)
    if all or harvestKicad:
        pass
        harvestKicadProject(project,overwrite)

def gitPullProject(project):
    print("    Pulling or cloning project ")
    gitRepo = project.getTag("gitRepo").value
    if gitRepo == "":
        raise Exception("No git repo for project")
    else:
        oomGitPull(gitRepo,"sourceFiles/git/")

def copyBaseFilesProject(project):
    print("    Copying Base Files ")
    type = "Board"
    filename = project.getTag("eagle" + type).value    
    outfile = outFile = project.getFilename(type + "Eagle")
    if filename != "":
        inFile = "sourceFiles/git/" + project.getTag("gitName").value + "/" + filename
    else:
        filename = project.getTag("kicad" + type).value
        if filename != "":
            inFile = "sourceFiles/git/" + project.getTag("gitName").value + "/" + filename
            outfile = outFile = project.getFilename(type + "Kicad")
        else:
            raise Exception("No source board file found")
    oomCopyFile(inFile,outFile)
    type = "Schem"
    filename = project.getTag("eagle" + type).value    
    outfile = outFile = project.getFilename(type + "Eagle")
    if filename != "":
        inFile = "sourceFiles/git/" + project.getTag("gitName").value + "/" + filename
    else:
        filename = project.getTag("kicad" + type).value
        if filename != "":
            inFile = "sourceFiles/git/" + project.getTag("gitName").value + "/" + filename
            outfile = outFile = project.getFilename(type + "Kicad")
        else:
            raise Exception("No source board file found")
    oomCopyFile(inFile,outFile)
    
def harvestEagleProject(project,overwrite=False):
    print("    Harvesting Eagle Files ")
    eagleBoardFile = project.getFilename("boardeagle")
    projectDir = project.getFolder()
    eagleBoardFileFull = project.getFilename("boardeagle",relative="full")
    oomLaunchOpen(eagleBoardFileFull)
    oomDelay(20)
    oomSendMaximize()
    oomDelay(2)
    oomSendMaximize()
    oomDelay(2)
    OOMPproject.harvestEagleBoardFile(eagleBoardFile,projectDir,overwrite=overwrite)
    OOMPproject.harvestEagleSchematicFile(eagleBoardFile.replace("boardEagle.brd","schematicEagle.sch"),projectDir,overwrite=overwrite)
    oomSendAltKey("x",delay=5)
    oomSendAltKey("x",delay=5)

def harvestKicadProject(project,overwrite=False):
    print("    Harvesting Kicad Files ")
    kicadBoardFile = project.getFilename("boardkicad")
    oomLaunchKicad()
    oomDelay(10)
    eagleBoardFile = project.getFilename("boardeagle")
    projectDir = project.getFolder()
    OOMPproject.harvestEagleBoardToKicad(eagleBoardFile,projectDir,overwrite=overwrite)
    OOMPproject.harvestEagleSchemToKicad(eagleBoardFile.replace("boardEagle.brd","schematicEagle.sch"),projectDir,overwrite=overwrite)
    OOMPproject.harvestKicadBoardFile(kicadBoardFile,projectDir,overwrite=overwrite)
