# Import the system library and pygame library
import sys, pygame
# Initalize pygame
pygame.init()

# Setting Window Size
size = width, height = 650, 350
# Creating a display window with size
screen = pygame.display.set_mode(size)

# loading a ball image
ball = pygame.image.load("NOOOB.gif")
# Measure the ball size in rectangle
ballrect = ball.get_rect()

# Setting the Ball speed
speed = [1, 1]
# Setting color (black; 0, 0, 0)
black = 0, 0, 0

# Makes the game repeating
while True:
  # when the 'X', exit button pressed, game terminates
  for event in pygame.event.get():
    if(event.type == pygame.QUIT):
      sys.exit()
      
  # Changing ball direction after bouncing
  ballrect = ballrect.move(speed)

  if(ballrect.left < 0 or ballrect.right > width):
    speed[0] = -speed[0]
  if(ballrect.top < 0 or ballrect.bottom > height):
    speed[1] = -speed[1]
  # Setting background color (solid black or random color)
  screen.fill(black)
  # Updating the screen and the ball position
  screen.blit(ball, ballrect)
  pygame.display.flip() 