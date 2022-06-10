pins = 3    #  variable;pins;3
# TEMPLATE  template;XXXX-I01-X-XX-01-iden
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
#  textB;0;0;2.835;##ooDesignator@@

os.chdir("C:/GH/oomlout-OOMP/parts/HEAD-I01-X-PI03-01/")
inkex.command.write_svg(svg_root, 'diagIDEN.svg')