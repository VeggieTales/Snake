import pygame

""" A class that creates a snake and controls its movement """

class SnakeBody(pygame.sprite.Sprite):
    
    def __init__(self, colour, width, height):
        #call the parent class (Sprite)
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        #draws the sprite
        pygame.draw.rect(self.image, colour, [0, 0, width, height])

        #creates rectangle object with dimensions of the image
        self.rect = self.image.get_rect()

    def moveUp(self, speed):
        self.rect.y -= speed

    def moveDown(self, speed):
        self.rect.y += speed

    def moveRight(self, speed):
        self.rect.x += speed

    def moveLeft(self, speed):
        self.rect.x -= speed
        
