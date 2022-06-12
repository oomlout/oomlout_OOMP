svg_root.set('width', '50mm')
svg_root.set('height', '50mm')
width, height = svg_root.width, svg_root.height
svg_root.set('viewBox', '0 0 %.0f %.0f' % (width, height))
svg_root.namedview.set('showgrid', 'false')
shiftX=50
shiftY=50
# TEMPLATE  template;BUTA-12-X-STAN-01
linewidth = 0.5    #  linewidth;0.5
######  rectangle;0;0;12.5;12.5;main bounding box
x = 0
y = 0* -1
width = 12.5
height = 12.5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth)

#  circle;0;0;8;8;button circle
######  rectangle;0;0;3;3;central square
x = 0
y = 0* -1
width = 3
height = 3
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth)

######  rectangle;-6.75;2.5;1;1;pins
x = -6.75
y = 2.5* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth)

######  rectangle;6.75;2.5;1;1;pins
x = 6.75
y = 2.5* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth)

######  rectangle;6.75;-2.5;1;1;pins
x = 6.75
y = -2.5* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth)

######  rectangle;-6.75;-2.5;1;1;pins
x = -6.75
y = -2.5* -1
width = 1
height = 1
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=linewidth)


# TEMPLATE  template;XXXX-XXXX-X-XXXX-XX-iden-words
#  textb;0;0;4;"S"
######  oompName;0;10.5;20;7;##name@@
x = 0
y = 10.5* -1
width = 20
height = 7
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shape = text(,(0,0),stroke_width=0.25,stroke='black',font_size='"12 mm Pushbutton (Tactile)"pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)

######  oompURL;0;-7.5;0.75;##hexID@@
x = 0
y = -7.5* -1
width = 0.75
height = "BT12"
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shape = text("http://oom.lt/BT12",(0,0),stroke_width=0.1,stroke='black',font_size='1pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)


os.chdir("C:/GH/oomlout-OOMP/parts/BUTA-12-X-STAN-01/")
inkex.command.write_svg(svg_root, 'diagIDEN.svg')