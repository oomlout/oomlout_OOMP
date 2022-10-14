from OOMPsummaries import *

import OOMP_summaries_BASE as base

def generateCollections():
    collections = {}
    col = "qwiic"
    collections[col] = {}
    collections[col]["ID"] =  col
    collections[col]["NAME"] =  "QWIIC Breakouts"
    items= []
    ###### Sparkfun
    baseStart = "PROJ-SPAR-"
    baseEnd = "-STAN-01"
    indexes = []
    indexes = ["15932","18355","8688","17001"]
    for index in indexes:
        items.append(baseStart + index + baseEnd)
    collections[col]["ITEMS"] = items
    
    oomMakeDir("collections/")
    for collection in collections:
        generateCollectionPage(collections[collection])

    generateCollectionsIndex(collections)


def generateCollectionsIndex(collections):  
    print("Generating Collection Index")  
    filename = "collections.md"
    
    mdFile = MdUtils(file_name=filename,title="")
    mdFile.new_line(getNavigation())
    mdFile.new_header(level=1,title="Collections")    
    parts = []
    for item in collections:      
        parts.append(mdGetLink(collections[item]["NAME"],"collections/" + item + ".md"))
        base.addDisplayTable(mdFile,parts,4)   
    #mdFile.new_table_of_contents(table_title='Contents', depth=2)
    mdFile.create_md_file()     
    


def generateCollectionPage(collection):   
    print("    Generating collection page for: " + collection["ID"]) 
    filename = "collections/" + collection["ID"] + ".md"
    
    mdFile = MdUtils(file_name=filename,title="")
    mdFile.new_header(level=1,title="Collection: " + collection["NAME"])
    
    items = []
    for itemID in collection["ITEMS"]:
        item = OOMP.getPartByID(itemID)
        string = base.getPictureLink(item)
        items.append(string)
    base.addDisplayTable(mdFile,items,4)
    
    mdFile.create_md_file()     

