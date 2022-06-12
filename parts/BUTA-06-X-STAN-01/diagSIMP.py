import os
svg_root.set('width', '50mm')
svg_root.set('height', '50mm')
width, height = svg_root.width, svg_root.height
svg_root.set('viewBox', '0 0 %.0f %.0f' % (width, height))
svg_root.namedview.set('showgrid', 'false')
shiftX=50
shiftY=50
os.chdir("C:/GH/oomlout-OOMP/parts/BUTA-06-X-STAN-01/")
try:
    os.remove("C:/GH/oomlout-OOMP/parts/BUTA-06-X-STAN-01/diagSIMP.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagSIMP.svg')