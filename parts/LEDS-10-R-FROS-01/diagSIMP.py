svg_root.set('width', '50mm')
svg_root.set('height', '50mm')
width, height = svg_root.width, svg_root.height
svg_root.set('viewBox', '0 0 %.0f %.0f' % (width, height))
svg_root.namedview.set('showgrid', 'false')
shiftX=50
shiftY=50
# TEMPLATE  template;LEDS-10-X-XXXX-01-simp
linewidth = 0.2    #  linewidth;0.2
# TEMPLATE  template;LEDS-10-X-XXXX-01
#  corTemplate;LEDS-10-X-XXXX-01-bbls

#  text;0;1;5;oom.lt/;pin 1
text("L10R",(0,0),stroke_width=0.25,stroke='black',font_size='5pt',font_family='Relief Single Line Outline',text_align='center')


os.chdir("C:/GH/oomlout-OOMP/parts/LEDS-10-R-FROS-01/")
inkex.command.write_svg(svg_root, 'diagSIMP.svg')