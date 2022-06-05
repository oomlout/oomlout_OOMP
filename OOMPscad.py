
import OPSC as opsc
from solid.objects import *

######  OOMP ROUTINES

def oompLeds10XX01(color):
    part = opsc.item()



    posA = [1.27,0,0.1]
    posB = [-posA[0],posA[1],posA[2]]
    size = [opsc.ooebPinWidth,opsc.ooebPinWidth,5.1]

    color = opsc.colWire
    part.addPos(insert("cube",pos=posA,size=size,color=color))
    part.addPos(insert("cube",pos=posB,size=size,color=color))
    color = opsc.colLEDRed
    part.addPos(insert("cylinder",pos=[0,0,8.5],rad=5,depth=6.5,color=color))
    part.addPos(insert("cylinder",pos=[0,0,2.05],rad=5.5,depth=2,color=color))
    part.addPos(insert("sphere",pos=[0,0,8.5+5],rad=5,color=color))

    return part.getPart()


def oompReseW04XX01(color):
    part = opsc.item()
    
    pinSpacing = 3.81
    resLength = 6.8
    resRad = 2.5/2
    resBandSpacing = 1

    posA = [pinSpacing,0,0+resRad+opsc.ooebPinWidth/2]
    posB = [-posA[0],posA[1],posA[2]]
    size = [opsc.ooebPinWidth,opsc.ooebPinWidth,5+resRad+opsc.ooebPinWidth/2]

    color = opsc.colWire
    part.addPos(insert("cube",pos=posA,size=size,color=color))
    part.addPos(insert("cube",pos=posB,size=size,color=color))
    part.addPos(insert("cube",pos=[pinSpacing*2/2,0,resRad],size=[opsc.ooebPinWidth,opsc.ooebPinWidth,pinSpacing*2],rot=[0,90,0],color=color))

    color = opsc.colResistor
    resPos = [resLength/2,0,resRad+0.01]
    part.addPos(insert("cylinder",pos=resPos,depth=resLength,rad=resRad,rot=[90,0,90],color=color))
    
    ####bands
    bandRad=resRad+0.01
    bandDepth = 0.75
    band1Pos=[resPos[0]-1,resPos[1],resPos[2]]    
    band1Color = opsc.colRes[5]
    part.addPos(insert("cylinder",pos=band1Pos,depth=bandDepth,rad=bandRad,rot=[90,0,90],color=band1Color))
    
    band2Pos=[band1Pos[0]-resBandSpacing,resPos[1],resPos[2]]    
    band2Color = opsc.colRes[6]
    part.addPos(insert("cylinder",pos=band2Pos,depth=bandDepth,rad=bandRad,rot=[90,0,90],color=band2Color))
    
    band3Pos=[band2Pos[0]-resBandSpacing,resPos[1],resPos[2]]    
    band3Color = opsc.colRes[1]
    part.addPos(insert("cylinder",pos=band3Pos,depth=bandDepth,rad=bandRad,rot=[90,0,90],color=band3Color))




    return part.getPart()


######  Insert Routines

def insert(item,pos=[None,None,None],x=0,y=0,z=0,ex=0,size=[None,None,None],length=0,rot=[None,None,None],rotX=0,rotY=0,rotZ=0,width=0,height=0,depth=100,rad=0,rad2=0,color=opsc.colDefault,alpha=1,OOwidth=0,OOheight=0,holes=True,negative=True, name=""):
    returnValue = ""
    if pos[0] != None:
        x=pos[0]
        y=pos[1]
        z=pos[2]
    if rot[0] != None:
        rotX=rot[0]
        rotY=rot[1]
        rotZ=rot[2]
    
    returnValue = translate((x,y,z))(
            rotate((rotX,rotY,rotZ))(
                OOEBInsertIf(item,pos,x,y,z,ex,size,length,rot,rotX,rotY,rotZ,width,height,depth,rad,rad2,color,alpha,OOwidth,OOheight,holes,negative,name)
            )
        )
    

    return returnValue

def OOEBInsertIf(item,pos=[None,None,None],x=0,y=0,z=0,ex=0,size=[None,None,None],length=0,rot=[None,None,None],rotX=0,rotY=0,rotZ=0,width=0,height=0,depth=100,rad=0,rad2=0,color=opsc.colDefault,alpha=1,OOwidth=0,OOheight=0,holes=True,negative=True, name=""):

    #print("    OOEBInsert item:" + str(item) + " at:[" + str(x) + "," + str(y) + "," + str(z) + "] size: [" + str(width) + "," + str(height) + "," + str(depth) + "]")

    #print(pos)

    if(item=="XXXX"):
        x=0
    ######  OOMP ITEMS
    elif(item=="OOMP-LEDS-10-X-X-01"):
        returnValue = oompLeds10XX01(color)
    elif(item=="OOMP-RESE-W04-X-X-01"):
        returnValue = oompReseW04XX01(color)

    else:    
        returnValue = opsc.insert(item,[None,None,None],0,0,0,ex,size,length,[None,None,None],0,0,0,width,height,depth,rad,rad2,color,alpha,OOwidth,OOheight,holes,negative,name)
    return returnValue

