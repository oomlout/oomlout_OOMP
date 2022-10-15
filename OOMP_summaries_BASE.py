import OOMP



import OOMPsummaries
import math

from oomBase import *

def createAllSummaries(all=False,overwrite=False,filter=""):
    for item in OOMP.parts:        
        if filter in item.getID():
            print("Summaries For:" + item.getID())
            createSummary(item=item,all=all,overwrite=overwrite)
    OOMPsummaries.generateReadmeIndex()
    


def createSummary(item,all=False,overwrite=False,filter=""):
    print("    Making Summary")
    OOMPsummaries.generateReadme(item,overwrite)




###### md helpers
def getLink(text,link):
    return "[" + text + "](" + link + ")"

def getPictureLink(item):    
    if item.getID() != "----":
        string = item.getFilename("kicadPcb3d",relative="githubRaw") + "<br>" + item.getID() + "  " + item.getName()
        string = getLink(string,item.getFilename(filename="",relative="github"))
    else:
        string = "MISSING"
    return string

def addDisplayTable(mdFile,cells,width):
    mdFile.new_line()

    numCells = len(cells)
    rows = math.floor(numCells / width) + 1
    difference = rows * width - len(cells)

    for r in range(0,difference):
        cells.append("")

    #print("Table Test: " + str(len(cells)) + "    rows: " + str(rows)  + "    Cols: " + str(width))
    mdFile.new_table(columns=width, rows=rows, text=cells, text_align='center')                           