"""
    generate password
"""
import random


def generate_password() -> str:
    """
        generate a random password of length 4
    :return:
    """
    generated_password = ""
    generator = random.Random()

    for i in range(1, 3):
        generated_password += generator.choice(seq=[
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "g", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "G", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "z"
        ])

    for i in range(1, 3):
        generated_password += str(generator.randint(0, 9))

    return generated_password
