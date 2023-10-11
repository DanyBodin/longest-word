import string
import random
import requests

class Game:
    """Define a grid"""
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = random.choices(string.ascii_uppercase, k=9)

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if not word:return False
        if len(word) > len(self.grid):return False
        for w in word:
            if word.count(w) == self.grid.count(w):return True
            else:return False

    def check_dict(self, word):
        dict_url = f'https://wagon-dictionary.herokuapp.com/{word}'
        dict_response = requests.get(dict_url)
        return dict_response.json()['found']

if __name__ == "__name__":
    newG = Game()
    print(newG.check_dict("cheval"))
