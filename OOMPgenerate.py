import OOMP
import OOMPscad
import OOMPdiagrams
import OOMPjson
import OOMPlabels
import OOMPsummaries
import OPSC as opsc
import os


import time


from PIL import Image
import os.path


def generateAll(filter="all",labels=True,scads=True,renders=True,readmes=True,diagrams=True,diagRenders=True,images=True,json=False,overwrite=False):

    print("Generating for " + str(len(OOMP.parts)) + " items")
  

    if labels:
        print("     Generating Labels:")
        if filter == "all" or filter == "parts":
            for item in OOMP.getItems("parts"):
                OOMPlabels.generateLabel(item,overwrite)

    if scads:        
        if filter == "all" or filter == "parts":
            print("     Generating SCADs: Parts")
            for item in OOMP.getItems("parts"):
                OOMPscad.generateScad(item,renders,overwrite)
        if filter == "all" or filter == "projects":                
            print("     Generating SCADs: Projects")
            for item in OOMP.getItems("projects"):
                OOMPscad.generateScad(item,renders,overwrite)

    if readmes:
        print("     Generating Readmes:")
        
        if filter == "all":
            OOMPsummaries.generateReadmeIndex()
            for item in OOMP.getItems():
                OOMPsummaries.generateReadme(item,overwrite)
        if filter == "parts":
            OOMPsummaries.generateReadmeIndex()
            for item in OOMP.getItems("parts"):
                OOMPsummaries.generateReadme(item,overwrite)
        if filter == "projects":
            for item in OOMP.getItems("projects"):
                OOMPsummaries.generateReadme(item,overwrite)
        if filter == "footprints":
            for item in OOMP.getItems("footprints"):
                OOMPsummaries.generateReadme(item,overwrite)
    if json:
        print("     Generating jsons:")
        if filter == "all" or filter == "footprints":
            for item in OOMP.getItems("footprints"):
                OOMPjson.generateJson(item,overwrite)
        if filter == "all" or filter == "parts":        
            for item in OOMP.getItems("parts"):
                OOMPjson.generateJson(item,overwrite)
        if filter == "all" or filter == "projects":        
            for item in OOMP.getItems("projects"):
                OOMPjson.generateJson(item,overwrite)

    if diagrams or diagRenders:
        
        if filter == "all" or filter == "parts":
            print("     Generating Diagrams: " + filter)
            for item in OOMP.getItems("parts"):
                OOMPdiagrams.generateDiagrams(item, diagrams=diagrams, renders=diagRenders,overwrite=overwrite)
            OOMPdiagrams.genAllDiagramsFile()

    if images:
        
        if filter == "all":
            print("     Generating Image Resolutions: All")
            for item in OOMP.getItems():
                generateResolutions(item,overwrite)
        if filter == "parts":        
            print("     Generating Image Resolutions: Parts")
            for item in OOMP.getItems("parts"):
                generateResolutions(item,overwrite)
        if filter == "projects":        
            print("     Generating Image Resolutions: Projects")
            for item in OOMP.getItems("projects"):
                generateResolutions(item,overwrite)
        if filter == "footprints":        
            print("     Generating Image Resolutions: Footprints")
            for item in OOMP.getItems("footprints"):
                generateResolutions(item,overwrite)

def generateItem(item, labels=True,scads=True,renders=True,readmes=True,diagrams=True,diagRenders=True,images=True,json=False,overwrite=False):

    if labels:
        OOMPlabels.generateLabel(item,overwrite=overwrite)

    if scads:
        OOMPscad.generateScad(x,renders,overwrite=overwrite)

    if readmes:
        OOMPsummaries.generateReadme(item,overwrite=overwrite)
    
    if json:
        OOMPjson.generateJson(item,overwrite=overwrite)

    if diagrams or diagRenders:
        OOMPdiagrams.generateDiagrams(item, diagrams=diagrams, renders=diagRenders,overwrite=overwrite)

    if images:
        generateResolutions(item,overwrite=overwrite)


def generateResolutions(item,overwrite=False):
    oompID = item.getTag("oompID").value
    if("FOOTPRINT" in oompID):
        images = ["image","kicadPcb3d","kicadPcb3dBack","kicadPcb3dFront","image_RE","image_TOP","image_BOTTOM"]
        res = [140,450,600]        
        for image in images:
            for r in res:
                folder = item.getTag("footprintFolder").value
                fileNamePng = folder +  image + ".png"
                outFilePng = folder + image + "_" + str(r) + ".png"
                fileNameJpg = folder +  image + ".jpg"
                outFileJpg = folder + image + "_" + str(r) + ".jpg"
                basewidth = r
                #print("OUTFILE: " + outFile + "    " + str(os.path.isfile(outFile)) + "      " + str(overwrite))
                if not os.path.isfile(outFilePng) or overwrite:                      
                    if os.path.isfile(fileNamePng):  
                        print("        Generating: " + outFilePng)
                        img = Image.open(fileNamePng)
                        wpercent = (basewidth / float(img.size[0]))
                        hsize = int((float(img.size[1]) * float(wpercent)))
                        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
                        img.save(outFilePng)
                if not os.path.isfile(outFileJpg) or overwrite:  
                    if os.path.isfile(fileNameJpg):  
                        print("        Generating: " + outFileJpg)
                        img = Image.open(fileNameJpg)
                        wpercent = (basewidth / float(img.size[0]))
                        hsize = int((float(img.size[1]) * float(wpercent)))
                        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
                        img.save(outFileJpg)
    


