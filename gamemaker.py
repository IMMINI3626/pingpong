import sys
import pygame
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255 ,255)
  
class Button:
  def __init__(self, text, x, y, w, h, fg, bg, action=None):
    self.is_click = False
    self.text = text
    self.pos = (x, y)
    self.size = (w, h)
    self.fg = fg
    self.bg = bg
    self.action = action

class Image:
  def __init__(self, img_path):
    self.img = pygame.image.load(img_path)
    self.size = self.img.get_size()
    self.w = self.size[0]
    self.h = self.size[1]
    

class GAMEMAKER:
  def __init__(self, display):
    self.small_font = pygame.font.Font("./NanumGothicExtraBold.ttf", 20)
    self.small_bold_font = pygame.font.Font("./NanumGothicExtraBold.ttf", 20)
    self.big_font = pygame.font.Font("./NanumGothicExtraBold.ttf", 40)
    self.big_bold_font = pygame.font.Font("./NanumGothicExtraBold.ttf", 40)
    self.clock = pygame.time.Clock()
    self.display = display

  def draw_text(self, font, text, pos, color):
    text = font.render(text, True, color)
    text_pos = text.get_rect()
    text_pos.center = pos
    self.display.blit(text, text_pos)

  def draw_button(self, button : Button):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    x, y = button.pos
    w, h = button.size
    if x < mouse[0] < x + w and y < mouse[1] < y + w:
        if click[0] == 1:
            button.is_click = True
        else:
            if button.is_click:
                button.action()
                button.is_click = False
    pygame.draw.rect(self.display, button.bg, (x,y,w,h))
    self.draw_text(self.small_bold_font, button.text, (x+w/2,y+h/2), button.fg)

  def draw_image(self, image:Image, x, y):
    self.display.blit(image, (x, y))

  def tick(self, FPS):
    pygame.display.update()
    self.clock.tick(FPS)