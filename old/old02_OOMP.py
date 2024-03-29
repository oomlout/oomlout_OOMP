import os
import random
import shutil
import time
from wsgiref.handlers import BaseCGIHandler
import pickle 




baseDir = ""



def oompAddDetail(category,code,name,sort="",extra1="",extra2=""):
    details.append(oompDetail(category,code,name,sort,extra1="",extra2=""))

def getDetailFromCode(category,code):
    """
    for x in details:
        if x.category == category:
            if x.code == code:
                return x
    return oompDetail("","","","")
    """
    try:
        rv = details[category + "-" + code]
    except KeyError:
        rv = oompDetail("","","","")
    return rv

def getDetailsCategory(category=""):
    rv = []
    for detail in details:
        if category in detail.category:
            rv.append(detail)
    return rv



def getParts():
    return parts

def getItems(type="",cache=False):
    global parts, partsFootprints, partsParts, partsNoFootprints, partsProjects, partsTemplates, partsSymbols
    if type == "load":
        getItems("footprints",cache=False)
        getItems("symbols",cache=False)
        getItems("parts",cache=False)
        getItems("nofootprints",cache=False)
        getItems("projects",cache=False)
        getItems("templates",cache=False)        
    if not cache:
        rv = parts
        if type.upper() == "FOOTPRINTS":
            rv = []
            for part in parts:
                t = part.getTag("oompType")
                if t.value == "FOOTPRINT":
                    rv.append(part)
            partsFootprints = rv
        if type.upper() == "SYMBOLS":
            rv = []
            for part in parts:
                t = part.getTag("oompType")
                if t.value == "SYMBOL":
                    rv.append(part)
            partsSymbols = rv
        if type.upper() == "PARTS":
            rv = []
            for part in parts:
                t = part.getTag("oompType")
                if t.value == "TEMPLATE" or t.value == "FOOTPRINT" or t.value == "SYMBOL" or t.value == "PROJ"  :
                    c = "SKIP"
                else:
                    rv.append(part)
            partsParts = rv
        if type.upper() == "NOFOOTPRINTS":
            rv = []
            for part in parts:
                t = part.getTag("oompType")
                if not t.value == "FOOTPRINT" and not t.value == "TEMPLATE":
                    rv.append(part)
                else:
                    c = "SKIP"
            partsNoFootprints = rv        
        if type.upper() == "PROJECTS":
            rv = []
            for part in parts:
                t = part.getTag("oompType")
                if t.value == "PROJ":
                    rv.append(part)
            partsProjects = rv
        if type.upper() == "TEMPLATES":
            rv = []
            for part in parts:
                t = part.getTag("oompType")
                if t == "TEMPLATE":
                    rv.append(part)                
            partsTemplates = rv
    else:
        rv = parts
        if type.upper() == "FOOTPRINTS":
            rv = partsFootprints
        if type.upper() == "SYMBOLS":
            rv = partsSymbols
        if type.upper() == "PARTS":
            rv = partsParts
        if type.upper() == "NOFOOTPRINTS":
            rv = partsNoFootprints
        if type.upper() == "PROJECTS":
            rv = partsProjects
        if type.upper() == "TEMPLATES":
            rv = partsTemplates
    return rv

def getPartByID(part):
##    print("     Get Part By ID: " + part)
    try:
        rv = parts[part]
    except KeyError:
        rv = oompItem()
    return rv

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
        

def getAddTagLine(tagName,value,quotes="single"):
    if quotes == "single":
        return 'newPart.addTag("' + tagName + '", "' + value + '")\n'
    elif quotes == "triple":
        return 'newPart.addTag("' + tagName + '", """' + value + '""")\n'


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
    rv = rv + "import OOMPtags\n"    
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


class oompDict(dict):
    def __init__(self,index=None):
        self.__dict__ = {}
    
    def append(self,newPart):
        oompID = newPart.getTag("oompID").value
        self.__dict__[oompID] = newPart

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __iter__(self):
        return iter(self.values())

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()        
     

