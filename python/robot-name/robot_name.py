import random
from string import ascii_uppercase
import time

class Robot:
    def __init__(self):
        self.name = random.choice(ascii_uppercase)+random.choice(ascii_uppercase)+str(random.randrange(100,999))
    def reset(self):
        random.seed(time.time())
        self.name = random.choice(ascii_uppercase)+random.choice(ascii_uppercase)+str(random.randrange(100,999))