import OOMP
import OOMP_projects_BASE

def createProjects():
    d = {}
    d["oompType"] = "PROJ"
    d["oompSize"] = "IBBC"
    d["oompColor"] = "0001"
    d["oompDesc"] = "STAN"
    d["oompIndex"] = "01"
    
    d["hexID"] = "PRI1"

    d["name"] = "ADXL345 Breakout"
    d["gitRepo"] = "https://github.com/oomlout/IBBC_0001"
    d["gitName"] = "IBBC_0001"
    d["kicadBoard"] = "working/IBBC_0001/IBBC_0001.kicad_pcb"
    d["kicadSchem"] = d["kicadBoard"].replace("kicad_pcb","kicad_sch")

    OOMP_projects_BASE.makeProject(d)



