import OOMP
import OOMP_projects_BASE

def createProjects():
    d = {}
    d["oompType"] = "PROJ"
    d["oompSize"] = "ELLA"
    d["oompColor"] = "0001"
    d["oompDesc"] = "STAN"
    d["oompIndex"] = "01"
    
    d["hexID"] = "PRE1"

    d["name"] = "Zig A Zig Ah"
    d["gitRepo"] = "https://github.com/electrolama/zig-a-zig-ah"
    d["eagleBoard"] = "zzh/Revision A/zzh.brd"
    d["eagleSchem"] = "zzh/Revision A/zzh.sch"

    OOMP_projects_BASE.makeProject(d)



