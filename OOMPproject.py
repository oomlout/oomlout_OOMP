from oomBase import *
import OOMP
import os
import shutil

##################
######  Adafruit Section

def harvestProjectsAdafruit():
    srcDir = "oomlout_OOMP_projects\sourceFiles/adafruit/"
    print("Harvesting Adafruit!")
    directory = srcDir
    for dir in os.listdir(directory):
        if(os.path.isdir(directory)):
            print("    Harvesting: " + srcDir + dir)
            processProjectDirAdafruit(srcDir + dir + "/")
            

def processProjectDirAdafruit(directory):
    hardwareDir = directory 
    readmeFile = ""
    boardFile = ""
    schematicFile = ""
    licenseFile = ""
    index = 0
    ############ Finding Files
    ###### Test if it has a hardware path
    if os.path.isdir(hardwareDir):
        files = [f for f in os.listdir(directory)]
        #print(files)
        for file in files:
            name = directory.replace("oomlout_OOMP_projects\sourceFiles/sparkfun/","").replace("-"," ").replace("/","").replace("\\","")
            if file.lower() == "license.txt":
                #print("        Found License")
                licenseFile = directory+file
            if file.lower() == "readme.md":
                #print("        Found Readme")
                readme = oomReadFileToString(directory+file)
                readmeFile = directory+file
                index = stringBetween(readme,'href="http://www.adafruit.com/products/','">')
                if not index.isnumeric():                    
                    ###### for debugging skipped repositories
                    c=0    
                
                #print ("            Index: " + str(index))

        ###### Hardware Folder
        files = [f for f in os.listdir(hardwareDir)]   
        for file in files:
            #print(file)
            if ".brd" in file.lower():                
                #print("        Found Board")
                boardFile = hardwareDir+file
            if ".sch" in file.lower():
                #print("        Found Schematic")
                schematicFile = hardwareDir+file

        if index != 0 and index != "" and boardFile != "" and schematicFile != "" :
            ############ Making OOMP file
            oompType = "PROJ"
            oompSize = "ADAF"
            oompColor = str(index)
            oompDesc = "STAN"
            oompIndex = "01" 
            hexID = "PRA" + index   
            directory = "oomlout_OOMP_projects/" + oompType + "-"  + oompSize + "-"  + oompColor + "-"  + oompDesc + "-"  + oompIndex + "/"
            oomMakeDir(directory)  

            fileName = directory + "details.py"
            f = open(fileName,"w")
            name = name
            f.write(OOMP.getFileOpening(hexID,oompType,oompSize,oompColor,oompDesc,oompIndex,name))
            ###### extra details
            f.write(OOMP.getAddTagLine("sources","All source files from https://github.com/adafruit/" + name.replace(" ","-") + " (source licence details in srcLicense.md)"))
            f.write(OOMP.getAddTagLine("linkBuyPage","http://www.adafruit.com/products/" + str(index)))

            f.write("\n")
            f.write(OOMP.getFileEnding())
            f.close()


            ############ Moving Files
            if readmeFile != "":
                oomCopyFile(readmeFile, directory + "srcReadme.md")
            if boardFile != "":
                oomCopyFile(boardFile, directory + "boardEagle.brd")
            if schematicFile != "":            
                oomCopyFile(schematicFile, directory + "schematicEagle.sch")
            if licenseFile != "":    
                oomCopyFile(licenseFile, directory + "srcLicense.md")

    else:
        print("SKIPING")
    #delay(1)
                            
                                


##################
######  Sparkfun Section

def harvestProjectsSparkfun():
    srcDir = "oomlout_OOMP_projects\sourceFiles/sparkfun/"
    print("Harvesting Sparkfun!")
    directory = srcDir
    for dir in os.listdir(directory):
        if(os.path.isdir(directory)):
            print("    Harvesting: " + srcDir + dir)
            processProjectDirSparkfun(srcDir + dir + "/")
            

def processProjectDirSparkfun(directory):
    hardwareDir = directory + "Hardware/"
    hardwareDir2 = directory + "Hardware/Qwiic Micro/"
    readmeFile = ""
    boardFile = ""
    schematicFile = ""
    licenseFile = ""
    index = 0
    ############ Finding Files
    ###### Test if it has a hardware path
    if os.path.isdir(hardwareDir):
        files = [f for f in os.listdir(directory)]
        #print(files)
        for file in files:
            name = directory.replace("oomlout_OOMP_projects\sourceFiles/sparkfun/","").replace("_"," ").replace("/","").replace("\\","")
            if file.lower() == "license.md":
                print("        Found License")
                licenseFile = directory+file
            if file.lower() == "readme.md":
                print("        Found Readme")
                readme = oomReadFileToString(directory+file)
                readmeFile = directory+file
                index = stringBetween(readme,"https://www.sparkfun.com/products/",")")
                if not index.isnumeric():
                    index = stringBetween(readme,'href="https://www.sparkfun.com/products/','">')   
                if not index.isnumeric():
                    index = stringBetween(readme,'href="https://www.sparkfun.com/products/','">')   
                if not index.isnumeric():
                    ###### for debugging skipped repositories
                    c=0    
                
                print ("            Index: " + str(index))

        ###### Hardware Folder
        files = [f for f in os.listdir(hardwareDir)]   
        for file in files:
            print(file)
            if ".brd" in file.lower():                
                print("        Found Board")
                boardFile = hardwareDir+file
            if ".sch" in file.lower():
                print("        Found Schematic")
                schematicFile = hardwareDir+file
        ###### test for qwiic nested files   
        if index == "20170":
            c=0
        if os.path.isdir(hardwareDir2) and boardFile == "":
            files = [f for f in os.listdir(hardwareDir2)]   
            for file in files:
                print(file)
                if ".brd" in file.lower():                
                    print("        Found Board")
                    boardFile = hardwareDir2+file
                if ".sch" in file.lower():
                    print("        Found Schematic")
                    schematicFile = hardwareDir2+file                   

        if index != 0 and index != "" and boardFile != "" and schematicFile != "" :
            ############ Making OOMP file
            oompType = "PROJ"
            oompSize = "SPAR"
            oompColor = str(index)
            oompDesc = "STAN"
            oompIndex = "01" 
            hexID = "PRS" + index   
            directory = "oomlout_OOMP_projects/" + oompType + "-"  + oompSize + "-"  + oompColor + "-"  + oompDesc + "-"  + oompIndex + "/"
            oomMakeDir(directory)  

            fileName = directory + "details.py"
            f = open(fileName,"w")
            name = name
            f.write(OOMP.getFileOpening(hexID,oompType,oompSize,oompColor,oompDesc,oompIndex,name))
            ###### extra details
            f.write(OOMP.getAddTagLine("sources","All source files from https://github.com/sparkfun/" + name.replace(" ","_") + " (source licence details in srcLicense.md)"))
            f.write(OOMP.getAddTagLine("linkBuyPage","https://www.sparkfun.com/products/" + str(index)))

            f.write("\n")
            f.write(OOMP.getFileEnding())
            f.close()


            ############ Moving Files
            if readmeFile != "":
                oomCopyFile(readmeFile, directory + "srcReadme.md")
            if boardFile != "":
                oomCopyFile(boardFile, directory + "boardEagle.brd")
            if schematicFile != "":            
                oomCopyFile(schematicFile, directory + "schematicEagle.sch")
            if licenseFile != "":    
                oomCopyFile(licenseFile, directory + "srcLicense.md")

    else:
        print("SKIPING")
            #delay(1)
                            
                                