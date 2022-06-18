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


def generateAll(labels=True,scads=True,renders=True,readmes=True,diagrams=True,diagRenders=True,images=True):

    print("Generating for " + str(len(OOMP.parts)) + " items")

    if labels:
        for item in OOMP.parts:
            OOMPlabels.generateLabel(item)

    if scads:
            for item in OOMP.parts:
                OOMPscad.generateScad(item,renders)

    if readmes:
        print("     Generating Readmes:")
        OOMPsummaries.generateReadmeIndex()
        for item in OOMP.parts:
            print(".",end="")
            OOMPsummaries.generateReadme(item)
    
    if diagrams or diagRenders:
        print("     Generating Diagrams:")
        for item in OOMP.parts:
            OOMPdiagrams.generateDiagrams(item, diagrams=diagrams, renders=diagRenders)

    if images:
        for item in OOMP.parts:
            generateResolutions(item)

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


def generateResolutions(item):
    oompID = item.getTag("oompID").value
    images = ["image","image_RE","image_TOP","image_BOTTOM",]
    res = [140,450,600]
    print("Generating resolutions for: " + oompID)
    for image in images:
        for r in res:
            fileName = "parts\\" + oompID + "\\" + image + ".jpg"
            outFile = "parts\\" + oompID + "\\" + image + "_" + str(r) + ".jpg"
            basewidth = r
            if os.path.isfile(fileName):            
                img = Image.open(fileName)
                wpercent = (basewidth / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                img = img.resize((basewidth, hsize), Image.ANTIALIAS)
                img.save(outFile)



