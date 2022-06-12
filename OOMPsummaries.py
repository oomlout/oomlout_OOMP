import OOMP
from mdutils.mdutils import MdUtils
import os

def generateReadmeIndex():    
    outFile = "parts\\Readme.md"
    f = open(outFile, "w")
    for item in OOMP.parts:
        line = item.indexMd()
        if(not "TEMPLATE" in line):
            f.write(line + "  \n")

    f.close()

#https://github.com/didix21/mdutils
def generateReadme(item):
    oompID = item.getTag("oompID").value
    name = item.getTag("name").value
    if not "TEMPLATE" in oompID:
        baseDir = "parts\\" + oompID + "\\"
        filename = baseDir + "Readme.md" 
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
        ###### Tags
        mdFile.new_header(level=2, title='Tags')
        tags = []
        #print(item.fullString())
        for tag in item.tags:
            tags.append(str(tag.name) + ": " + str(tag.value))
        mdFile.new_list(tags)




        mdFile.new_table_of_contents(table_title='Contents', depth=2)
        mdFile.create_md_file()

def addOompTable(mdFile,images,imageName,baseName,extension,title,baseDir):
        line1 = []
        line2 = []
        index = 0
        numImages = 0
        for image in images:            
            if(os.path.isfile(baseDir + baseName + image + extension)):
                line1.append(imageName[index])
                line2.append("[!["  + imageName[index] + "](" + baseName + image + extension + ")](" + baseName + image + extension + ")")
            index = index + 1
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

def generateReadmeOLD(item):
    
    oompID = item.getTag("oompID").value
    outFile = "parts\\" + oompID + "\\Readme.md"
    if not "TEMPLATE" in oompID:
        f = open(outFile, "w")
        f.write(item.mdPage())
        f.close()
