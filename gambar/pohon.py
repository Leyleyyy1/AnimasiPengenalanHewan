import cairo

WIDTH, HEIGHT = 400, 400

def draw_circle(context, x, y, radius, color):
    context.set_source_rgb(*color)
    context.arc(x, y, radius, 0, 2 * 3.14159)
    context.fill()


surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

green_shade_light = (0.0, 0.3, 0.0) 

leaf_positions = [
    (200, 100, 50), (160, 140, 60), (240, 140, 60), 
    (180, 80, 50), (220, 80, 50), (150, 100, 50), 
    (250, 100, 50), (200, 160, 50)
]

leaf_positions1 = [
    (200, 100, 50), (160, 140, 60), (240, 140, 60), 
    (180, 80, 50), (220, 80, 50), (150, 100, 50), 
    (250, 100, 50), (200, 160, 50)
]


for x, y, r in leaf_positions:
    draw_circle(context, x, y, r, green_shade_light)
    

context.set_source_rgb(0.61, 0.35, 0.21) 
context.move_to(180, 300) 
context.curve_to(200, 250, 175, 200, 200, 150)  
context.line_to(205, 150)  
context.curve_to(225, 200, 200, 250, 225, 300)  
context.close_path()
context.fill()

context.set_source_rgb(0.61, 0.35, 0.21)  


context.set_line_width(7) 

context.move_to(200, 200)
context.line_to(150, 130)
context.line_to(170, 170)
context.close_path()
context.stroke()

context.move_to(200, 200)
context.line_to(250, 150)
context.line_to(230, 180)
context.close_path()
context.stroke()

surface.write_to_png("pohon.png")
