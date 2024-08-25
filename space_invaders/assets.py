# assets.py
import pygame
import os
from settings import WIDTH, HEIGHT

pygame.mixer.init()

def load_image(filename):
    try:
        return pygame.image.load(os.path.join("assets", filename))
    except pygame.error as e:
        print(f"Falha ao carregar a imagem {filename}: {e}")
        raise

def load_sound(filename):
    try:
        return pygame.mixer.Sound(os.path.join("sounds", filename))
    except pygame.error as e:
        print(f"Falha ao carregar o som {filename}: {e}")
        raise

# Carregando imagens dos assets
PIXEL_SHIP_RED_SMALL = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
PIXEL_SHIP_GREEN_SMALL = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
PIXEL_SHIP_BLUE_SMALL = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
PIXEL_SHIP_YELLOW = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

PIXEL_LASER_RED = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
PIXEL_LASER_GREEN = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
PIXEL_LASER_BLUE = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
PIXEL_LASER_YELLOW = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Carregando sons (se houver)
LASER_SOUND = pygame.mixer.Sound(os.path.join("sounds", "space-laser.wav"))
EXPLOSION_SOUND = pygame.mixer.Sound(os.path.join("sounds", "explosion.wav"))

# Carregar imagem de fundo
BG = pygame.transform.scale(load_image("background-black.png"), (WIDTH, HEIGHT))
