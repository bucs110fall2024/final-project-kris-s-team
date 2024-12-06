import pygame
import html
import random
import pygame_menu
from src.answers import Answers
from src.trivia import Trivia
from src.lives import Lives


BG_COLOR = (211, 211, 211)

class Controller:
  
  def __init__(self):
    
    pygame.init()
    pygame.event.pump()
    self.screen = pygame.display.set_mode(size=(1250, 750))
    width, height = pygame.display.get_window_size()
    self.background = pygame.Surface((width, height))
    self.background.fill(BG_COLOR)
    
    
    
    self.menu = pygame_menu.Menu("Menu", width-20, height/2, position=(10, 10))
    self.menu.add.label("Trivia Master", max_char=-1)
    self.menu.add.button("Start", self.start_game)
    self.menu.add.button("Quit", pygame_menu.events.EXIT)
    
    self.pause_menu = pygame_menu.Menu("Pause", width-20, height/2, position=(10,10))
    self.pause_menu.add.label("Game Paused", max_char=-1)
    self.pause_menu.add.button("Quit", pygame_menu.events.EXIT)
    
    self.triv = Trivia()
    self.lives = Lives(x=50, y=650, max_lives=3)
    self.score = 0
    
    self.state = "menu"
    
  def mainloop(self):
    
    while True:
      if self.state == "menu":
        self.menuloop()
      elif self.state == "game":
        self.gameloop()
      elif self.state == "pause":
        self.pause_menu.mainloop(self.screen)
      elif self.state == "gameover":
        self.gameoverloop()
  

  def menuloop(self):
    
    while self.state == "menu":
      if self.menu.is_enabled():
        self.menu.update(pygame.event.get())
        self.menu.draw(self.screen)
      pygame.display.update()
      pygame.display.flip()
      
  def gameloop(self):
    
    while self.state == "game":
      
      data = self.triv.get()
      for trivia in data:
        
        question = html.unescape(trivia["question"])
        correct_ans = trivia["correct_answer"]
        choices = html.unescape(trivia["incorrect_answers"] + [correct_ans])
        random.shuffle(choices)
        choice_buttons = [
          Answers(200, 200 + i * 100, 800, 50, (255, 255, 255), answer)
          for i, answer in enumerate(choices)
        ]
        
        answered = False
        
        while not answered:
            
          self.screen.blit(self.background, (0,0))
          
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              self.state = "menu"
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_ESCAPE:
                self.state = "pause"
                return
              
            
              
            if not answered:
              
              for i in range(len(choice_buttons)):
                if choice_buttons[i].click(event):
                  if choices[i] == trivia["correct_answer"]:
                    print("Correct!")
                    self.score += 1
                  else:
                    print(f"Wrong! Correct Answer: {trivia["correct_answer"]}")
                    self.lives.deduct()
                    if self.lives.game_over():
                      self.state = "gameover"
                      return
                    
                  
                  answered = True
                  break
              
          font = pygame.font.SysFont(None, 24)
          question_surface = font.render(question, True, (0, 0, 0))
          question_rect = question_surface.get_rect(center=(self.screen.get_width() // 2, 100))
          self.screen.blit(question_surface, question_rect)
          
          for button in choice_buttons:
            button.draw(self.screen)
          
          self.lives.draw(self.screen)
          score_surface = font.render(f"Score: {self.score}", True, (0, 0, 0))
          self.screen.blit(score_surface, (1050, 650))
          
          pygame.display.update()
          pygame.display.flip()
        
      pygame.time.wait(5000)
    
  

        
  def start_game(self):
    self.state = "game"
    
  def gameoverloop(self):
    self.lives.reset()
    font = pygame.font.SysFont(None, 72)
    game_over_surface = font.render("Game Over!", True, (255, 0, 0))
    game_over_rect = game_over_surface.get_rect(center=(self.screen.get_width() // 2, 300))

    score_surface = font.render(f"Your Score: {self.score}", True, (0, 0, 0))
    score_rect = score_surface.get_rect(center=(self.screen.get_width() // 2, 400))

    self.screen.blit(self.background, (0, 0))
    self.screen.blit(game_over_surface, game_over_rect)
    self.screen.blit(score_surface, score_rect)
    pygame.display.update()
    pygame.display.flip()
    self.score = 0
    pygame.time.wait(3000)
    self.state = "menu"