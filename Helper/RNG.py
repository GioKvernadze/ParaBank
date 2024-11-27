import random
import string

def generate_random_string():
    length = random.randint(4, 8)
    characters = string.ascii_letters
    random_strings = ''.join(random.choice(characters) for _ in range(length))
    return random_strings

def generate_random_number():
    length = random.randint(4, 12)
    min_value = 10**(length - 1)
    max_value = 10**length - 1
    random_numbers = random.randint(min_value, max_value)
    return random_numbers


