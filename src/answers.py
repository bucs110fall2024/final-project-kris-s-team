from lives import Lives

class Answers:
    def __init__(self, answers, false_answers=[], user_choice="choice"):
        self.answer = answers
        self.fake = false_answers
        self.user_choice = ""
    
    def points(self, score=0):
        self.score = score
        self.x = 1
        self.y = 1
        if self.user_choice == self.answer:
            score += 10
        elif self.user_choice in self.fake:
            score -= 5
            Lives.deduct()
        
        
    
    