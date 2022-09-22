from email.errors import InvalidMultipartContentTransferEncodingDefect
import OOMP
from mdutils.mdutils import MdUtils
import os
from pathlib import Path
import math
from oomBase import *


def generateReadmeIndex():    
    filename = OOMP.getDir("parts") + "\\Readme.md"
    
    mdFile = MdUtils(file_name=filename,title="")
    mdFile.new_header(level=1,title="Parts")
    
    
    types = OOMP.getDetailsCategory("type")
    for type in types:
        parts = []
        #print("Type: " + type.code)
        for item in OOMP.getItems("parts"):      
            testType = item.getTag("oompType").value
            if type.code == testType:
                parts.append(item.indexMd())
        if len(parts) > 0:
            mdFile.new_header(level=2, title=type.code + " > " + type.name)        
            addDisplayTable(mdFile,parts,4)   
    mdFile.new_table_of_contents(table_title='Contents', depth=2)
    mdFile.create_md_file()     
    

def generateRedirect():
    redirectLimit = 10000
    print("Generating redirect file")
    fileNum = 1
    filename = "sourceFiles/redirects"
    f = open(filename + str(fileNum) + ".csv","w+")
    x = 0
    
    for item in OOMP.parts:
        oompID = item.getID()
        hexID = item.getHex()
        longLink = item.getFolder("github")
        try:
            if oompID != "":     
                f.write(longLink + "," + oompID.lower() + "\n")
            if hexID != "":            
                f.write(longLink + "," + hexID.lower() + "\n")
        except:
            print("ERROR" + str(item))
        x = x + 1
        if x % redirectLimit == 0:
            f.close()
            fileNum = fileNum + 1
            f = open(filename + str(fileNum) + ".csv","w+")
            print(".",end="")
    


def generateRedirectOld(item,overwrite=False):
    print("Generating redirect for: " +item.getID())
    replaceString = "%%ID%%"
    redirect = item.getFolder("github")
    templateFile = "templates/OOMP_redirect.tmpl.html"
    redirectFile = item.getFilename("redirect")
    redirectFileHex = item.getFilename("redirectHex")
    if overwrite or not os.path.isfile(redirectFile):
        oomFileSearchAndReplace(templateFile,redirectFile,replaceString,redirect)
        oomFileSearchAndReplace(templateFile,redirectFileHex,replaceString,redirect)

        
def generateReadme(item,overwrite=False):  
    baseDir = item.getFolder()
    oomMakeDir(baseDir)
    filename = item.getFilename("readme")
    if not os.path.isfile(filename) or overwrite:       
        mdFile = MdUtils(file_name=filename,title='')      
        ## Add main image
        addMainImage(item,mdFile)
        ###### Summary
        addSummary(item,mdFile)
        ######  Specific items
        type = item.getType()
        if type== "FOOTPRINT":
            generateReadmeFootprint(item, mdFile)
        elif type== "PROJ":
            generateReadmeProject(item, mdFile)
        elif type== "SYMBOL":
            generateReadmeProject(item, mdFile)
        else:
            generateReadmePart(item, mdFile)                
        ###### Images  
        addImages(item,mdFile)             
        ###### Tags
        addTags(item,mdFile)

        print("Writing Readme: " + item.getID())
        mdFile.create_md_file()

def generateReadmeFootprint(item,mdFile):  
    pass

def generateReadmeProject(item,mdFile):  
        ###### Schematic
        file = "schemEagle"
        filename = item.getFilename(file,extension="png", resolution="600",relative="flat")
        link = filename = item.getFilename(file,extension="png",relative="flat")
        if item.ifFileExists(file):
            addTitle(mdFile,title='Schematic',level=2)                   
            addImage(mdFile,filename,"schem",link)
        ###### PCB
        file = "eagleImage"
        filename = item.getFilename(file,extension="png", resolution="600",relative="flat")
        link = filename = item.getFilename(file,extension="png",relative="flat")
        if item.ifFileExists(file):
            addTitle(mdFile,title='PCB',level=2)                   
            addImage(mdFile,filename,"pcb",link)
        ###### Interactive BOM
        bomFilename = item.getFilename("bomInteractive")
        if os.path.isfile(bomFilename ):
            addTitle(mdFile,title="Interactive BOM", level=2)
            summary = []
            text = "ibom.html"
            link = item.getFilename("bomInteractive",relative="githubWeb")
            summary.append("Interactive BOM page: " + addLink(text,link))
            addList(mdFile,summary)
                  
        ###### 
        ###### OOMP Parts   
        partsTags = item.getTags("oompParts")
        
        if len(partsTags) > 0:
            title='OOMP Parts'
            mdFile.new_header(level=2, title=title)
            addOompPartTable(mdFile,item)


def generateReadmeSymbol(item,mdFile):  
    pass

