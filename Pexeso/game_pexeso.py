import random
import pygame
import time
from Card import Card

BOARD_SIZE_X = 8
BOARD_SIZE_Y = 8
WINDOW_SIZE_X = 800
WINDOW_SIZE_Y = 800

IMAGE_SIZE = 100
IMAGE_MARGIN = 2

N_OF_CARDS = int(BOARD_SIZE_X * BOARD_SIZE_Y / 2)
CHAR_OFFSET = 96
COLLECTED_CARD = 42

board = [[Card() for _ in range(BOARD_SIZE_Y)] for _ in range(BOARD_SIZE_X)]
cards = [x for x in range(1, N_OF_CARDS + 1)] * 2

def createBoard() -> list[list[int]]:   
     i = 0
     random.shuffle(cards)    
     for x in range(BOARD_SIZE_X):
          for y in range(BOARD_SIZE_Y):
               board[x][y].card_id = cards[i]
               board[x][y].addImage()
               i+=1   
     return board


if __name__ == "__main__":
     random.seed(1234)
     pygame.init()
     cliks = 0
     clicked = []
     end_of_game = N_OF_CARDS
     window = pygame.display.set_mode((WINDOW_SIZE_X + (BOARD_SIZE_X * IMAGE_MARGIN - 1), WINDOW_SIZE_Y + (BOARD_SIZE_X * IMAGE_MARGIN - 1)))
     clock = pygame.time.Clock()

     board = createBoard()
     while (end_of_game):
          clock.tick(100)

          if cliks == 2:
               card_1 = board[clicked[0][0]][clicked[0][1]]
               card_2 = board[clicked[1][0]][clicked[1][1]]

               if card_1 == card_2:
                    cliks-= 1
                    clicked.pop()
                    continue

               if card_1.card_id == COLLECTED_CARD:
                    cliks-= 1
                    clicked.pop(0)
                    continue

               if card_2.card_id == COLLECTED_CARD:
                    cliks-= 1
                    clicked.pop()
                    continue

               if card_1.card_id == card_2.card_id:
                    card_1.card_id = COLLECTED_CARD
                    card_1.front = pygame.image.load("images/empty.png")  
                    card_1.back = pygame.image.load("images/empty.png")  
                    card_2.card_id = COLLECTED_CARD
                    card_2.front = pygame.image.load("images/empty.png")  
                    card_2.back = pygame.image.load("images/empty.png") 
                    end_of_game -= 1               
               clicked.clear()
               cliks = 0
               card_1.clicked = False
               card_2.clicked = False 
               time.sleep(1)
               
          for event in pygame.event.get():   
               if event.type == pygame.MOUSEBUTTONDOWN:    
                    if event.button == 1:
                         pos_x = int(event.pos[1] // (IMAGE_SIZE + IMAGE_MARGIN))
                         pos_y = int(event.pos[0] // (IMAGE_SIZE + IMAGE_MARGIN))
                         board[pos_x][pos_y].clicked = True
                         clicked.append((pos_x, pos_y))
                         cliks += 1                        

          window.fill(0)
          for iy, rowOfCells in enumerate(board):
               for ix, cell in enumerate(rowOfCells):        
                  image = cell.front if cell.clicked else cell.back
                  imgae_rect = ((IMAGE_MARGIN + IMAGE_SIZE) * ix + IMAGE_MARGIN, (IMAGE_MARGIN + IMAGE_SIZE) * iy + IMAGE_MARGIN)
                  window.blit(image, imgae_rect)
          pygame.display.flip()

     pygame.quit()
     exit()
