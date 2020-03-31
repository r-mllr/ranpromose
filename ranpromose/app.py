# app.py
from .resources.sequence import generate_sequence


class Ranpromose:

    @staticmethod
    def run():
        generate_sequence(5, 50, 8, 2, 6, 2, 15)
        print("Hello World!")