def generateReadmePart(item,mdFile):  
    baseDir = OOMP.baseDir
    ###### Diagram        
    images = ['diagBBLS','diagDIAG','diagIDEN','diagSCHEM','diagSIMP']
    title='Diagrams'
    #addOompTable(mdFile,images,imageName,baseName,extension,title,baseDir)
    addOompTable(mdFile,images,title=title,version=2,item=item)
    ###### Datasheet
    if os.path.isfile(item.getFilename("datasheet")):
        mdFile.new_header(level=2, title="Datasheets")
        summary = []
        summary.append("Datasheet: " + "[datasheet.pdf](datasheet.pdf)")
        mdFile.new_list(summary)        
    ###### 3D Model
    images = ['']
    imageName = ['3D Model Ortho']
    extension = ".png"
    baseName = "3dmodel"
    title='3D Models'
    addOompTable(mdFile,images,imageName,baseName,extension,title,baseDir)        
    ###### Labels
    images = ["label-front","label-inventory","label-spec"]
    title='Labels'
    addOompTable(mdFile,images,title=title,version=2,item=item)     
    ###### EDA
    mdFile.new_header(level=2, title="EDA")
    ######  Footprints
    
    images = []
    imageName = []
    footprintTags = [['footprintKicad',"kicad"],['footprintEagle','eagle']]        
    for type in footprintTags:
        tags = item.getTags(type[0])   
        footprints = []    
        for tag in tags:
            footprint = tag.value            
            if footprint != "":                    
                #print("Footprint:" + footprint)
                linkPath = "https://github.com/oomlout/oomlout_OOMP_eda/tree/main/footprints/"+ type[1] + "/" + footprint + "/"
                #https://raw.githubusercontent.com/oomlout/oomlout_OOMP_eda/main/footprints/kicad/kicad-footprints/Connector_PinHeader_2.54mm/PinHeader_1x03_P2.54mm_Vertical/image.png
                imagePath="https://raw.githubusercontent.com/oomlout/oomlout_OOMP_eda/main/footprints/"+ type[1] + "/" + footprint + "/image_140.png"
                name = type[1] + "/" + footprint
                footprints.append(mdGetImage(image=imagePath,alt=name) + "<br> " + mdGetLink(text=name,link=linkPath))
                #mdFile.new_line(mdFile.new_inline_link(text=footprint,link=linkPath))
                #mdFile.new_line(mdFile.new_inline_image(text=footprint,path=imagePath))
    if len(footprints) > 0:
        mdFile.new_header(level=3, title="Footprints")
        addDisplayTable(mdFile,footprints,4)            
    #extension = ".png"
    #baseName = ""
    #title='Footprints'
    #addOompTable(mdFile,images,imageName,baseName,extension,title,baseDir="")   
    ######  Symbols      
    mdFile.new_header(level=3, title="Symbols")
    images = []
    imageName = []
    footprintTags = ['kicadSymbol','eagleSymbol','sparkfunSymbol','adafruitSymbol']        
    for tag in footprintTags:
        footprint = item.getTag(tag).value            
        if footprint != "":
            #print("Footprint:" + footprint)
            images.append("/eda/symbols/" + tag.replace("Symbol","") + "/" + footprint)
            imageName.append(tag + " " + footprint)
    extension = ".png"
    baseName = ""
    title='Footprints'
    addOompTable(mdFile,images,imageName,baseName,extension,title,baseDir="")   


#####################################################################################
####################################################################################
####################################################################################
######  Helper Routines

#https://github.com/didix21/mdutils

def addMainImage(item,mdFile):
    ######  Image work  
        mainImageTree=["image","kicadPcb3dFront","kicadPcb3dBack","kicadPcb3d"]
        imageList = []
        mainImage = ""
        ###### see which images exist
        for image in mainImageTree:
            if(item.ifFileExists(image,resolution="450", relative="")):
                mainImage = item.getFilename(image,resolution="450", relative="flat")
                imageList.append(image)
        if mainImage != "":        
            mdFile.new_line(mdFile.new_reference_image(text='', path=mainImage, reference_tag='im'))
        
def addSummary(item,mdFile):
    type = item.getTag("oompType").value
    oompID = item.getTag("oompID").value
    hexID = item.getTag("hexID").value
    name = item.getTag("name").value
    oompName = item.getTag("oompName").value
    title = hexID + " > " + name
    if type == "FOOTPRINT" or  type == "PROJ":
        title = hexID +  " > " + oompName
    mdFile.new_header(level=1, title=title)
    summary = []
    summary.append("ID: " + oompID)
    summary.append("Hex ID: " + hexID)
    summary.append("Name: " + name) 
    summary.append("Description: " + name) 
    summary.append("Long Link: " + addLink("http://oom.lt/" + oompID, "http://oom.lt/" + oompID))
    summary.append("Short Link: " + addLink("http://oom.lt/" + hexID, "http://oom.lt/" + hexID))
    mdFile.new_list(summary)

def addLink(text,link):
    return "[" + text + "](" + link + ")" 

def addList(mdFile,list):
    mdFile.new_list(list)    

def addImage(mdFile,filename,alt="",link=""):
    image = ""
    if link !="":
        image = addLink("!" + addLink(alt,filename),link)
    else:
        image = "!" + addLink(alt,filename)
    mdFile.new_line(image)

def addTitle(mdFile,title,level):
    mdFile.new_header(level=level, title=title)

