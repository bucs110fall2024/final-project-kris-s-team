import requests
import random

# Proxy class
class Trivia:

    def __init__(self, category=9, amount=1):
        self.url = f'https://opentdb.com/api.php?amount={amount}&category={category}&difficulty=medium&type=multiple'

    def get(self):
        r = requests.get(self.url)
        response = r.json()
        if response.get("results"):
            return response["results"]
        else:
            return None

    def change_category(self, category):
        pass
        #self.url = #...


def main():
    tapi = Trivia()
    results = tapi.get()
    for trivia in results:
        #combine the incorrect and corrects into a single array
        answers = trivia['incorrect_answers'] + [trivia['correct_answer']]

        #shuffle the array
        random.shuffle(answers)
        print(f"{trivia['question']} -- Please select the correct answer\n===")

        #display all possible answers
        for i, a in enumerate(answers):
            print(f"{i}] {a}")

        #ask the user for their choice
        choice = int(input(":"))
        if answers[choice] == trivia['correct_answer']:
            print("correct, I guess.")
        else:
            print(f"Actually, {trivia['correct_answer']}")
main()        