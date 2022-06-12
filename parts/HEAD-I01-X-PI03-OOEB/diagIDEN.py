svg_root.set('width', '50mm')
svg_root.set('height', '50mm')
width, height = svg_root.width, svg_root.height
svg_root.set('viewBox', '0 0 %.0f %.0f' % (width, height))
svg_root.namedview.set('showgrid', 'false')
shiftX=50
shiftY=50
#  CLEAR variable;clear
pins = 3    #  variable;pins;3
os.chdir("C:/GH/oomlout-OOMP/parts/HEAD-I01-X-PI03-OOEB/")
inkex.command.write_svg(svg_root, 'diagIDEN.svg')