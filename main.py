import random
from art import logo, vs
from data import data
import os

def clear_terminal():
   os.system("cls" if os.name == "nt" else "clear")
print(logo)

def show_comparison(a, b):
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")

def get_user_choice():
    return input("Who has more followers? Type 'A' or 'B': ").lower()
