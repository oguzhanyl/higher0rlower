import random
from art import logo, vs
from data import data
import os

# Terminal ekranını temizleyen fonksiyon:
def clear_terminal():
   os.system("cls" if os.name == "nt" else "clear")
print(logo)

# Her tur için yazılan kalıp cümleler:
def show_comparison(a, b):
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")

# Kullanıcı tercihini temsil eden fonksiyon:
def get_user_choice():
    return input("Who has more followers? Type 'A' or 'B': ").lower()

# Her tur için fonksiyon:
def play_round():
    a = random.choice(data)
    b = random.choice(data)
    # Rastgele seçildiği halde aynı gelirse b değişkenini bir kez daha rastgele döndür:
    if a == b:
        b = random.choice(data)
    show_comparison(a, b)
    user_choice = get_user_choice()
    
    # a ve b sözlüklerinden takipçi sayılarını çekip karşılaştır:
    if a['follower_count'] > b['follower_count']:
        return user_choice == 'a'
    else:
        return user_choice == 'b'

# Oyunun fonksiyonu:
def game():
    score = 0
    game_over = True
    
    while game_over:
        is_correct = play_round()
        if is_correct:
            score += 1
            clear_terminal()
            print(logo)
            print(f"You're right! Current score: {score}.")
        else:
            clear_terminal()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_over = False

game()