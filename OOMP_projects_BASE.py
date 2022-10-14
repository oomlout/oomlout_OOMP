import OOMP
import OOMPproject
import OOMPprojectParts
from oomBase import *

import OOMP_projects_partsMatch

######  Company Files
import OOMP_projects_ADAF
import OOMP_projects_ELLA
import OOMP_projects_IBBC
import OOMP_projects_SEED
import OOMP_projects_SIRB
import OOMP_projects_SOPA
import OOMP_projects_SPAR

def createAllProjects():
    #OOMP_projects_IBBC.createProjects()
    #OOMP_projects_ADAF.createProjects()    
    #OOMP_projects_ELLA.createProjects()
    #OOMP_projects_SEED.createProjects()
    #OOMP_projects_SIRB.createProjects()
    #OOMP_projects_SOPA.createProjects()
    OOMP_projects_SPAR.createProjects()

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

def makeProjectNew(d):
    type = d["oompType"]
    size = d["oompSize"]


    color = str(d["count"]).zfill(4)
    desc = "STAN"
    index = "01"
    try:
        index = d["oompIndex"]
    except:
        pass


    hexID = "PR" + type[0:2] + str(d["count"])

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

    extraTags = []
    tagString = ""
    extraTags.append(OOMP.oompTag("name",d["name"]))
    extraTags.append(OOMP.oompTag("gitRepo",d["github"] + d["repo"]))
    extraTags.append(OOMP.oompTag("gitName",d["repo"]))
    if d["format"].lower() == "eagle":
        extraTags.append(OOMP.oompTag("eagleBoard",d["file"] + ".brd"))
        extraTags.append(OOMP.oompTag("eagleSchem",d["file"] + ".sch"))
    elif d["format"].lower() == "kicad":
        extraTags.append(OOMP.oompTag("kicadBoard",d["file"] + ".kicad_pcb"))
        extraTags.append(OOMP.oompTag("kicadSchem",d["file"] + ".kicad_sch"))

    for tag in extraTags:
        tagString = tagString + tag.getPythonLine() + "\n"

    contents = contents.replace("EXTRAZZ",tagString)

    oomWriteToFile(outputFile,contents)

def harvestProjects(filter="",exclusions="NONE"):
    neverString = "nnmmkjkjoijlknlkzzzz"
    if exclusions = "NONE":
        exclusions= neverString
    oomLaunchKicad()
    for project in OOMP.getItems("projects"):
        oompID = project.getID()
        test = project.getTag("gitRepo").value
        test =  "GO"
        skip = ["PROJ-SEED-20054-STAN-01"]
        if test != "" and oompID not in skip:
            testID = project.getID()
            if filter in testID and exclusions not in testID:

                harvestProject(project,all=True)
    for part in OOMP.getItems("parts"):
        part.exportTags("detailsInstancesOomp",["oompInstances"]) 
   

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
        print("        No Git Repo Found")
        #raise Exception("No git repo for project")
    else:
        oomGitPull(gitRepo,"sourceFiles/git/", pause=False)

def copyBaseFilesProject(project):
    print("    Copying Base Files ")
    type = "Board"
    filename = project.getTag("eagle" + type).value    
    outFile = project.getFilename(type + "Eagle")
    outDir = ""
    inFile = ""
    if filename != "":
        inFile = "sourceFiles/git/" + project.getTag("gitName").value + "/" + filename
    else:
        filename = project.getTag("kicad" + type).value
        if filename != "":
            inFile = "sourceFiles/git/" + project.getTag("gitName").value + "/" + filename
            outFile = project.getFilename(type + "Kicad")
            outDir = project.getFilename("dirkicad")
        else:
            #raise Exception("No source board file found")
            print("        No Board File Found")
    if os.path.exists(inFile):
        if outDir != "":
            oomMakeDir(outDir)
        oomCopyFile(inFile,outFile)


    type = "Schem"
    filename = project.getTag("eagle" + type).value    
    outFile = project.getFilename(type + "Eagle")
    outDir = ""
    if filename != "":
        inFile = "sourceFiles/git/" + project.getTag("gitName").value + "/" + filename
    else:
        filename = project.getTag("kicad" + type).value
        if filename != "":
            inFile = "sourceFiles/git/" + project.getTag("gitName").value + "/" + filename
            outFile = project.getFilename(type + "Kicad")
            outDir = project.getFilename("dirkicad")
        else:
            #raise Exception("No source board file found")
            print("        No Schematic File Found")
    if os.path.exists(inFile):
        if outDir != "":
            oomMakeDir(outDir)
 
  
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
    kicadSchemFile = project.getFilename("schemkicad")    
    eagleBoardFile = project.getFilename("boardeagle")
    eagleSchemFile = project.getFilename("schemeagle")
    
    projectDir = project.getFolder()
    OOMPproject.harvestEagleBoardToKicad(eagleBoardFile,projectDir,overwrite=overwrite)
    OOMPproject.harvestEagleSchemToKicad(eagleSchemFile,projectDir,overwrite=overwrite)
    ###### get files out
    #  of kicad
    OOMPproject.harvestKicadBoardFile(kicadBoardFile,projectDir,overwrite=overwrite)
    OOMPproject.harvestKicadSchemFile(kicadSchemFile,projectDir,overwrite=overwrite)
    ###### interactive BOM
    OOMPproject.makeInteractiveHtmlBom(project,overwrite)
    ###### currently broken for kicad files
    if os.path.exists(eagleBoardFile):
        OOMPproject.makeInteractiveHtmlBomImages(project,overwrite)
    OOMPprojectParts.harvestParts(project,overwrite=overwrite)
    OOMP_projects_partsMatch.matchParts(project)

    OOMPproject.renderPcbDraw(project,overwrite)
    if False:
        for part in OOMP.getItems("parts"):
                part.exportTags("detailsInstancesOomp",["oompInstances"]) 
