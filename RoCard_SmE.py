from random import shuffle
from os import system
from time import sleep

LETTERS = ["A","B","C","D","E","F","G","H","I","J"]
NUMBERS = ["1","2","3","4","5","6","7","8","9","10"]
VARIANTS = [
    "😈 ", "😞 ", "😀 ", "😠 ", "😡 ", "😢 ", "😣 ", "😤 ", "😥 ", "😦 ",
    "😧 ", "😨 ", "😩 ", "😪 ", "😫 ", "😬 ", "😭 ", "😮 ", "😯 ", "😰 ",
    "😱 ", "😲 ", "😳 ", "😴 ", "😵 ", "😶 ", "😷 ", "😸 ", "😹 ", "😺 ",
    "😻 ", "😼 ", "😽 ", "😅 ", "😿 ", "🙀 ", "🙁 ", "🙂 ", "🙃 ", "🙄 ",
    "🙅 ", "🙆 ", "🙇 ", "😇 ", "🙉 ", "🙊 ", "🙋 ", "🙌 ", "🙍 ", "🙎 "]

#функції
# виводимо поле на екран
def game_table(cord1="__", cord2="__"):
    print("   ",end="")
    for number in NUMBERS[:game_size]:
        print(f"{number}  ", end="")
    print()
    for letter in LETTERS[:game_size]:
        print(letter,end=" ")
        for indx, cell in enumerate(game_answers[letter]):
            if (letter == cord1[0].upper() and str(indx+1) == cord1[1])\
                    or (letter == cord2[0].upper() and str(indx+1) == cord2[1]):
                print(f"{cell[1]}", end="")
            else:
                print(f"{cell[0]}", end="")
        print()
# перевіряємо чи співпадають елементи
def is_guessed(cord1, cord2):
    if game_answers[cord1[0].upper()][int(cord1[1])-1][1] == game_answers[cord2[0].upper()][int(cord2[1])-1][1]:
        game_answers[cord1[0].upper()][int(cord1[1]) - 1][0] = game_answers[cord1[0].upper()][int(cord1[1]) - 1][1]
        game_answers[cord2[0].upper()][int(cord2[1]) - 1][0] = game_answers[cord2[0].upper()][int(cord2[1]) - 1][1]
        print("You've guessed!")
        return True
    else:
        print("Try again")
        return False
#отримуємо і валідуємо координату
def walidate_cord(no=""):
    while True:
        cord = input(f"Please enter the coordinates of the {no} the cell (in 'A1' format): ")
        if len(cord) > 1 and cord[0].upper() in LETTERS[:game_size] and cord[1] in NUMBERS[:game_size]:
            return cord
        else:
            print("Try again.")
#затримка і очищення
def tclear(time=0):
    sleep(time)
    system("cls")

#привітання
tclear()
print("Hello, dear friend!")
tclear(3)
print("You are going to play a fun game with cards.")
tclear(4)
print("But first, let`s pick the game size (bigger number -> harder game).")

#вибір розміру, валідація
while True:
    game_size = input("Pick one of the numbers(4, 6, 8, 10): ")
    if game_size.isdigit() and 4 <= int(game_size) <= 10 and not int(game_size)%2:
        game_size = int(game_size)
        tclear()
        break
    tclear()
    print("Please try again.")

#виводмо всі можливі картки
print("Nice!\nHere are all cards you can find in the cells:")
for variant in VARIANTS[:game_size**2//2]:
    print(variant, end=" ")
print()

#список з усіма можливими координатами перемішаними
cordinates = [[x,y] for x in range(game_size) for y in range(game_size)]
shuffle(cordinates)

#список з відповідями
game_answers = {x:[[" X "] for y in NUMBERS[:game_size]] for x in LETTERS[:game_size]}

#додаємо відповіді
n = 0
for X, Y in cordinates:
    game_answers[LETTERS[X]][Y].append(VARIANTS[int(n)])
    n += 0.5

#основна гра
guesses_counter = 0
turn_counter = 0
while guesses_counter < game_size**2//2:
    tclear(3)
    game_table()
    while True:
        cordx = walidate_cord("first")
        cordy = walidate_cord("second")
        if cordx[:2].upper() != cordy[:2].upper():
            break
    game_table(cordx,cordy)
    if is_guessed(cordx,cordy):
        guesses_counter += 1
    turn_counter += 1
    if cordx == "A1XX" and cordy == "B1XX":
        break
tclear(3)
print("Congratulations!!!")
tclear(3)
print("You've won!")
tclear(3)
print(f"It took {turn_counter} turns!")
tclear(3)
print("your reward is...")
tclear(3)
while True:
    print('''
    watch a camel walking
          _    _                       
         /  \/  \_/ °=      
     °\/(__________/    
         /      \       
        /_       \_''')
    tclear(1)
    print('''
    watch a camel walking
          _    _                       
         /  \/  \_/ °=      
     °\/(__________/    
          \     \       
          /_    /_''')
    tclear(1)
    print('''
    watch a camel walking
          _    _                       
         /  \/  \_/ °=      
     °\/(__________/    
          \     /       
           \_  /_''')
    tclear(1)
    print('''
    watch a camel walking
          _    _                       
         /  \/  \_/ °=      
     °\/(__________/    
          \     \       
          /_    /_''')
    tclear(1)
