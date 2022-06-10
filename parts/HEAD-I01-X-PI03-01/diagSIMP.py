pins = 3    #  variable;pins;3
# TEMPLATE  template;XXXX-I01-X-XX-01-simp
linewidth = 0.2    #  linewidth;0.2
x = 0    #  rectangle;0;0;2.54*pins;2.54;Main Square
y = 0
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect((x1,y1), (x2,y2),0.1,stroke_width=linewidth)
x = 0    #  oompURL;0;0;2.835;##hexID@@
y = 0
width = 20
height = 5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect((x1,y1), (x2,y2),0.1,stroke_width=0)
x = 0    #  oompURL;0;0;2.835;##hexID@@
y = 0
width = 0
height = 0
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = text("http://oom.lt/XXXX-I01-X-XX-01-simp", (0, 0),stroke_width=0.2,font_size='2.835pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)

os.chdir("C:/GH/oomlout-OOMP/parts/HEAD-I01-X-PI03-01/")
inkex.command.write_svg(svg_root, 'diagSIMP.svg')