pins = 3    #  variable;pins;3
# TEMPLATE  template;XXXX-XX-X-XX-01-PINS-ODD-schem
linewidth = 0    #  linewidth;0
x = 0    #  rectangle;0;10;20;10*pins + 30;OutlineSquare
y = 10
width = 20
height = 10*pins + 30
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect((x1,y1), (x2,y2),0.1,stroke_width=linewidth)
linewidth = 1    #  linewidth;1
x = -1.5    #  rectangle;-1.5;0;13;10*pins;Square
y = 0
width = 13
height = 10*pins
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect((x1,y1), (x2,y2),0.1,stroke_width=linewidth)
for b in range(pins):    # repeat;pins;hLine;7.5;(pins*10/2)-(i-1)*10-5;5;0;pin i
    i = b + 1
    #  hLine;7.5;(pins*10/2)-(i-1)*10-5;5;0;pin i;
for b in range(pins):    # repeat;pins;textb;2;(pins*10/2)-(i-1)*10-5;3.5;PIN i
    i = b + 1
    #  textb;2;(pins*10/2)-(i-1)*10-5;3.5;PIN i;
x = 0    #  oompURL;0;-(%%pins%%*10/2)+3.5;3.5;##hexID@@
y = -(pins*10/2)+3.5
width = 20
height = 5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect((x1,y1), (x2,y2),0.1,stroke_width=0)
x = 0    #  oompURL;0;-(%%pins%%*10/2)+3.5;3.5;##hexID@@
y = -(pins*10/2)+3.5
width = 0
height = 0
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = text("http://oom.lt/XXXX-XX-X-XX-01-PINS-ODD-schem", (0, 0),stroke_width=0.2,font_size='2.835pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)
#  oompName;0;(pins*10/2)+5;20;5;##name@@

os.chdir("C:/GH/oomlout-OOMP/parts/HEAD-I01-X-PI03-01/")
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')