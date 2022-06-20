import os
import random
import shutil
import time
from wsgiref.handlers import BaseCGIHandler

details = list()
parts = list()

baseDir = ""



def oompAddDetail(category,code,name,sort="",extra1="",extra2=""):
    details.append(oompDetail(category,code,name,sort,extra1="",extra2=""))

def getDetailFromCode(category,code):
    for x in details:
        if x.category == category:
            if x.code == code:
                return x
    return oompDetail("","","","")




def getParts():
    return parts

def getItems(type=""):
    rv = parts
    if type.upper() == "FOOTPRINTS":
        rv = []
        for part in parts:
            t = part.getTag("oompType")
            if t.value == "FOOTPRINT":
                rv.append(part)
    if type.upper() == "PARTS":
        rv = []
        for part in parts:
            t = part.getTag("oompType")
            if t.value == "TEMPLATE" or t.value == "FOOTPRINT" or t.value == "PROJ"  :
                c = "SKIP"
            else:
                rv.append(part)
    if type.upper() == "PROJECTS":
        rv = []
        for part in parts:
            t = part.getTag("oompType")
            if t.value == "PROJ":
                rv.append(part)
    if type.upper() == "TEMPLATES":
        rv = []
        for part in parts:
            t.value = part.getTag("oompType")
            if t == "TEMPLATE":
                rv.append(part)                
    return rv

def getPartByID(part):
##    print("     Get Part By ID: " + part)
    for x in parts:
        if x.getTag("oompID").value == part:
            return x     
    return oompItem("")

def getPartByHex(hexid):
##    print("     Get Part By ID: " + part)
    for x in parts:
        x.getTag("hexID").value
        if x.getTag("hexID").value == hexid:
            return x     
    return oompItem("")

def getPartByName(name):
##    print("     Get Part By ID: " + part)
    for x in parts:
        if x.getTag("name").value == name:
            return x     
    return oompItem("")    


def getDetailByCode(category, code):    
##    print("     Get Part By ID: " + code)
    for x in details:
        #print("    Matching: " + x.code + " with -- " + code)
        if x.code == code:
            return x     
    return oompDetail("","","","")


def printParts():
    print("OOMP Parts")
    for x in parts:
        b = 0
        #print("    Part: " + str(x.fullString()))
        oompID = x.getTag("oompID").value
        print("Loading: ", oompID)

def getNextIndex():
    return len(parts) + 1
        

def getAddTagLine(tagName,value):
    return 'newPart.addTag("' + tagName + '", "' + value + '")\n'


######  Directory routines

def setBaseDir(base):
    global baseDir
    baseDir = base 

def getDir(type, base=False):
    global baseDir
    rv = ""
    if base:
        rv = baseDir
    if type == "eda":
        rv = rv + "oomlout_OOMP_eda/"
    if type == "parts":
        rv = rv + "oomlout_OOMP_parts/"
    if type == "projects":
        rv = rv + "oomlout_OOMP_projects/"
    return rv


def getFileOpening(hexID="",type="",size="",color="",desc="",index=None,name=None):
    if index == None:
        index = getNextIndex()
    rv = ""

    rv = rv + "###### OOMP FILE  ######\n"
    rv = rv + "\n"
    rv = rv + "import OOMP\n"
    rv = rv + "\n"
    rv = rv + "newPart = OOMP.oompItem()\n"
    rv = rv + "\n"
    rv = rv + getAddTagLine("hexID",hexID)
    rv = rv + getAddTagLine("oompType",type)
    rv = rv + getAddTagLine("oompSize",size)
    rv = rv + getAddTagLine("oompColor",color)
    rv = rv + getAddTagLine("oompDesc",desc)
    rv = rv + getAddTagLine("oompIndex",index)

    if name != None:
        rv = rv + getAddTagLine("oompName",name)

    rv = rv + "\n"

    return rv

def getFileEnding():
    return 'OOMP.parts.append(newPart)' 


class oompItem:

    def __init__(self,index=None):
        if index == None:
            index = getNextIndex()
        self.tags=list()
        if index == 0:
            index = len(parts) + 1
        self.index=index
        self.addTag("index", index)

    def __str__(self):
        rv = ""
        rv = rv + self.getName()
        #for x in self.tags:
        #    rv = rv + "    " + str(x)
        return rv

    def fullString(self):
        rv = ""
        rv = rv + self.getName() + "\n"
        for x in self.tags:
            rv = rv + "" + str(x)
