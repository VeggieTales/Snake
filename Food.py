import pygame

""" A class to make food blocks for the snake to eat. """

class FoodBlock(pygame.sprite.Sprite):

    def __init__(self, colour, width, height):
        #call the parent class (Sprite)
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(colour)

        #draws the sprite
        pygame.draw.rect(self.image, colour, [0, 0, width, height])

        #creates rectangle object with dimensions of the image
        self.rect = self.image.get_rect()
