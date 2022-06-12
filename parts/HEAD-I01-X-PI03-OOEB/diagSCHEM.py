svg_root.set('width', '50mm')
svg_root.set('height', '50mm')
width, height = svg_root.width, svg_root.height
svg_root.set('viewBox', '0 0 %.0f %.0f' % (width, height))
svg_root.namedview.set('showgrid', 'false')
shiftX=50
shiftY=50
#  CLEAR variable;clear
pins = 3    #  variable;pins;3
# TEMPLATE  template;XXXX-XX-X-XX-01-PINS-ODD-schem
linewidth = 0    #  linewidth;0
######  rectangle;0;10;20;10*pins + 30;OutlineSquare
x = 0
y = 10* -1
width = 20
height = 10*pins + 30
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth)

linewidth = 1    #  linewidth;1
######  rectangle;-1.5;0;13;10*pins;Square
x = -1.5
y = 0* -1
width = 13
height = 10*pins
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth)

for b in range(pins):    # repeat;pins;hLine;7.5;(pins*10/2)-(i-1)*10-5;5;0;pin i
    i = b + 1
    #  hLine;7.5;(pins*10/2)-(i-1)*10-5;5;0;pin i;
for b in range(pins):    # repeat;pins;textb;2;(pins*10/2)-(i-1)*10-5;3.5;PIN i
    i = b + 1
    #  textb;2;(pins*10/2)-(i-1)*10-5;3.5;PIN i;
######  oompURL;0;-(%%pins%%*10/2)+3.5;3.5;0.75;##hexID@@
x = 0
y = -(pins*10/2)+3.5* -1
width = 3.5
height = 0.75
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shape = text("http://oom.lt/H03OOEB",(0,0),stroke_width=0.1,stroke='black',font_size='"H03OOEB"pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)

######  oompName;0;(%%pins%%*10/2)+5;20;5;1.33;##name@@
x = 0
y = (pins*10/2)+5* -1
width = 20
height = 5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shape = text("2.54 mm 3 Pin Header (OOEB)",(0,0),stroke_width=0.25,stroke='black',font_size='1.33pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)


os.chdir("C:/GH/oomlout-OOMP/parts/HEAD-I01-X-PI03-OOEB/")
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')