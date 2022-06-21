from email.errors import InvalidMultipartContentTransferEncodingDefect
import OOMP
from mdutils.mdutils import MdUtils
import os
from pathlib import Path
import math

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
    name = item.getTag("name").value
    baseDir = item.getFolder()
    Path(baseDir).mkdir(parents=True, exist_ok=True)
    filename = baseDir + "Readme.md" 
    if not os.path.isfile(filename) or overwrite:
        title = name
        mdFile = MdUtils(file_name=filename,title='')
        mainImage="image.png"
        if(os.path.isfile(baseDir + mainImage)):
            mdFile.new_line(mdFile.new_reference_image(text='', path=mainImage, reference_tag='im'))
        ###### Summary
        mdFile.new_header(level=1, title=title)
        summary = []
        summary.append("ID: " + oompID)
        summary.append("Name: " + name) 
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
    name = item.getTag("name").value
    baseDir = item.getFolder()
    filename = baseDir + "Readme.md" 

    if not os.path.isfile(filename) or overwrite:
        title = oompID + ">" + name
        mdFile = MdUtils(file_name=filename,title=title)        
        mdFile.new_table_of_contents(table_title='Contents', depth=2)
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
        images = ['','_RE','_TOP','_BOTTOM']
        imageName = ['Main','Reference','Top','Bottom']
        extension = ".jpg"
        baseName = "image"
        title='Images'
        addOompTable(mdFile,images,imageName,baseName,extension,title,baseDir)
        ###### Diagram        
        images = ['BBLS','DIAG','IDEN','SCHEM','SIMP']
        imageName = ['Breadboard Layout','Diagram','Identifier','Schematic','Simple']
        extension = ".png"
        baseName = "diag"
        title='Diagrams'
        addOompTable(mdFile,images,imageName,baseName,extension,title,baseDir)
        ###### Datasheet
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
        images = ['-front','-inventory','-spec']
        imageName = ['Front', "Inventory", "Specifications"]        
        extension = ".png"
        baseName = "label"
        title='Labels'
        addOompTable(mdFile,images,imageName,baseName,extension,title,baseDir)        
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

def addOompTable(mdFile,images,imageName,baseName,extension,title,baseDir):
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
