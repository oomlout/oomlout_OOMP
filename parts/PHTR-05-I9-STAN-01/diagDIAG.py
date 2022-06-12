svg_root.set('width', '50mm')
svg_root.set('height', '50mm')
width, height = svg_root.width, svg_root.height
svg_root.set('viewBox', '0 0 %.0f %.0f' % (width, height))
svg_root.namedview.set('showgrid', 'false')
shiftX=50
shiftY=50
os.chdir("C:/GH/oomlout-OOMP/parts/PHTR-05-I9-STAN-01/")
inkex.command.write_svg(svg_root, 'diagDIAG.svg')