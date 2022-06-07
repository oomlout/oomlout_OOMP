# TEMPLATE  template;LEDS-10-X-XXXX-01-bbls
linewidth = 0.2    #  linewidth;0.2
# TEMPLATE  template;LEDS-10-X-XXXX-01

x = -1.27    #  rectangle;-1.27;0;0.6;0.6;pin1
y = 0
width = 0.6
height = 0.6
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect((x1,y1), (x2,y2),0.1,stroke_width=linewidth)
x = 1.27    #  rectangle;1.27;0;0.6;0.6;pin2
y = 0
width = 0.6
height = 0.6
x1 = x - width/2 
y1 = y + height/2 
x2 = x + width/2 
y2 = y - height/2 
rect((x1,y1), (x2,y2),0.1,stroke_width=linewidth)
#  textB;-1.27;1;2.5;A;pin 1
#  textB;1.27;1;2.5;K;pin 2
#  oompName;0;8.5;23;5;##name@@
#  ompURL;0;-7;2.835;##hexID@@

