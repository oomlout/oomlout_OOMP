import OOMP
import OOMPscad
import OOMPdiagrams
import OOMPlabels
import OOMPsummaries
import OPSC as opsc
import os


import time


from PIL import Image
import os.path


def generateAll(labels=True,scads=True,renders=True,readmes=True,diagrams=True,diagRenders=True,images=True,overwrite=False):

    print("Generating for " + str(len(OOMP.parts)) + " items")
  

    if labels:
        print("     Generating Labels:")
        for item in OOMP.getItems("parts"):
            OOMPlabels.generateLabel(item,overwrite)

    if scads:
        print("     Generating SCADs:")
        for item in OOMP.getItems("parts"):
            OOMPscad.generateScad(item,renders,overwrite)
        for item in OOMP.getItems("projectss"):
            OOMPscad.generateScad(item,renders,overwrite)

    if readmes:
        print("     Generating Readmes:")
        OOMPsummaries.generateReadmeIndex()
        for item in OOMP.getItems():
            OOMPsummaries.generateReadme(item,overwrite)
    
    if diagrams or diagRenders:
        print("     Generating Diagrams:")
        for item in OOMP.getItems("parts"):
            OOMPdiagrams.generateDiagrams(item, diagrams=diagrams, renders=diagRenders,overwrite=overwrite)
        OOMPdiagrams.genAllDiagramsFile()

    if images:
        print("     Generating Image Resolutions:")
        for item in OOMP.getItems():
            generateResolutions(item,overwrite)

def generateItem(item, labels=True,scads=True,renders=True,readmes=True,diagrams=True,diagRenders=True,images=True):

    if labels:
        OOMPlabels.generateLabel(item)

    if scads:
        OOMPscad.generateScad(x,renders)

    if readmes:
        OOMPsummaries.generateReadme(item)
    
    if diagrams or diagRenders:
        OOMPdiagrams.generateDiagrams(item, diagrams=diagrams, renders=diagRenders)

    if images:
        generateResolutions(item)


def generateResolutions(item,overwrite=False):
    oompID = item.getTag("oompID").value
    if("FOOTPRINT" in oompID):
        images = ["image"]
        res = [140,450,600]        
        for image in images:
            for r in res:
                folder = item.getTag("footprintFolder").value
                fileName = folder +  image + ".png"
                outFile = folder + image + "_" + str(r) + ".png"
                basewidth = r
                #print("OUTFILE: " + outFile + "    " + str(os.path.isfile(outFile)) + "      " + str(overwrite))
                if not os.path.isfile(outFile) or overwrite:  
                    if os.path.isfile(fileName):  
                        print("Generating resolutions for (eda pngs): " + oompID) 
                        img = Image.open(fileName)
                        wpercent = (basewidth / float(img.size[0]))
                        hsize = int((float(img.size[1]) * float(wpercent)))
                        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
                        img.save(outFile)

    else:    
        images = ["image","image_RE","image_TOP","image_BOTTOM",]
        res = [140,450,600]
        
        for image in images:
            for r in res:
                fileName = OOMP.getDir("parts") + oompID + "\\" + image + ".jpg"
                outFile = OOMP.getDir("parts") + oompID + "\\" + image + "_" + str(r) + ".jpg"
                basewidth = r
                if not os.path.isfile(outFile) or overwrite:                      
                    if os.path.isfile(fileName):            
                        print("Generating resolutions for (parts jpg): " + oompID)
                        img = Image.open(fileName)
                        wpercent = (basewidth / float(img.size[0]))
                        hsize = int((float(img.size[1]) * float(wpercent)))
                        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
                        img.save(outFile)



