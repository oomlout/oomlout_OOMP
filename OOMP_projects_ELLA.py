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

    ind = 2
    rev = "A"
    d["oompColor"] = str(ind).zfill(4)
    d["oompIndex"] = rev.zfill(2)
    d["hexID"] = "PRE" + str(ind)
    d["name"] = "Zoe Rev " + rev
    d["gitRepo"] = "https://github.com/electrolama/zoe"
    d["eagleBoard"] = "/Revision " + rev +"/pi-zigbee-poe-rtc.brd"
    d["eagleSchem"] = d["eagleBoard"].replace(".brd",".sch")
    OOMP_projects_BASE.makeProject(d)

    ind = ind
    rev = "B"
    d["oompColor"] = str(ind).zfill(4)
    d["oompIndex"] = rev.zfill(2)
    d["hexID"] = "PRE" + str(ind)
    d["name"] = "Zoe Rev " + rev
    d["gitRepo"] = "https://github.com/electrolama/zoe"
    d["eagleBoard"] = "/Revision " + rev +"/pi-zigbee-poe-rtc.brd"
    d["eagleSchem"] = d["eagleBoard"].replace(".brd",".sch")
    OOMP_projects_BASE.makeProject(d)

    ind = ind
    rev = "C"
    d["oompColor"] = str(ind).zfill(4)
    d["oompIndex"] = rev.zfill(2)
    d["hexID"] = "PRE" + str(ind)
    d["name"] = "Zoe Rev " + rev
    d["gitRepo"] = "https://github.com/electrolama/zoe"
    d["eagleBoard"] = "/Revision " + rev +"/pi-zigbee-poe-rtc.brd"
    d["eagleSchem"] = d["eagleBoard"].replace(".brd",".sch")
    OOMP_projects_BASE.makeProject(d)



    d["oompIndex"] = "01"