##            if not isinstance(x.value, list):
##                rv = rv + "    " + str(x)
##            else: #tag has a list
##                rv = rv + "    " + str(x) + "\n"
##                for y in x.value:
##                    if isinstance(y, list):
##                        rv = rv + "    " + str(y) + "\n"
##                        for c in y:
##                            rv = rv + "            " + str(c) + "\n"
##                    else:
##                        rv = rv + "        " + str(y) + "\n"
        return rv
    

    def getFolder(self):        
        rv = ""
        oompType = self.getTag("oompType").value
        oompSize = self.getTag("oompSize").value
        oompColor = self.getTag("oompColor").value
        oompDesc = self.getTag("oompDesc").value
        oompIndex = self.getTag("oompIndex").value
        oompID = self.getTag("oompID").value
        if oompType == "FOOTPRINT":
            rv = "oomlout_OOMP_eda/footprints/" + oompSize + "/" + oompColor + "/" + oompDesc + "/" + oompIndex + "/"
        elif oompType == "PROJ":
            rv = "oomlout_OOMP_projects/"  + oompID + "/" 
        else:
            rv = "oomlout_OOMP_parts/"  + oompID + "/" 

        return rv

    ##No longer used    
    def indexMd(self):
        oompID = self.getTag("oompID").value
        name = self.getTag("name").value
        rv = ""
        rv = rv + "![" + name + "](" + oompID + "/image_140.jpg) " + "[" + oompID + " > " + name + "](" + oompID + "/Readme.md)"        
        return rv

    ##No longer used
    def mdPage(self,file):
        oompID = item.getTag("oompID").value
        name = item.getTag("name").value
        with MarkdownGenerator(
            # By setting enable_write as False, content of the file is written
            # into buffer at first, instead of writing directly into the file
            # This enables for example the generation of table of contents
            filename=filename, enable_write=False
        ) as doc:
            header = oompID + ">" + name
            doc.addHeader(1, header)

            doc.writeTextLine(f'{doc.addBoldedText("This is just a test.")}')
            doc.addHeader(2, "Second level header.")
            table = [
                {"Column1": "col1row1 data", "Column2": "col2row1 data"},
                {"Column1": "col1row2 data", "Column2": "col2row2 data"},
            ]

            doc.addTable(dictionary_list=table)
            doc.writeTextLine("Ending the document....")

    def mdPageOld(self):        
        oompID = self.getTag("oompID").value
        name = self.getTag("name").value
        rv = ""
        rv = rv + "# " + oompID + " > " + name + "  \n"
        rv = rv + "![" + name + "](image_600.jpg)  \n"
        for x in self.tags:
            rv = rv + "" + x.getMD() + ""
        return rv
    
    def addTag(self,name,value):
        self.tags.append(oompTag(name,value))

    def addTagSupplied(self,name,value,tag):
        tag.append(oompTag(name,value))
        return tag

    def getTag(self,name):
        if name == "oompID":
            id = self.getTag("oompType").value + "-" +  self.getTag("oompSize").value + "-" +  self.getTag("oompColor").value + "-" +  self.getTag("oompDesc").value + "-" +  self.getTag("oompIndex").value
            return(oompTag("oompID", id))
        elif name == "taxaID":
            id = self.getTag("taxaDomain").value.upper() + "-" + self.getTag("taxaKingdom").value.upper() + "-" + self.getTag("taxaDivision").value.upper() + "-" + self.getTag("taxaClass").value.upper() + "-" + self.getTag("taxaOrder").value.upper() + "-" + self.getTag("taxaFamily").value.upper() + "-" + self.getTag("taxaGenus").value.upper() + "-" + self.getTag("taxaSpecies").value.upper()
            return(oompTag("oompID", id))
        #elif name == "hexID":
        #    hexValue = hex(self.getTag("index").value).replace("0x","").upper()
        #    return(oompTag("hexID",hexValue))
        elif name == "name":
            id = self.getTag("namename").value
            if id == "" or id == "XXXXX":
                name = ""
                #size
                value = getDetailFromCode("size",self.getTag("oompSize").value).name
                if value != "":
                    name = name + value + " "

                #desc
                value = getDetailFromCode("desc",self.getTag("oompDesc").value).name
                if value != "":
                    name = name + value + " "
                    
                #color
                value = getDetailFromCode("color",self.getTag("oompColor").value).name
                if value != "":
                    name = name + value + " "
                    
                #type
                value = getDetailFromCode("type",self.getTag("oompType").value).name
                if value != "":
                    name = name + value + " "
                    
                #index
                value = getDetailFromCode("index",self.getTag("oompIndex").value).name
                if value != "":
                    name = name + value + " "                      

                name = name.strip()
                return(oompTag("name", name))
            else:
                return self.getTag("namename")
        elif name == "footprintFolder":
            folder = getDir("eda") + "footprints/" + self.getTag("oompSize").value + "/" +  self.getTag("oompColor").value + "/" + self.getTag("oompDesc").value +"/" + self.getTag("oompIndex").value + "/"
            return(oompTag("footprintFolder",folder))
        else:
            if name == "namename":
                name = "name"
            for x in self.tags:
                if x.name == name:
                    return x
            return oompTag("","")

    def getTags(self,tagName):
        rv = []
        for tag in self.tags:
            if tag.name == tagName:
                rv.append(tag)
        return rv

    def getName(self):
        return "OOMP Item:    " + self.getTag("oompID").value + " " + self.getTag("name").value

    
