#Создайте программу для игры с конфетами человек против человека.
#Условие задачи:
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28
# конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько
# конфет нужно взять первому игроку, чтобы забрать все конфеты у своего
# конкурента?
# a) Добавьте игру против бота
# b) Подумайте, как наделить бота "интеллектом"
import os
os.system('cls')
import random
from tokenize import String

greeting = ('Чтобы начать голодные игры, необходимо решить, \
    \nВ какой режим Вы хотите играть? \
        \nЕсли с Игроком2: введите 1, если с Ботом введите 2 \
            \nесли хотите почувствовать себя ничтожеством - введите 3 (BigBoss)')
n = 2021
m = 28          

messages = ['Ваша очередь', 'возьмите конфеты', 
            'сколько конфет возьмёте?', 'Ваш ход']


def play_game(n, m, players, messages, number_player):
    while n > 0:
        print(f'{players[number_player%2]}, {random.choice(messages)}')
        move = int(input())
        while move > n or move > m or move <= 0:
            print(f'Можно взять не более {m} конфет, у нас всего {n} конфет, 0 брать нельзя')
            move = int(input())
        n = n - move
        if n > 0: print(f'Осталось {n} конфет')
        else: print('Все конфеты разобраны.')
        number_player +=1
    return players[not number_player%2]

def play_game_bot_hard(n, m, players, messages, number_player):
    while n > 0:
        if number_player%2 != 0:
            if n > m:
                move = n % (m + 1)
            else:
                move = n
            print(f'Я беру {move} конфет')
        else:
            print(f'{players[number_player%2]}, {random.choice(messages)}')
            move = int(input())
            while move > n or move > m or move <= 0:
                print(f'Можно взять не более {m} конфет, у нас всего {n} конфет, 0 брать нельзя')
                move = int(input())
        n = n - move
        if n > 0: print(f'Осталось {n} конфет')
        else: print('Все конфеты разобраны.')
        number_player +=1
    return players[not number_player%2]

def play_game_bot(n, m, players, messages, number_player):
    while n > 0:
        if number_player%2 != 0:
            if n > m:
                move = random.randint(1, m)
            else:
                move = 1
            print(f'Я беру {move} конфет')
        else:
            print(f'{players[number_player%2]}, {random.choice(messages)}')
            move = int(input())
            while move > n or move > m or move <= 0:
                print(f'Можно взять не более {m} конфет, у нас всего {n} конфет, 0 брать нельзя')
                move = int(input())
        n = n - move
        if n > 0: print(f'Осталось {n} конфет')
        else: print('Все конфеты разобраны.')
        number_player +=1
    return players[not number_player%2]

def choice(players):
    count = 0
    print(f'{players[0]} А теперь жеребьевка!!! Выберите: если орел введите 1, если решка 2')
    choice = input()
    while choice not in '12' or choice == '':
        print('Введено неверное значение. Выберите 1 (ОРЕЛ) или 2 (РЕШКА)')
        choice = input()    
    fortune = ['1', '2']
    li = random.choice(fortune)
    print('Монета взлетает в воздух, опускается на землю, и там....')
    if choice == li and li == '1':
        print('Удача на Вашей стороне,выпал орел, начинаете первым')
    elif choice == li and li == '2':
        print('Удача на Вашей стороне,выпала решка, начинаете первым')
    else:
        count = 1
        print(f'Вы видите другую сторону монеты, первым ходит соперник')
    return count

print(greeting)
num = input()
while num not in '123' or num == '':
    print('Введено неверное значение. Выберите 1, 2 или 3')
    num = input()
if num == '1':
    player1 = input('Давайте познакомися. Первый игрок, как к Вам можно обращаться?\n')
    player2 = input('Второй игрок, и Вы представьтесь, пожалуйста\n')
    players = [player1, player2]
    number_player = choice(players)
    winer = play_game(n, m, players, messages, number_player)
if num == '2':
    player1 = input('Давайте познакомися. Первый игрок, как к Вам можно обращаться?\n')
    print(f'Привет {player1}!!! А меня зовут Бот.')
    bot = 'Бот'
    players = [player1, bot]
    number_player = choice(players)
    winer = play_game_bot(n, m, players, messages, number_player)
if num == '3':
    player1 = input('Давайте познакомися. Первый игрок, как к Вам можно обращаться?\n')
    print(f'Привет {player1}!!! А меня зовут BigBoss. И я здесь, чтобы унизить тебя!!!')
    bot = 'BigBoss'
    players = [player1, bot]
    number_player = choice(players)
    winer = play_game_bot_hard(n, m, players, messages, number_player)

print(f'Ииииии победитель, это {winer}! Ему достаются все конфеты!')