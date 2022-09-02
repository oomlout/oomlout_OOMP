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


def generateAll(filter="all",labels=False,scads=False,renders=False,readmes=False,diagrams=False,diagRenders=False,images=False,json=False,redirects=False,overwrite=False):

    print("Generating for " + str(len(OOMP.parts)) + " items")
  

    if labels:
        print("     Generating Labels:")
        if filter == "all" or filter == "parts":
            for item in OOMP.getItems("parts",cache=True):
                OOMPlabels.generateLabel(item,overwrite)

    if scads:        
        print("     Generating SCADs: Parts")
        for item in OOMP.getItems(filter,cache=True):
            OOMPscad.generateScad(item,renders,overwrite)

    if redirects:
        for item in OOMP.getItems(cache=True):
            OOMPsummaries.generateRedirect(item,overwrite) 


    if readmes:
        print("     Generating Readmes:")
        OOMPsummaries.generateReadmeIndex()
        for item in OOMP.getItems(filter,cache=True):
            OOMPsummaries.generateReadme(item,overwrite)

    if json:
        print("     Generating jsons:")
        for item in OOMP.getItems(filter,cache=True):
                OOMPjson.generateJson(item,overwrite)

    if diagrams or diagRenders:
        
        if filter == "all" or filter == "parts":
            print("     Generating Diagrams: " + filter)
            for item in OOMP.getItems("parts",cache=True):
                OOMPdiagrams.generateDiagrams(item, diagrams=diagrams, renders=diagRenders,overwrite=overwrite)
            OOMPdiagrams.genAllDiagramsFile()

    if images:
        print("     Generating Image Resolutions: All")
        for item in OOMP.getItems(filter,cache=True):
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
    #if("FOOTPRINT" in oompID):
    if True:
        images = ["image","kicadPcb3d","kicadPcb3dBack","kicadPcb3dFront","image_RE","image_TOP","image_BOTTOM","eagleImage"]
        res = [140,450,600]        
        for image in images:
            for r in res:
                folder = item.getFolder()
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
    