class oompDetailDict(dict):
    def __init__(self,index=None):
        self.__dict__ = {}

    def append(self,newDetail):
        detailID = newDetail.category + "-" + newDetail.code
        self.__dict__[detailID] = newDetail


    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __iter__(self):
        return iter(self.values())

    def __repr__(self):
        return repr(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __delitem__(self, key):
        del self.__dict__[key]

    def clear(self):
        return self.__dict__.clear()

    def copy(self):
        return self.__dict__.copy()

    def has_key(self, k):
        return k in self.__dict__

    def update(self, *args, **kwargs):
        return self.__dict__.update(*args, **kwargs)

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

class oompItem:

    def __init__(self,index=None):
        if index == None:
            index = getNextIndex()
        self.tags=list()
        if index == 0:
            index = len(parts) + 1
        #self.index=index
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
    
    def getDir(self):  
        return self.getFolder()

    def getFolder(self,style=""):        
        rv = ""
        oompType = self.getTag("oompType").value
        oompSize = self.getTag("oompSize").value
        oompColor = self.getTag("oompColor").value
        oompDesc = self.getTag("oompDesc").value
        oompIndex = self.getTag("oompIndex").value
        oompID = self.getTag("oompID").value
        if style == "":
            if oompType == "FOOTPRINT":
                rv = "oomlout_OOMP_eda/footprints/" + oompSize + "/" + oompColor + "/" + oompDesc + "/" + oompIndex.replace(":","-").replace("\\","-").replace("/","-") + "/"
            if oompType == "SYMBOL":
                rv = "oomlout_OOMP_eda/symbols/" + oompSize + "/" + oompColor + "/" + oompDesc + "/" + oompIndex.replace(":","-").replace("\\","-").replace("/","-") + "/"
            elif oompType == "PROJ":
                rv = "oomlout_OOMP_projects/"  + oompID + "/" 
            else:
                rv = "oomlout_OOMP_parts/"  + oompID + "/" 
        elif style == "github":

            if oompType == "FOOTPRINT":
                rv = "https://github.com/oomlout/oomlout_OOMP_eda/tree/main/footprints/" + oompSize + "/" + oompColor + "/" + oompDesc + "/" + oompIndex.replace(":","-").replace("\\","-").replace("/","-") + "/"
            elif oompType == "PROJ":
                rv = "https://github.com/oomlout/oomlout_OOMP_projects/tree/main/"  + oompID + "/" 
            else:
                rv = "https://github.com/oomlout/oomlout_OOMP_parts/tree/main/"  + oompID + "/" 

        return rv.replace(":","-")

    def getFilename(self,filename,relative="",resolution="",extension=""):
        base = ""
        if relative == "": ## relative to oomlout_OOMP
            base = self.getFolder()
        elif relative.lower() == "flat": ## relative to directory
            base = ""
        elif relative.lower() == "full": ## relative to c
            base = baseDir + self.getFolder()
        elif relative.lower() == "github": ## relative to c
            oompID = self.getTag("oompID").value
            if "FOOTPRINT" in oompID:
                base = "https://github.com/oomlout/oomlout_OOMP_eda/tree/main/footprints/" + oompID + "/"
            elif "PROJECT" in oompID:
                base = "https://github.com/oomlout/oomlout_OOMP_projects/tree/main/" + oompID + "/"
            else:    
                base = "https://github.com/oomlout/oomlout_OOMP_parts/tree/main/" + oompID + "/"
        elif relative.lower() == "githubraw": ## relative to c
            oompID = self.getTag("oompID").value
            if "FOOTPRINT" in oompID:
                base = "https://raw.githubusercontent.com/oomlout/oomlout_OOMP_eda/main/footprints/" + oompID + "/"
            elif "PROJECT" in oompID:
                base = "https://raw.githubusercontent.com/oomlout/oomlout_OOMP_projects/main/" + oompID + "/"
            else:    
                base = "https://raw.githubusercontent.com/oomlout/oomlout_OOMP_parts/main/" + oompID + "/"
        else:
            base = baseDir + self.getFolder()
        fileExtra = filename
        
        ######  Bom Files
        if filename.lower() == "bominteractive":
            fileExtra = "kicad/bom/ibom.html"
        
        
        
        ######  Datasheet
        if filename.lower() == "datasheet":
            fileExtra = "datasheet.pdf"
        ######  Image files
        if filename.lower() == "image":
            type = self.getTag("oompType")
            if resolution != "":
                if type.value.upper() == "FOOTPRINT":
                    fileExtra = "image_" + str(resolution) + ".png"  
                else :
                    if extension =="":
                        fileExtra = "image_" + str(resolution) + ".jpg"  
                    else:
                        fileExtra = "image_" + str(resolution) + "." + extension  
            else:
                if extension =="":
                    fileExtra = "image.jpg"  
                else:
                    fileExtra = "image." + extension  
        imageTypePng = ["kicadPcb3d","kicadPcb3dFront","kicadPcb3dBack","eagleImage"]        
        for imageType in imageTypePng:
            if filename.lower() == imageType.lower():
                fileExtra = imageType + "_" + str(resolution) + ".png"  
        imageTypeJpg = ["image_RE","image_TOP","image_BOTTOM"]        
        for imageType in imageTypeJpg:
            if filename.lower() == imageType.lower():
                fileExtra = imageType + "_" + str(resolution) + ".jpg"  
                
        ######  Eagle Files
        if filename.lower() == "boardeagle":
            fileExtra = "boardEagle.brd"
        if filename.lower() == "eagleparts":
            fileExtra = "eagleparts.txt"

        ######  Kicad files
        if filename.lower() == "boardkicad":
            fileExtra = "kicad/boardKicad.kicad_pcb"
        if filename.lower() == "dirkicad":
            fileExtra = "kicad/"
        if filename.lower() == "dirkicad":
            fileExtra = "kicad/"
        if filename.lower() == "symbolkicad":
            fileExtra = "symbol.kicad_sym"

        

        ######  Label Files
        labels = ["label-front","label-inventory","label-spec"]
        for label in labels:
            if filename.lower() == label:
                if extension == "png":
                    fileExtra = label + ".png"  
                elif extension == "svg":
                    fileExtra = label + ".svg"    
                else:
                    fileExtra = label + ".pdf"    

        ######  Python Files
        if filename.lower() == "details":
            fileExtra = "details.py"        
        if filename.lower() == "pythonparts":
            fileExtra = "pythonParts.py"    

        ######  Redirect
        if filename.lower() == "redirect":
            base = base.replace(self.getFolder(),"")            
            fileExtra = "redirects/" + self.getTag("oompID").value.replace("/","-").replace(":","-") + "/index.html"
        if filename.lower() == "redirecthex":
            base = base.replace(self.getFolder(),"")            
            fileExtra = "redirects/" + self.getTag("hexID").value + "/index.html"

        return base + fileExtra

    ##No longer used    
    def indexMd(self):
        oompID = self.getTag("oompID").value
        name = self.getTag("name").value
        hexID = self.getTag("hexID").value
        rv = ""
        image = ""
        filename = getDir("parts") + oompID +  "/image_140.jpg"
        if os.path.isfile(filename):
            image = "![" + name + "](" + oompID +  "/image_140.jpg)"
        text = "[" + oompID + " <br> " + name + "](" + oompID + "/)"
        hex = ""
        if hexID != "":
            hex = "[" + hexID + "](" + oompID + "/)"
        rv = rv + image + "<br>" + text + "<br>" + hex
        return rv

    def mdLine(self, value):
        values = value.split(",")
        identifier = values[1]
        gitLink = self.getFilename("",resolution="140",relative="github")
        gitImage = self.getFilename("image",resolution="140",relative="githubRaw")
        oompID = self.getTag("oompID").value
        hexID = self.getTag("hexID").value
        name = self.getTag("name").value
        rv = "<table><tr>"

        rv = rv + "<td>![" + oompID + "](" + gitImage + ")</td>"
        rv = rv + "<td>" + identifier + "</td>"
        rv = rv + "<td>[" + oompID + "<br>" + name + "](" + gitLink + ")</td>"
        rv = rv + "<td>[" + hexID + "](" + gitLink + ")</td>"
        

        rv = rv + "</tr></table>"
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
    
    def addTag(self,name,value,singleValue=False):
        singleValueTags = ["hexID"]
        for singleValueTag in singleValueTags:
            if name == singleValueTag:
                singleValue = True
        if singleValue:
            workingTag = self.getTag(name)
            if workingTag.name == name:
                workingTag.value = value
            else:  ## if not already there add a new one
                self.tags.append(oompTag(name,value))
        else:
            self.tags.append(oompTag(name,value))

    def addTagSupplied(self,name,value,tag):
        tag.append(oompTag(name,value))
        return tag


    def removeTag(self,name):
        for x in self.tags:
            if x.name == name:
                self.tags.remove(x)

    def getTag(self,name):
        if name == "oompID":
            id = ""
            for x in self.tags:
                if x.name == "oompID":
                    id = x
                if id != "":
                    return id
            else:
                id = self.getTag("oompType").value + "-" +  self.getTag("oompSize").value + "-" +  self.getTag("oompColor").value + "-" +  self.getTag("oompDesc").value + "-" +  self.getTag("oompIndex").value
                self.addTag("oompID",id)
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
        if tagName == "allParts":
            oompParts = self.getTags("oompPart")
            rawParts = self.getTags("rawPart")
            for c in range(len(oompParts)):
                rv.append(oompTag("allParts",oompParts[c].value + "," + rawParts[c].value))
        else:
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

def loadParts(type):
    if type != "pickle":  
        import codes.OOMPdetailsType
        import codes.OOMPdetailsSize
        import codes.OOMPdetailsColor
        import codes.OOMPdetailsDesc
        import codes.OOMPdetailsIndex              
        if type == "all" or type == "parts" or type == "nofootprints":        
            print("    Loading:    Parts")
            directory = "oomlout_OOMP_parts\\"
            loadDirectory(directory)
            print("    done Details.py")
            loadDirectory(directory,fileFilter="details2.py")
            print("    done Details2.py")
        if type == "all" or type == "projects" or type == "nofootprints":  
            print("    Loading:    Projects")          
            directory = "oomlout_OOMP_projects\\"
            loadDirectory(directory)
            print("    done Details.py")
            loadDirectory(directory,fileFilter="details2.py")
            print("    done Details2.py")
            loadDirectory(directory,fileFilter="pythonParts.py")
            print("    done pythonParts.py")
        if type == "all" or type == "templates" or type == "nofootprints":        
            print("    Loading:    Templates")
            directory = "templates\\diag\\"
            loadDirectory(directory, fileFilter = ".py")
            print("    done Details.py")
            loadDirectory(directory,fileFilter="details2.py")
            print("    done Details2.py")
        if type == "all" or type == "eda":
            print("    Loading:    EDA")
            directory = "oomlout_OOMP_eda\\"            
            loadDirectory(directory)
            print("    done Details.py")
            loadDirectory(directory,fileFilter="details2.py")
            print("    done Details2.py")
                    
    else:
        picklePartsFile = "sourceFiles/picklePartsOOMP.pickle"
        pickleTagsFile = "sourceFiles/pickleTagsOOMP.pickle"
        global parts
        global details
        parts = pickle.load(open(picklePartsFile,"rb"))
        details = pickle.load(open(pickleTagsFile,"rb"))

def exportPickle():
    picklePartsFile = "sourceFiles/picklePartsOOMP.pickle"
    pickle.dump(parts, open(picklePartsFile,"wb"))
    pickleTagsFile = "sourceFiles/pickleTagsOOMP.pickle"
    pickle.dump(details, open(pickleTagsFile,"wb"))


def loadDirectory(directory,fileFilter="details.py"):
    testing = 1000000000000000000
    #testing = 10000
    #testing = 7000
    #testing = 5000
    #testing = 1000
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

partsFootprints = oompDict()
partsSymbols = oompDict()
partsParts = oompDict()
partsNoFootprints = oompDict()
partsProjects = oompDict()
partsTemplates = oompDict()

details = oompDetailDict()

parts = oompDict()
pass