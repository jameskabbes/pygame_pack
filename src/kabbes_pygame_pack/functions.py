import pygame
import math
import numpy as np

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

#def draw_rect(screen, color, coords):
def deg_to_rad(deg):
    return math.pi * deg / 180

def rad_to_deg(rad):
    return rad * 180 / math.pi

def draw_sqaure(screen, color, center_coords, length):


    coords = []
    coords.append([center_coords[0] + length /2, center_coords[1] + length/2])
    coords.append([center_coords[0] + length /2, center_coords[1] - length/2])
    coords.append([center_coords[0] - length /2, center_coords[1] - length/2])
    coords.append([center_coords[0] - length /2, center_coords[1] + length/2])
    draw_polygon(screen, color, coords)

def detect_collision(x1,y1,x2,y2, buffer):
    dist = get_dist(x1,y1,x2,y2)
    if dist < buffer:
        return True
    return False

def get_dist(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**.5

def angle_from_1_to_2(x1,y1,x2,y2):

    dy = y2 - y1
    dx = x2 - x1
    theta = math.atan2(dy,dx)
    return theta

def polar_to_cart(r, radians):

    x = r * math.cos(radians)
    y = r * math.sin(radians)
    return x, y


def get_angle_of_vel(vx, vy):

    try:
        angle = math.atan(vy / vx)
    except:
        if vy > 0:
            return math.pi / 2

        elif vy < 0:
            return math.pi * 3 / 2
        else:
            return False

    return angle

def cap_speed(vx, vy, max_speed):

    v = (vx**2 + vy**2) ** 0.5

    theta = get_angle_of_vel(vx, vy)
    if max_speed < v:
        v = max_speed

    vx, vy = polar_to_cart(v, theta)
    return vx, vy


def rotate_values(x, y, radians):
        #Rotation matrix
        # [cos sin] * [ vx ]
        # [-sin cos]  [ vy ]
    xp = math.cos(radians)*x + math.sin(radians)*y
    yp = -1 * math.sin(radians)*x + math.cos(radians)*y
    return xp, yp
