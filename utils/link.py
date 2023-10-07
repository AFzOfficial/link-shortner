import random
import string

def generate_random_string() -> str:
    str_ = ""
    for _ in range(8):
        str_ += random.choice(string.ascii_letters)
    
    return str_
