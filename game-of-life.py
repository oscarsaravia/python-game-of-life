import pygame
import random

BLACK = (0, 0, 0, 0)
WHITE = (255, 255, 255, 255)

class Life(object):
  def __init__(self, screen):
    self.first_render = True
    self.set_width = 500
    self.set_height = 500
    _, _, self.width, self.height = screen.get_rect()
    self.screen = screen

  def pixel(self, x, y, color=WHITE):
    self.screen.set_at((x, y), color)

  def copy(self):
    self.prev_turn = self.screen.copy()

  def figure(self):
    self.pixel(100, 100)
    self.pixel(101, 100)
    self.pixel(102, 100)
    self.pixel(106, 100)
    self.pixel(107, 100)
    self.pixel(108, 100)
    self.pixel(98, 97)
    self.pixel(98, 96)
    self.pixel(98, 95)
    self.pixel(103, 97)
    self.pixel(103, 96)
    self.pixel(103, 95)
    self.pixel(105, 97)
    self.pixel(105, 96)
    self.pixel(105, 95)
    self.pixel(110, 97)
    self.pixel(110, 96)
    self.pixel(110, 95)
    self.pixel(100, 95)
    self.pixel(101, 95)
    self.pixel(102, 95)
  
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
      # self.createWindow()
      self.figure();
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
              self.pixel(i, k, BLACK)
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
  pygame.time.delay(500)
  r.render()
  r.copy()
  pygame.display.flip()

