import os
svg_root.set('width', '50mm')
svg_root.set('height', '50mm')
width, height = svg_root.width, svg_root.height
svg_root.set('viewBox', '0 0 %.0f %.0f' % (width, height))
svg_root.namedview.set('showgrid', 'false')
shiftX=50
shiftY=50
#  CLEAR variable;clear
pins = 2    #  variable;pins;2
# MISSING TEMPLATE # TEMPLATE  template;HEAD-I01-X-XX-01-diag

os.chdir("C:/GH/oomlout-OOMP/parts/HEAD-I01-X-PI02-01/")
try:
    os.remove("C:/GH/oomlout-OOMP/parts/HEAD-I01-X-PI02-01/diagDIAG.svg")
except:
    f=0
inkex.command.write_svg(svg_root, 'diagDIAG.svg')