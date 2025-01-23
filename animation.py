import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Fling Balls with Boundaries and Smaller Balls')

# Ball class
class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = 0  # Horizontal speed
        self.speed_y = 0  # Vertical speed
        self.gravity = 0.2  # Gravity strength
        self.bounce_factor = -0.7  # Bounce elasticity
        self.is_dragging = False  # Is the ball being dragged?
        self.mouse_offset_x = 0
        self.mouse_offset_y = 0
        self.previous_mouse_x = 0
        self.previous_mouse_y = 0

    def apply_gravity(self):
        # Apply gravity and vertical speed
        self.speed_y += self.gravity
        self.y += self.speed_y

    def check_bounce(self, ground_level, screen_width):
        # Bounce off the ground
        if self.y >= ground_level:
            self.y = ground_level
            self.speed_y *= self.bounce_factor

        # Bounce off the left or right edges
        if self.x + self.radius > screen_width:
            self.x = screen_width - self.radius
            self.speed_x *= self.bounce_factor
        elif self.x - self.radius < 0:
            self.x = self.radius
            self.speed_x *= self.bounce_factor

    def move_with_mouse(self, mouse_x, mouse_y):
        # Update ball position while dragging
        self.x = mouse_x + self.mouse_offset_x
        self.y = mouse_y + self.mouse_offset_y

    def fling(self, mouse_x, mouse_y):
        # Fling the ball with calculated speed based on mouse movement
        delta_x = mouse_x - self.previous_mouse_x  # Horizontal movement
        delta_y = mouse_y - self.previous_mouse_y  # Vertical movement
        self.speed_x = delta_x * 0.2  # Horizontal speed multiplier
        self.speed_y = delta_y * 0.2  # Vertical speed multiplier

    def update(self):
        self.apply_gravity()
        self.check_bounce(screen_height - self.radius, screen_width)

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Initialize the large ball and smaller balls
large_ball = Ball(400, 300, 40, (255, 0, 0))  # Red large ball
smaller_balls = []

# Create 10 smaller balls with random properties
for _ in range(10):
    radius = random.randint(10, 20)
    x = random.randint(radius, screen_width - radius)
    y = random.randint(radius, screen_height - radius)
    color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    smaller_balls.append(Ball(x, y, radius, color))

balls = [large_ball] + smaller_balls  # Add the large ball to the list

# Set up the clock for frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for ball in balls:
                if (mouse_x - ball.x)**2 + (mouse_y - ball.y)**2 <= ball.radius**2:
                    ball.is_dragging = True
                    ball.mouse_offset_x = ball.x - mouse_x
                    ball.mouse_offset_y = ball.y - mouse_y
                    ball.previous_mouse_x = mouse_x
                    ball.previous_mouse_y = mouse_y
                    ball.speed_x = 0
                    ball.speed_y = 0

        if event.type == pygame.MOUSEBUTTONUP:
            for ball in balls:
                if ball.is_dragging:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    ball.fling(mouse_x, mouse_y)  # Fling the ball based on movement
                    ball.is_dragging = False

        if event.type == pygame.MOUSEMOTION:
            for ball in balls:
                if ball.is_dragging:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    ball.move_with_mouse(mouse_x, mouse_y)
                    ball.previous_mouse_x = mouse_x
                    ball.previous_mouse_y = mouse_y

    # Update all balls and apply physics
    for ball in balls:
        if not ball.is_dragging:
            ball.update()

    # Fill the screen with a color (background)
    screen.fill((0, 0, 0))  # Black background

    # Draw all the balls
    for ball in balls:
        ball.draw()

    # Update the display
    pygame.display.flip()

    # Set the frame rate (60 frames per second)
    clock.tick(60)
