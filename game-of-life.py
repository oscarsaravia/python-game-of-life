import pygame
import random

class Life(object):
  def __init__(self, screen):
    _, _, self.width, self.height = screen.get_rect()
    self.screen = screen

  def clear(self):
    self.screen.fill((0, 0, 0))

  def pixel(self, x, y):
    self.screen.set_at((x, y), (255, 255, 255))

  def copy(self):
    self.prev_turn = self.screen.copy()
  
  def createWindow(self):
    # for i in range(0, 100):
    #   x = random.randint(10, 490)
    #   y = random.randint(10, 490)
    #   self.pixel(x, y)
      self.pixel(100, 100)

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
    for i in range(0, self.width):
      for k in range(0, self.height):
        counter = 0
        if self.screen.get_at((i, k)) == (255, 255, 255):
          print(i, k, ' estoy vivo')

pygame.init()
screen = pygame.display.set_mode((500, 500))

r = Life(screen)
while True:
  pygame.event.get()
  pygame.time.delay(1000)
  r.createWindow()
  r.copy()
  r.clear()
  r.render()

  pygame.display.flip()
