import requests

class Trivia:
    def __init__(self, category=9, amount=50):
        self.url = f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty=medium&type=multiple"
        
    def get(self):
        r = requests.get(self.url)
        triv_data = r.json()
        
        if triv_data.get("results"):
            return triv_data["results"]
        else:
            return None