class oompTag:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        if isinstance(self.value, list):
            rv = "oompTagCC " + self.name + "\n"
            for x in self.value:
                rv = rv + "    " + str(x) 
            return rv
        elif isinstance(self.value, oompTag):
            return "     " + self.name + "    \n" + str(self.value) + "\n"
        else:
            return "     " + str(self.name) + " : " + str(self.value)+ "\n"

    def getMD(self):
        if isinstance(self.value, list):
            rv = "oompTagCC " + self.name + "\n"
            for x in self.value:
                rv = rv + "" + str(x) 
            return rv
        elif isinstance(self.value, oompTag):
            return "" + self.name + "  \n" + str(self.value) + "  \n"
        else:
            return "" + str(self.name) + " : " + str(self.value)+ "  \n"
            

    def getValue(self):
        return self.value

class oompDetail:

    def __init__(self, category, code, name, sort="", extra1="", extra2=""):
        self.category = category
        self.code = code
        self.name = name
        self.sort = sort
        self.extra1 = extra1
        self.extra2 = extra2

    def __str__(self):
        return self.category + "   " + self.code  + "   " + self.name  + "   " + self.sort
    
#### import detail lists

import codes.OOMPdetailsType
import codes.OOMPdetailsSize
import codes.OOMPdetailsColor
import codes.OOMPdetailsDesc
import codes.OOMPdetailsIndex

def loadParts():
    files = os.listdir()

    ##for file in files:
    ##    if "TAXApart_" in file:
    ##        #print(file)
    ##        moduleName = file.replace(".py","")
    ##        __import__(moduleName)

    directory = "oomlout_OOMP_eda\\"
    loadDirectory(directory)
    directory = "oomlout_OOMP_parts\\"
    loadDirectory(directory)
    directory = "oomlout_OOMP_projects\\"
    loadDirectory(directory)

    directory = "templates\\diag\\"
    loadDirectory(directory, fileFilter = ".py")



def loadDirectory(directory,fileFilter="details.py"):
    testing = 1000000000000000000
    testing = 7000
    count = 0
    for subdir, dirs, files in os.walk(directory):
            if count > testing:
                print("Breaking " + str(count) + " " + str(testing))
                break
            for file in files:
                count = count + 1
                if count > testing:
                    print("Breaking " + str(count) + " " + str(testing))
                    break
                if(fileFilter in file):
                    moduleName = file.replace(".py","")
                    moduleName = subdir.replace("\\",".") + "." + moduleName
                    ##print("    moduleName: " + moduleName)
                    #print(".",end="")
                    try:
                        __import__(moduleName)    
                    except:
                        ###### For dealing with folders with a full stop
                        sourceFile = subdir + "/" + file
                        destFile = "sourceFiles/temp/" + str(random.randint(0,999999999)) + ".py"
                        moduleName = destFile.replace("\\",".").replace("/",".").replace(".py","")
                        shutil.copyfile(sourceFile,destFile)
                        time.sleep(0.01)
                        __import__(moduleName)   
                        os.remove(destFile) 


#### import parts
loadParts()
        
