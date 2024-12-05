import pygame

class Background(pygame.sprite.Sprite):
  def __init__(self, image_file):
    super().__init__()
    self.image = pygame.image.load('media/pixel-art-illustration-space-background-pixelated-space-background-space-background-nebula-pixelated-for-the-pixel-art-game-and-icon-for-website-and-game-old-school-retro-vector.JPG').convert()
    self.rect = self.image.get_rect()

  def draw(self, screen):
    screen.blit(self.image, self.rect)