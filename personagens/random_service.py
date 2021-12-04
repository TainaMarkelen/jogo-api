import random

class RandomService:
    def get_random_number(self, min, max):
        return random.randint(min, max)