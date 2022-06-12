svg_root.set('width', '50mm')
svg_root.set('height', '50mm')
width, height = svg_root.width, svg_root.height
svg_root.set('viewBox', '0 0 %.0f %.0f' % (width, height))
svg_root.namedview.set('showgrid', 'false')
shiftX=50
shiftY=50
# TEMPLATE  template;LEDS-10-X-XXXX-01-diag
linewidth = 0.2    #  linewidth;0.2
#  corTemplate;LEDS-10-X-XXXX-01-diag
text(A,(0,0),stroke_width=0.25,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center')

text(K,(0,0),stroke_width=0.25,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center')

######  oompName;0;23;20;5;1.33;##name@@
x = 0
y = 23* -1
width = 20
height = 5
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shape = text("10 mm Frosted Red LED",(0,0),stroke_width=0.25,stroke='black',font_size='1.33pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)

######  oompURL;0;-21;4;##hexID@@
x = 0
y = -21* -1
width = 4
height = "L10R"
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
shape = rect(((x1+shiftX/2)*mm,(y1+shiftY/2)*mm), ((x2+shiftX/2)*mm,(y2+shiftY/2)*mm),0.1,stroke_width=0)
shape = text("http://oom.lt/L10R",(0,0),stroke_width=0.1,stroke='black',font_size='1pt',font_family='Relief Single Line Outline',text_align='center',shape_inside=shape)


os.chdir("C:/GH/oomlout-OOMP/parts/LEDS-10-R-FROS-01/")
inkex.command.write_svg(svg_root, 'diagDIAG.svg')