svg_root.set('width', '50mm')
svg_root.set('height', '50mm')
width, height = svg_root.width, svg_root.height
svg_root.set('viewBox', '0 0 %.0f %.0f' % (width, height))
svg_root.namedview.set('showgrid', 'false')
shiftX=50
shiftY=50
# TEMPLATE  template;RESE-XXXX-X-XXXX-XX-schem
#  corTemplate;RESE-XXXX-X-XXXX-XX-schem
######  oompName;0;7;20;6;##name@@
x = 0
y = 7* -1
width = 20
height = 6
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shape = text(,(0,0),stroke_width=0.25,stroke='black',font_size='"1/4 Watt 560 Ohm Resistor"pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)

######  oompURL;0;-5;0.75;##hexID@@
x = 0
y = -5* -1
width = 0.75
height = "R4561"
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shape = text("http://oom.lt/R4561",(0,0),stroke_width=0.1,stroke='black',font_size='1pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)


os.chdir("C:/GH/oomlout-OOMP/parts/RESE-W04-X-O561-01/")
inkex.command.write_svg(svg_root, 'diagSCHEM.svg')