import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game settings
WIDTH = 400
HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Bird settings
BIRD_WIDTH = 40
BIRD_HEIGHT = 40
bird_x = 50
bird_y = HEIGHT // 2
bird_velocity = 0
gravity = 0.5
flap_strength = -10

# Pipe settings
PIPE_WIDTH = 60
PIPE_GAP = 150
pipe_velocity = 5
pipe_frequency = 1500  # milliseconds

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load bird image (can replace with your own image)
bird = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
bird.fill(BLUE)

#
