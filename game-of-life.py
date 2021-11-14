import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Life(object):
  def __init__(self, screen):
    self.first_render = True
    self.set_width = 500
    self.set_height = 500
    _, _, self.width, self.height = screen.get_rect()
    self.screen = screen

  def pixel(self, x, y):
    self.screen.set_at((x, y), (255, 255, 255))

  def copy(self):
    self.prev_turn = self.screen.copy()
  
  def createWindow(self):
    for i in range(0, 1000):
      x = random.randint(0, self.set_width)
      y = random.randint(0, self.set_height)
      self.pixel(x, y)

  def fatpixel(self, x, y):
    self.screen.set_at((x, y), (255, 255, 255))
    self.screen.set_at((x + 1, y + 1), (255, 255, 255))
    self.screen.set_at((x + 1, y - 1), (255, 255, 255))
    self.screen.set_at((x + 1, y), (255, 255, 255))
    self.screen.set_at((x - 1, y + 1), (255, 255, 255))
    self.screen.set_at((x - 1, y - 1), (255, 255, 255))
    self.screen.set_at((x - 1, y), (255, 255, 255))
    self.screen.set_at((x, y + 1), (255, 255, 255))
    self.screen.set_at((x, y - 1), (255, 255, 255))

  def render(self):
    if self.first_render:
      self.createWindow()
      self.first_render = False
    else:
      for i in range(1, self.width - 1):
        for k in range(1, self.height - 1):
          counter = 0
          if self.prev_turn.get_at((i - 1, k)) == WHITE:
            counter += 1
          if self.prev_turn.get_at((i + 1, k)) == WHITE:
            counter += 1
          if self.prev_turn.get_at((i, k - 1)) == WHITE:
            counter += 1
          if self.prev_turn.get_at((i, k + 1)) == WHITE:
            counter += 1
          if self.prev_turn.get_at((i - 1, k + 1)) == WHITE:
            counter += 1
          if self.prev_turn.get_at((i + 1, k + 1)) == WHITE:
            counter += 1
          if self.prev_turn.get_at((i - 1, k - 1)) == WHITE:
            counter += 1
          if self.prev_turn.get_at((i + 1, k - 1)) == WHITE:
            counter += 1
          if (self.prev_turn.get_at((i, k)) == (255, 255, 255, 255)):
            if counter < 2 or counter not in [2, 3]:
              self.pixel(i, k)
            else:
              self.pixel(i, k)
          elif counter == 3:
            self.pixel(i, k)
          counter = 0

pygame.init()
screen = pygame.display.set_mode((500, 500))
r = Life(screen)
running = True

while running:
  pygame.event.pump()
  pygame.time.delay(300)
  r.copy()
  r.render()
  pygame.display.flip()