def addImages(item, mdFile):
    images = item.getFilename("allImagesNames")
    title='Images'
    addOompTable(mdFile,images,title=title,version=2,item=item)

def addTags(item,mdFile):
    mdFile.new_header(level=2, title='Tags')
    tags = []    
    #print(item.fullString())
    for tag in item.tags:
        if tag.name != "index":
            tags.append(str(tag.name) + ": " + str(tag.value))
    mdFile.new_list(tags)        
    mdFile.new_table_of_contents(table_title='Contents', depth=2)


def addOompPartTable(mdFile,item):
    mdFile.new_line()

    partsTags = item.getTags("oompParts")
    rawTags = item.getTags("rawParts")
    parts = ["OOMP Parts"]
    for partTag in partsTags:
        p = partTag.value.split(",")[1]
        partIdentifier = partTag.value.split(",")[0]
        part = OOMP.getPartByID(p)
        id = part.getID()
        if id == "----":
            v = partIdentifier + " " + partTag.value
        else:
            name = part.getName()
            #text = mdGetImage(part.getFilename("image",extension="png", resolution="140",relative="githubweb"),alt=id) + " " + id + " " + name
            text = partIdentifier + " " + name
            link = part.getFilename("",relative="github")
            v = mdGetLink(text,link)
        #value = getOompPartLine(str(partsTags[c].value))
        if v != "":
            parts.append(v)

    columns = 1
    rows = len(parts)    
    cells = parts

    mdFile.new_table(columns=columns, rows=rows, text=cells, text_align='center')                           

def getOompPartLine(value):
    rv = ""
    values = value.split(",")
    #print("Values: " + str(values))
    oompID = values[0] 
    if "SKIP" in oompID:
        rv = ""
    else:
        rv = oompID
        part = OOMP.getPartByID(oompID)
        name = part.getTag("name").value
        if name != "":
            rv = part.mdLine(value)
        else:
            rv = value

    return rv


def addDisplayTable(mdFile,cells,width):
    mdFile.new_line()

    numCells = len(cells)
    rows = math.floor(numCells / width) + 1
    difference = rows * width - len(cells)

    for r in range(0,difference):
        cells.append("")

    #print("Table Test: " + str(len(cells)) + "    rows: " + str(rows)  + "    Cols: " + str(width))
    mdFile.new_table(columns=width, rows=rows, text=cells, text_align='center')                           


def addOompTable(mdFile,images,imageName="",baseName="",extension="",title="",baseDir="",version=1,item=""):
    if version == 1:
        addOompTableV1(mdFile,images,imageName,baseName,extension,title,baseDir)
    elif version == 2: 
        addOompTableV2(mdFile,images,title,item)

def addOompTableV2(mdFile,images,title,item):
        line1 = []
        line2 = []
        index = 0
        numImages = 0
        for image in images:  
            testFile =  item.getFilename(image,resolution=140)
            if item.ifFileExists(image,resolution=140) :
                #print("Test File: " + baseDir  + baseName +   image.replace("/eda","eda")  +  extension)
                line1.append(image)
                line2.append("[!["  + image + "](" + item.getFilename(image,relative="flat",resolution=140) + ")](" + item.getFilename(image,relative="flat") + ")")
        if len(line1) > 0:
            mdFile.new_header(level=2, title=title)
            mdFile.new_line()
            #print(line1)
            tableText = line1
            tableText.extend(line2)
            #print("Images " + oompID)
            #print(tableText)
            #print(line2)
            #print(len(line2))
            #print(len(tableText))
            mdFile.new_line()
            mdFile.new_table(columns=len(line2), rows=2, text=tableText, text_align='center')                       

def addOompTableV1(mdFile,images,imageName,baseName,extension,title,baseDir):
        line1 = []
        line2 = []
        index = 0
        numImages = 0
        for image in images:            
            #print("Test File: " + baseDir  + baseName +   image.replace("/eda","eda")  +  extension)
            if(os.path.isfile(baseDir + baseName + image.replace("/eda","eda") + extension)):
                line1.append(imageName[index])
                line2.append("[!["  + imageName[index] + "](" + baseName + image + extension + ")](" + baseName + image + extension + ")")
            index = index + 1
        #print("Images: " + str(len(images)) + " " + str(images))            
        #print("Line1: " + str(len(line1)) + " " + str(line1))            
        if len(line1) > 0:
            mdFile.new_header(level=2, title=title)
            mdFile.new_line()
            #print(line1)
            tableText = line1
            tableText.extend(line2)
            #print("Images " + oompID)
            #print(tableText)
            #print(line2)
            #print(len(line2))
            #print(len(tableText))
            mdFile.new_line()
            mdFile.new_table(columns=len(line2), rows=2, text=tableText, text_align='center')                       

def mdGetLink(text,link):
    return "[" + text + "](" + link + ")"

def mdGetImage(image,alt=""):
    return "![" + alt + "](" + image + ")"

def generateReadmeOLD(item):
    
    oompID = item.getTag("oompID").value
    outFile = "parts\\" + oompID + "\\Readme.md"
    if not "TEMPLATE" in oompID:
        f = open(outFile, "w")
        f.write(item.mdPage())
        f.close()
