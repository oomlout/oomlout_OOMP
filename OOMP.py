import os

details = list()
parts = list()




def oompAddDetail(category,code,name,sort="",extra1="",extra2=""):
    details.append(oompDetail(category,code,name,sort,extra1="",extra2=""))

def getDetailFromCode(category,code):
    for x in details:
        if x.category == category:
            if x.code == code:
                return x
    return oompDetail("","","","")

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

        

class oompItem:

    def __init__(self,index=0):
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
        else:
            if name == "namename":
                name = "name"
            for x in self.tags:
                if x.name == name:
                    return x
            return oompTag("","")

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
    loadDirectory(directory)

def loadDirectory(directory):
    for subdir, dirs, files in os.walk(directory):
            for file in files:
                if(file == "details.py"):
                    moduleName = file.replace(".py","")
                    moduleName = subdir.replace("\\",".") + "." + moduleName
                    ##print("    moduleName: " + moduleName)
                    print(".",end="")
                    __import__(moduleName)    

#### import parts
loadParts()
        
