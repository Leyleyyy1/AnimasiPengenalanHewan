import cairo
width, height = 400, 150


surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)

ctx.set_source_rgb(0.30, 0.49, 0.11)  
ctx.move_to(0, height - 50)
for x in range(0, width + 1, 40): 
    ctx.curve_to(x - 20, height - 80, x + 20, height - 80, x + 40, height - 50)
ctx.line_to(width, height)
ctx.line_to(0, height)
ctx.close_path()
ctx.fill()

surface.write_to_png("simple_bush.png")