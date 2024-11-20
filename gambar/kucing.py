import cairo
import math

width = 700
height = 700
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
ctx = cairo.Context(surface)


#KOORDINAT
center_x = width / 2
center_y = height / 2

#TELINGAAAA
ctx.set_source_rgb(0.7, 0.7, 0.7)  # ABU CERAH
ctx.fill()
ctx.move_to(center_x - 20, center_y - 70)
ctx.line_to(center_x - 100, center_y - 120)
ctx.line_to(center_x - 90, center_y - 40)
ctx.close_path()
ctx.fill()

ctx.move_to(center_x + 20, center_y - 70)
ctx.line_to(center_x + 100, center_y - 120)
ctx.line_to(center_x + 90, center_y - 40)
ctx.close_path()
ctx.fill()

#TELINGA DALAM
ctx.set_source_rgb(1, 0.75, 0.8) #ABU GELAP
ctx.fill()
ctx.move_to(center_x - 20, center_y - 70)
ctx.line_to(center_x - 90, center_y - 105)
ctx.line_to(center_x - 85, center_y - 40)
ctx.close_path()
ctx.fill()

ctx.move_to(center_x + 20, center_y - 70)
ctx.line_to(center_x + 90, center_y - 105)
ctx.line_to(center_x + 85, center_y - 40)
ctx.close_path()
ctx.fill()

#BUNTUT
ctx.set_source_rgb(0.7,0.7,0.7)
ctx.set_line_width(24)
ctx.move_to(center_x+60, center_y+250)
ctx.curve_to(center_x+120,center_y+280,center_x+100,center_y+140,center_x+180, center_y+120)
ctx.stroke()
ctx.set_line_width(1)
ctx.arc(center_x+180, center_y+120, 12, 0, 2 * math.pi)
ctx.fill()

#BADAN
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.move_to(center_x-50,center_y+80)
ctx.curve_to(center_x-20, center_y+130,center_x-180,center_y+300, center_x, center_y+310)
ctx.curve_to(center_x+180,center_y+300,center_x+20, center_y+130, center_x+50,center_y+80)
ctx.fill()

#ctx.set_source_rgb(0.7, 0.7, 0.7)
#ctx.move_to(center_x-60,center_y+70)
#ctx.curve_to(center_x+60, center_y+100,center_x-170,center_y+230, center_x-10, center_y+250)
#ctx.curve_to(center_x+170,center_y+250,center_x-60, center_y+100, center_x+60,center_y+70)
#ctx.fill()

#KEPALA
ctx.arc(center_x, center_y, 100, 0, 2 * math.pi)
ctx.set_source_rgb(0.8, 0.8, 0.8)  # ABU CERAH
ctx.fill()

#MATA -KIRI
ctx.arc(center_x - 40, center_y - 10, 15, 0, 2 * math.pi)
ctx.set_source_rgb(0, 0, 0) 
ctx.fill()
#MATA KANAN
ctx.arc(center_x + 40, center_y - 10, 15, 0, 2 * math.pi)
ctx.fill()
#KILAU MATA
ctx.set_source_rgb(1, 1, 1) 
ctx.arc(center_x - 35, center_y - 15, 5, 0, 2 * math.pi)
ctx.fill()
ctx.arc(center_x + 45, center_y - 15, 5, 0, 2 * math.pi)
ctx.fill()

#HIDUNK
ctx.move_to(center_x , center_y+35)
ctx.line_to(center_x+10, center_y+20 )
ctx.line_to(center_x - 10, center_y+20 )
ctx.close_path()
ctx.set_source_rgb(1, 0.75, 0.8)  # PINK
ctx.fill()

#MULUT
ctx.set_source_rgb(0,0,0) 
ctx.set_line_width(2)
ctx.arc(center_x-5, center_y+35 , 5, 0, math.pi)
ctx.stroke()
ctx.arc(center_x+5, center_y+35, 5, 0, math.pi)
ctx.stroke()

#KUMIS
ctx.set_source_rgb(0, 0, 0)
control_x, control_y = center_x + 65, center_y +15

#KANAN
ctx.move_to(center_x + 50, center_y +20) 
ctx.curve_to(control_x, control_y, control_x+10, control_y-5, center_x + 120 , center_y +10)
ctx.move_to(center_x+50, center_y + 30)
ctx.curve_to(control_x, control_y+10, control_x, control_y +5, center_x + 110 , center_y +30)
ctx.move_to(center_x+50, center_y + 40)
ctx.curve_to(control_x, control_y+20, control_x+40, control_y +40, center_x + 100 , center_y +52)
ctx.stroke()

#KIRI
control_x2, control_y2 = center_x - 65, center_y +15
ctx.move_to(center_x - 50, center_y +20)
ctx.curve_to(control_x2, control_y2, control_x2+10, control_y2-5, center_x - 120 , center_y +10)
ctx.move_to(center_x-50, center_y + 30)
ctx.curve_to(control_x2, control_y2+10, control_x2, control_y2 +5, center_x - 110 , center_y +30)
ctx.move_to(center_x-50, center_y + 42)
ctx.curve_to(control_x2+15, control_y2+30, control_x2+20, control_y2 +20, center_x - 100 , center_y +60)
ctx.stroke()

#TANGAN
ctx.set_line_width(3)
ctx.set_source_rgb(0.7,0.7,0.7)
ctx.move_to(center_x-35,center_y+200)
ctx.curve_to(center_x-45,center_y+250, center_x-5,center_y+340,center_x-10,center_y+200)
ctx.move_to(center_x+35,center_y+200)
ctx.curve_to(center_x+45,center_y+250, center_x+5,center_y+340,center_x+10,center_y+200)
ctx.stroke()

surface.write_to_png('kucing.png')