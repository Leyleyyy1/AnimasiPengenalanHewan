import pygame
import os
import cairo
import numpy as np

def draw_background(surface, tree_image, clouds):
    width, height = surface.get_width(), surface.get_height()


    cairo_surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    cr = cairo.Context(cairo_surface)

    cr.set_source_rgb(0.99, 0.98, 0.82)  
    cr.rectangle(0, 0, width, height * 2 // 2)
    cr.fill()

    cr.set_source_rgb(0.25, 0.76, 0.53)
    cr.move_to(0,height*2//3)
    cr.curve_to(height*2//2, height * 2 //2, height * 2 // 3, height/2,width,height *2//3)
    cr.line_to(width,height)
    cr.line_to(0,height*2//2)
    cr.fill()


    buffer = cairo_surface.get_data()
    array = np.ndarray(shape=(height, width, 4), dtype=np.uint8, buffer=buffer)
    rgb_array = array[:, :, :3]  

    image = pygame.image.frombuffer(rgb_array.tobytes(), (width, height), "RGB")
    surface.blit(image, (0, 0))

    for cloud in clouds:
        pygame.draw.circle(surface, (255, 255, 255), (cloud['x'], cloud['y']), 30)
        pygame.draw.circle(surface, (255, 255, 255), (cloud['x'] + 30, cloud['y'] - 10), 30)
        pygame.draw.circle(surface, (255, 255, 255), (cloud['x'] + 60, cloud['y']), 30)

def draw_tree(surface, tree_image, x, y, width=500, height=500):
    """Menggambar pohon pada posisi yang ditentukan."""
    tree_scaled = pygame.transform.scale(tree_image, (width, height))
    surface.blit(tree_scaled, (x, y))

def draw_bush(surface, bush_image, x, y, width=400, height=150):
    """Menggambar pohon pada posisi yang ditentukan."""
    bush_scaled = pygame.transform.scale(bush_image, (width, height))
    surface.blit(bush_scaled, (x, y))

def draw_button(surface, text, x, y, radius, font):
    """Menggambar tombol bulat dengan teks di tengahnya."""
    outer_color = (34, 139, 34)  
    inner_color = (255, 255, 255)  
    text_color = (0, 0, 0) 

   
    pygame.draw.circle(surface, outer_color, (x, y), radius)
    pygame.draw.circle(surface, inner_color, (x, y), radius - 5)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

def draw_text(surface, text, x, y, font, color=(0, 0, 0)):
    """Menggambar teks di layar."""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption("Tampilan Awal")

    tree_image_path = "pohon.png"
    if not os.path.exists(tree_image_path):
        print("File pohon.png tidak ditemukan!")
        return

    tree_image = pygame.image.load(tree_image_path)

    bush_image_path = "simple_bush.png"
    if not os.path.exists(bush_image_path):
        print("File simple_bush.png tidak ditemukan!")
        return
    
    bush_image = pygame.image.load(bush_image_path)
    font = pygame.font.SysFont("Comic Sans", 24)
    title_font = pygame.font.SysFont("Comic Sans", 32)
    clouds = [
        {'x': 100, 'y': 100}, 
        {'x': 300, 'y': 150}, 
        {'x': 500, 'y': 50},  
        {'x': 700, 'y': 200}  
    ]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if (mouse_x - 400) ** 2 + (mouse_y - 300) ** 2 <= 50 ** 2: 
                    os.system('python "tugas akhir/materi1.py"')
                    running = False

        for cloud in clouds:
            cloud['x'] += 1
            if cloud['x'] > 800: 
                cloud['x'] = -100

        draw_background(screen, tree_image, clouds)
        draw_tree(screen, tree_image, -150, 120)  
        draw_tree(screen, tree_image, 450, 120) 
        draw_bush(screen, bush_image, -10, 470)
        draw_bush(screen, bush_image, 350, 470)
        draw_bush(screen, bush_image, 750, 470)
        draw_text(screen, "MARI BERKENALAN", 400, 150, title_font)
        draw_text(screen, "DENGAN HEWAN", 400, 180, title_font)
        draw_button(screen, "Mulai", 400, 300, 50, font)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
