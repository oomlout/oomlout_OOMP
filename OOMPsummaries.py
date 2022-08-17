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
    

def generateRedirect(item,overwrite=False):
    replaceString = "%%ID%%"
    redirect = item.getFolder("github")
    templateFile = "templates/OOMP_redirect.tmpl.html"
    redirectFile = item.getFilename("redirect")
    redirectFileHex = item.getFilename("redirectHex")
    if overwrite or not os.path.isfile(redirectFile):
        oomFileSearchAndReplace(templateFile,redirectFile,replaceString,redirect)
        oomFileSearchAndReplace(templateFile,redirectFileHex,replaceString,redirect)

#https://github.com/didix21/mdutils
def generateReadme(item,overwrite=False):
    oompID = item.getTag("oompID").value
    if "FOOTPRINT" in oompID:
        generateReadmeFootprint(item,overwrite)
    elif "PROJ" in oompID:
        generateReadmeProject(item,overwrite)
    elif not "TEMPLATE" in oompID:
        generateReadmePart(item,overwrite)

def generateReadmeFootprint(item,overwrite=False):  
    oompID = item.getTag("oompID").value
    hexID = item.getTag("hexID").value
    name = item.getTag("name").value
    oompName = item.getTag("oompName").value
    description = item.getTag("description").value
    baseDir = item.getFolder()
    Path(baseDir).mkdir(parents=True, exist_ok=True)
    filename = baseDir + "Readme.md" 
    if not os.path.isfile(filename) or overwrite:
        title = hexID + ">" + oompName
        mdFile = MdUtils(file_name=filename,title='')      
        ######  Image work  
        mainImageTree=["image","kicadPcb3dFront","kicadPcb3dBack","kicadPcb3d"]
        imageList = []
        mainImage = ""
        ###### see which images exist
        for image in mainImageTree:
            imagePath = item.getFilename(image,resolution="450", relative="")
            if(os.path.isfile(imagePath)):
                mainImage = item.getFilename(image,resolution="450", relative="flat")
                imageList.append(image)
        ## Add main image
        if mainImage != "":        
            mdFile.new_line(mdFile.new_reference_image(text='', path=mainImage, reference_tag='im'))
        ###### Summary
        mdFile.new_header(level=1, title=title)
        summary = []
        summary.append("ID: " + oompID)
        summary.append("Hex ID: " + hexID)
        summary.append("Name: " + name) 
        summary.append("Description: " + name) 
        mdFile.new_list(summary)
        ###### Images   
        images = imageList
        title='Images'
        addOompTable(mdFile,images,title=title,version=2,item=item)
        ###### Tags
        mdFile.new_header(level=2, title='Tags')
        tags = []    
        #print(item.fullString())
        for tag in item.tags:
            if tag.name != "index":
                tags.append(str(tag.name) + ": " + str(tag.value))
        mdFile.new_list(tags)        
        mdFile.new_table_of_contents(table_title='Contents', depth=2)
            
        #print("Writing readme: " + filename)    
        mdFile.create_md_file()

