import pygame
import random
import pygame_menu
import pygame_menu.events
import pygame_menu.locals
from src.button import Button
from src.trivia import Trivia


BG_COLOR = (211, 211, 211)




class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    pygame.event.pump()
    self.screen = pygame.display.set_mode()
    width, height = pygame.display.get_window_size()
    self.background = pygame.Surface((width, height))
    self.background.fill(BG_COLOR)
    
    
    
    self.menu = pygame_menu.Menu("Menu", width-20, height/2, position=(10, 10))
    self.menu.add.label("Lifeline Trivia", max_char=-1)
    self.menu.add.button("Start", self.start_game)
    self.menu.add.button("Quit", pygame_menu.events.EXIT)
    
    
    self.button = Button(x=50, y=self.menu.get_rect().bottom + 10)
    
    rec = pygame.Rect(50, 600, 1000, 200)
    self.rec = pygame.draw.rect(self.screen, (0, 0, 0), rec)
    self.screen.blit(self.rec)
    pygame.display.flip()
    
    self.state = "menu"
    
  def mainloop(self):
    #select state loop
    
    while True:
      if self.state == "menu":
        self.menuloop()
      elif self.state == "game":
        self.gameloop()
  
  ### below are some sample loop states ###

  def menuloop(self):
    
    while self.state == "menu":
      if self.menu.is_enabled():
        self.menu.update(pygame.event.get())
        self.menu.draw(self.screen)
        if(False): self.state = "game"
      pygame.display.update()
      pygame.display.flip()
        
      #event loop

      #update data

      #redraw
      
  def gameloop(self):

    while self.state == "game":
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.state = "menu"
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            self.state = "menu"
      triv = Trivia()
      data = triv.get()

      
      # question_box = pygame.Rect()
      # question_box.center

      # for options in data:
      #   answers = [options["incorrect_answers"]] + [options["correct_answer"]]
      #   random.shuffle(answers)
      #   ans_1 = Button(x=100, y=100, width=50, height=25, text="hi")
      
      
      self.screen.blit(self.background, (0,0))
      
      pygame.display.update()
      pygame.display.flip()
      #event loop

      #update data

      #redraw
    
  
  def start_game(self):
    self.state = "game"
  def gameoverloop(self):
      #event loop
      pass

      #update data

      #redraw
