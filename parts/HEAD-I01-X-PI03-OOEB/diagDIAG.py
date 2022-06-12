svg_root.set('width', '50mm')
svg_root.set('height', '50mm')
width, height = svg_root.width, svg_root.height
svg_root.set('viewBox', '0 0 %.0f %.0f' % (width, height))
svg_root.namedview.set('showgrid', 'false')
shiftX=50
shiftY=50
#  CLEAR variable;clear
pins = 3    #  variable;pins;3
# TEMPLATE  template;HEAD-I01-X-XX-01-diag
linewidth = 0.2    #  linewidth;0.2
for b in range(pins):    # repeat;pins;rectangle;(2.54*pins/2-2.54/2)-2.54*(i-1);-2;0.64;11.54;pin i
    i = b + 1
    ######  rectangle;(2.54*pins/2-2.54/2)-2.54*(i-1);-2;0.64;11.54;pin i;
    x = (2.54*pins/2-2.54/2)-2.54*(i-1)
    y = -2* -1
    width = 0.64
    height = 11.54
    x1 = x - width/2 
    y1 = y + height/2 
    x2 = x + width/2 
    y2 = y - height/2 
    rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth)
    
linewidth = 1    #  linewidth;1
######  rectangle;0;-3.5;2.54*pins;2.54;Main Square
x = 0
y = -3.5* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth)

######  oompName;0;11;20;5;1.33;##name@@
x = 0
y = 11* -1
width = 20
height = 5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shape = text("2.54 mm 3 Pin Header (OOEB)",(0,0),stroke_width=0.25,stroke='black',font_size='1.33pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)

######  oompURL;0;-8.5;20;5;0.75;##hexID@@
x = 0
y = -8.5* -1
width = 20
height = 5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shape = text("http://oom.lt/H03OOEB",(0,0),stroke_width=0.1,stroke='black',font_size='0.75pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)


os.chdir("C:/GH/oomlout-OOMP/parts/HEAD-I01-X-PI03-OOEB/")
inkex.command.write_svg(svg_root, 'diagDIAG.svg')