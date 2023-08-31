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



# İkinci karşılaştırdığımızın ilk sıraya geldiği senaryonun kodu

# ***********************************************

# from data import data
# import random
# from art import logo, vs
# import os

# def get_random_account():
#   """Get data from random account"""
#   return random.choice(data)

# def format_data(account):
#   """Format account into printable format: name, description and country"""
#   name = account["name"]
#   description = account["description"]
#   country = account["country"]
#   # print(f'{name}: {account["follower_count"]}')
#   return f"{name}, a {description}, from {country}"

# def check_answer(guess, a_followers, b_followers):
#   """Checks followers against user's guess 
#   and returns True if they got it right.
#   Or False if they got it wrong.""" 
#   if a_followers > b_followers:
#     return guess == "a"
#   else:
#     return guess == "b"


# def game():
#     print(logo)
#     score = 0
#     game_should_continue = True
#     account_a = get_random_account()
#     account_b = get_random_account()

#     while game_should_continue:
#         account_a = account_b
#         account_b = get_random_account()

#     while account_a == account_b:
#         account_b = get_random_account()

#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}.")
    
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     clear_terminal()
#     print(logo)
#     if is_correct:
#       score += 1
#       print(f"You're right! Current score: {score}.")
#     else:
#       game_should_continue = False
#       print(f"Sorry, that's wrong. Final score: {score}")

# game()