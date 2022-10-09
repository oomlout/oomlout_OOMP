import OOMP
import OOMPproject
import OOMPprojectParts
from oomBase import *

######  Company Files
import OOMP_projects_ADAF
import OOMP_projects_ELLA
import OOMP_projects_IBBC
import OOMP_projects_SEED
import OOMP_projects_SOPA

def createAllProjects():
    OOMP_projects_IBBC.createProjects()
    OOMP_projects_ADAF.createProjects()    
    OOMP_projects_ELLA.createProjects()
    OOMP_projects_SEED.createProjects()
    OOMP_projects_SOPA.createProjects()

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

    repoName = ""
    extraTags = []
    try:
        sp = d["gitRepo"].split("/")
        repoName = sp[len(sp)-1]
        d["gitName"] = repoName
    except:
        print("No gitRepo found")
    
    

    tagList = ["name","gitRepo","gitName","eagleBoard","eagleSchem","kicadBoard","kicadSchem",]
    
    tagString = ""
    for tag in tagList:
        try:
            extraTags.append(OOMP.oompTag(tag,d[tag]))        
        except:
            print("No " + tag + " found")

    try:
        for tag in d["extraTags"]:
            extraTags.append(OOMP.oompTag(tag[0],tag[1]))        
    except:
        print("no extra tags")

    for tag in extraTags:
        tagString = tagString + tag.getPythonLine() + "\n"

    



    contents = contents.replace("EXTRAZZ",tagString)

    oomWriteToFile(outputFile,contents)

def harvestProjects():
    oomLaunchKicad()
    for project in OOMP.getItems("projects"):
        test = project.getTag("gitRepo").value
        test = "GO"
        if test != "":
            harvestProject(project,all=True)

def harvestProject(project,all=False,gitPull=False,copyBaseFiles=False,harvestEagle=False,harvestKicad=False,overwrite=False):
    oompID = project.getID()
    print("Harvesting Project: " + oompID)

    if all or gitPull:
        pass
        gitPullProject(project)
    if all or copyBaseFiles:
        pass
        copyBaseFilesProject(project)
    if all or harvestEagle:        
        pass
        harvestEagleProject(project,overwrite)
    if all or harvestKicad:
        pass
        harvestKicadProject(project,overwrite)

def gitPullProject(project):
    print("    Pulling or cloning project ")
    gitRepo = project.getTag("gitRepo").value
    if gitRepo == "":
        #raise Exception("No git repo for project")
        print("        No Git Repo Found SKIPPING")
    else:
        oomGitPull(gitRepo,"sourceFiles/git/")

def copyBaseFilesProject(project):
    print("    Copying Base Files ")
    type = "Board"
    filename = project.getTag("eagle" + type).value    
    outfile = outFile = project.getFilename(type + "Eagle")
    inFile = ""
    if filename != "":
        inFile = "sourceFiles/git/" + project.getTag("gitName").value + "/" + filename
    else:
        filename = project.getTag("kicad" + type).value
        if filename != "":
            inFile = "sourceFiles/git/" + project.getTag("gitName").value + "/" + filename
            outfile = outFile = project.getFilename(type + "Kicad")
            oomMakeDir(project.getFilename("dirKicad"))
        else:
            #raise Exception("No source board file found")
            print("        No Board File Found SKIPPING")
    if inFile != "":
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
            oomMakeDir(project.getFilename("dirKicad"))
        else:
            #raise Exception("No source board file found")
            print("        No Schematic File Found SKIPPING")
    if inFile != "":
        oomCopyFile(inFile,outFile)
    
def harvestEagleProject(project,overwrite=False):
    print("    Harvesting Eagle Files ")
    eagleBoardFile = project.getFilename("boardeagle")
    projectDir = project.getFolder()
    eagleBoardFileFull = project.getFilename("boardeagle",relative="full")
    OOMPproject.harvestEagleBoardFile(eagleBoardFile,projectDir,overwrite=overwrite)
    OOMPproject.harvestEagleSchematicFile(eagleBoardFile.replace("boardEagle.brd","schematicEagle.sch"),projectDir,overwrite=overwrite)
    #oomSendAltKey("x",delay=5)
    #oomSendAltKey("x",delay=5)

def harvestKicadProject(project,overwrite=False):
    print("    Harvesting Kicad Files ")
    ###### Convert to kicad
    kicadBoardFile = project.getFilename("boardkicad")    
    eagleBoardFile = project.getFilename("boardeagle")
    projectDir = project.getFolder()
    OOMPproject.harvestEagleBoardToKicad(eagleBoardFile,projectDir,overwrite=overwrite)
    OOMPproject.harvestEagleSchemToKicad(eagleBoardFile.replace("boardEagle.brd","schematicEagle.sch"),projectDir,overwrite=overwrite)
    ###### get files out of kicad
    OOMPproject.harvestKicadBoardFile(kicadBoardFile,projectDir,overwrite=overwrite)
    OOMPproject.harvestKicadSchemFile(kicadBoardFile,projectDir,overwrite=overwrite)
    ###### interactive BOM
    OOMPproject.makeInteractiveHtmlBom(project,overwrite)
    OOMPproject.makeInteractiveHtmlBomImages(project,overwrite)
    OOMPprojectParts.harvestParts(project,overwrite=overwrite)
    OOMPprojectParts.matchParts(project)
    for part in OOMP.getItems("parts"):
            part.exportTags("detailsInstancesOomp",["oompInstances"]) 
