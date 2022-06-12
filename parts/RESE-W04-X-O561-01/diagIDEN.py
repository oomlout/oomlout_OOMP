svg_root.set('width', '50mm')
svg_root.set('height', '50mm')
width, height = svg_root.width, svg_root.height
svg_root.set('viewBox', '0 0 %.0f %.0f' % (width, height))
svg_root.namedview.set('showgrid', 'false')
shiftX=50
shiftY=50
# TEMPLATE  template;RESE-W04-X-XXXX-XX-iden
# TEMPLATE  template;RESE-W04-X-XXXX-01
#  corTemplate;RESE-W04-X-XXXX-01

text("R1",(0,0),stroke_width=0.25,stroke='black',font_size='4pt',font_family='Relief Single Line Outline',text_align='center')


os.chdir("C:/GH/oomlout-OOMP/parts/RESE-W04-X-O561-01/")
inkex.command.write_svg(svg_root, 'diagIDEN.svg')