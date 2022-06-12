svg_root.set('width', '50mm')
svg_root.set('height', '50mm')
width, height = svg_root.width, svg_root.height
svg_root.set('viewBox', '0 0 %.0f %.0f' % (width, height))
svg_root.namedview.set('showgrid', 'false')
shiftX=50
shiftY=50
# TEMPLATE  template;XXXX-T220-X-XXXX-01-simp
######  rectangle;0;0;10.16;4.35;Main Square
x = 0
y = 0* -1
width = 10.16
height = 4.35
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth)

#  hLine;0;0.925;10.16;1;top line
#  text;0;0;4;oom.lt/;pin 1
text("TN120",(0,0),stroke_width=0.25,stroke='black',font_size='4pt',font_family='Relief Single Line Outline',text_align='center')


os.chdir("C:/GH/oomlout-OOMP/parts/TRNN-T220-BCE-A05-01/")
inkex.command.write_svg(svg_root, 'diagSIMP.svg')