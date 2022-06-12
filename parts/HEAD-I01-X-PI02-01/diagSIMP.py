import os
svg_root.set('width', '50mm')
svg_root.set('height', '50mm')
width, height = svg_root.width, svg_root.height
svg_root.set('viewBox', '0 0 %.0f %.0f' % (width, height))
svg_root.namedview.set('showgrid', 'false')
shiftX=50
shiftY=50
#  CLEAR variable;clear
pins = 2    #  variable;pins;2
# TEMPLATE  template;XXXX-I01-X-XX-01-simp
linewidth = 1    #  linewidth;1
######  rectangle;0;0;2.54*pins;2.54;Main Square
x = 0
y = (0)* -1
width = 2.54*pins
height = 2.54
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth)

######  oompURL;0;0;20;1;2;##hexID@@
x = 0
y = (0)* -1
width = 20
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
x = 0
y = (0)* -1
fontShift = (2)* 0.3527 * .5
shape = text('http://oom.lt/H02',(x+shiftX/2*mm,(y+shiftY/2+fontShift/2)*mm),stroke_width=0.1,stroke='black',font_size='2pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)


os.chdir("C:/GH/oomlout-OOMP/parts/HEAD-I01-X-PI02-01/")
try:
    os.remove("C:/GH/oomlout-OOMP/parts/HEAD-I01-X-PI02-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')