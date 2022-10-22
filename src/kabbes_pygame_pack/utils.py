import pygame

def get_screen(length, width):
    '''Returns the screen with length and width'''
    return pygame.display.set_mode((length, width))

def flip_screen():
    '''Updates the screen'''
    pygame.display.flip()

def fill_screen(screen, color):
    screen.fill(color)

def capture_screen( screen, save_path ):
    size = screen.get_size()
    image = pygame.Surface( size )
    image.blit( screen, (0,0), ((0,0),size) )
    pygame.image.save( image, save_path )

def set_pixel_color(screen, x, y, color):
    screen.set_at((x,y), color)

def draw_circle(screen, color, coords, radius):
    x = int(coords[0])
    y = int(coords[1])
    pygame.draw.circle(screen, color, [x,y], int(radius))

def draw_polygon(screen, color, coords):
    pygame.draw.polygon(screen, color, coords)

def draw_sqaure(screen, color, center_coords, length):

    coords = []
    coords.append([center_coords[0] + length /2, center_coords[1] + length/2])
    coords.append([center_coords[0] + length /2, center_coords[1] - length/2])
    coords.append([center_coords[0] - length /2, center_coords[1] - length/2])
    coords.append([center_coords[0] - length /2, center_coords[1] + length/2])
    draw_polygon(screen, color, coords)




