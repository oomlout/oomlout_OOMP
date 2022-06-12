import os
svg_root.set('width', '50mm')
svg_root.set('height', '50mm')
width, height = svg_root.width, svg_root.height
svg_root.set('viewBox', '0 0 %.0f %.0f' % (width, height))
svg_root.namedview.set('showgrid', 'false')
shiftX=50
shiftY=50
# TEMPLATE  template;BUTA-06-X-STAN-01
linewidth = 0.5    #  linewidth;0.5
######  rectangle;0;0;6.2;6.2;main bounding box
x = 0
y = 0* -1
width = 6.2
height = 6.2
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth)

#  circle;0;0;3;3;button circle
######  rectangle;-3.25;2.25;1;1;pins
x = -3.25
y = 2.25* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth)

######  rectangle;3.25;2.25;1;1;pins
x = 3.25
y = 2.25* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth)

######  rectangle;3.25;-2.25;1;1;pins
x = 3.25
y = -2.25* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth)

######  rectangle;-3.25;-2.25;1;1;pins
x = -3.25
y = -2.25* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth)


os.chdir("C:/GH/oomlout-OOMP/parts/BUTA-06-X-STAN-01/")
try:
    os.remove("C:/GH/oomlout-OOMP/parts/BUTA-06-X-STAN-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')