def generateReadmeProject(item,overwrite=False):
    oompID = item.getTag("oompID").value
    hexID = item.getTag("hexID").value
    name = item.getTag("name").value
    oompName = item.getTag("oompName").value
    description = item.getTag("description").value
    baseDir = item.getFolder()
    Path(baseDir).mkdir(parents=True, exist_ok=True)
    filename = baseDir + "Readme.md" 
    if not os.path.isfile(filename) or overwrite:
        title = oompID + ">" + oompName
        mdFile = MdUtils(file_name=filename,title='')      
        ######  Image work  
        mainImageTree=["eagleImage","image","kicadPcb3dFront","kicadPcb3dBack","kicadPcb3d"]
        imageList = []
        mainImage = ""
        ###### see which images exist
        for image in mainImageTree:
            imagePath = item.getFilename(image,resolution="450", relative="")
            if(os.path.isfile(imagePath)):
                mainImage = item.getFilename(image,resolution="450", relative="flat")
                imageList.append(image)
        ## Add main image
        if mainImage != "":        
            mdFile.new_line(mdFile.new_reference_image(text='', path=mainImage, reference_tag='im'))
        ###### Summary
        mdFile.new_header(level=1, title=title)
        summary = []
        summary.append("ID: " + oompID)
        summary.append("Hex ID: " + hexID)
        summary.append("Name: " + oompName) 
        summary.append("Description: " + description) 
        mdFile.new_list(summary)
        ###### Images   
        images = imageList
        title='Images'
        addOompTable(mdFile,images,title=title,version=2,item=item)
        ###### Interactive BOM
        bomFilename = item.getFilename("bomInteractive")
        if os.path.isfile(bomFilename ):
            mdFile.new_header(level=2, title="Interactive BOM")
            summary = []
            summary.append("Interactive BOM page: " + "[ibom.html](" + item.getFilename("bomInteractive",relative="flat") + ")")
            mdFile.new_list(summary)  
        ###### Tags
        mdFile.new_header(level=2, title='Tags')
        tags = []    
        #print(item.fullString())
        for tag in item.tags:
            if tag.name != "index":
                tags.append(str(tag.name) + ": " + str(tag.value))
        mdFile.new_list(tags)        
        mdFile.new_table_of_contents(table_title='Contents', depth=2)
            
        #print("Writing readme: " + filename)    
        mdFile.create_md_file()


def generateReadmePart(item,overwrite=False):    
    oompID = item.getTag("oompID").value
    name = item.getTag("name").value
    baseDir = item.getFolder()
    filename = baseDir + "Readme.md" 
    print(oompID)
    if oompID == "RESE-0603-X--67":
        c=0
    if not os.path.isfile(filename) or overwrite:
        title = oompID + ">" + name
        mdFile = MdUtils(file_name=filename,title='')
        ######  Image work  
        mainImageTree=["image","image_RE","image_TOP","image_BOTTOM"]
        imageList = []
        mainImage = ""
        ###### see which images exist
        for image in mainImageTree:
            imagePath = item.getFilename(image,resolution="450", relative="")
            if(os.path.isfile(imagePath)):
                mainImage = item.getFilename(image,resolution="450", relative="flat")
                imageList.append(image)


        mainImage="image_600.jpg"
        if(os.path.isfile(baseDir + mainImage)):
            mdFile.new_line(mdFile.new_reference_image(text='', path=mainImage, reference_tag='im'))
        ###### Summary
        mdFile.new_header(level=1, title=title)
        summary = []
        summary.append("ID: " + oompID)
        summary.append("Name: " + oompID)        
        mdFile.new_list(summary)
        ###### Images   
        images = imageList
        title='Images'
        addOompTable(mdFile,images,title=title,version=2,item=item)
        ###### Diagram        
        images = ['BBLS','DIAG','IDEN','SCHEM','SIMP']
        imageName = ['Breadboard Layout','Diagram','Identifier','Schematic','Simple']
        extension = ".png"
        baseName = "diag"
        title='Diagrams'
        addOompTable(mdFile,images,imageName,baseName,extension,title,baseDir)
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
        ###### Tags
        mdFile.new_header(level=2, title='Tags')
        tags = []
        
        #print(item.fullString())
        for tag in item.tags:
            
            if tag.name != "index":
                tags.append(str(tag.name) + ": " + str(tag.value))
        mdFile.new_list(tags)




        mdFile.new_table_of_contents(table_title='Contents', depth=3)
        try:
            mdFile.create_md_file()
        except:
            c=0

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
            #print("Test File: " + baseDir  + baseName +   image.replace("/eda","eda")  +  extension)
            line1.append(image)
            line2.append("[!["  + image + "](" + item.getFilename(image,relative="flat",resolution=140,extension="png") + ")](" + item.getFilename(image,relative="flat",resolution=600,extension="png") + ")")
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
