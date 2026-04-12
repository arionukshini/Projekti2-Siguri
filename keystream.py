import random

def generate_keystream(length, seed):
    random.seed(seed)
    return [random.randint(0, 255) for _ in range(length)]