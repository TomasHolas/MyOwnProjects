import pygame

IMAGE_SIZE = 100

class Card():
     def __init__(self) -> None:
          self.clicked = False
          self.card_id = 42
          self.front = None       
          self.back = None

     def __str__(self) -> str:
          return 'Cell id: ' + str(self.card_id) 

     def __repr__(self) -> str:
          return 'Cell id: ' + str(self.card_id) 

     def addImage(self):
          self.front = pygame.image.load("images/" + str(self.card_id) + ".png")         
          self.front = pygame.transform.scale(self.front, (IMAGE_SIZE, IMAGE_SIZE))
          self.back = pygame.image.load("images/back.png")        
          self.back = pygame.transform.scale(self.back, (IMAGE_SIZE, IMAGE_SIZE))