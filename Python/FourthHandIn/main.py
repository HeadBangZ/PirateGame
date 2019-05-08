from dice import Dice
import random

players = []
placeholder = []
RGB = []

def pick_color():
    for i in range(0, 3):
        color = int(input("Pick a number: "))
        if color != 0:
            player = Dice(color)
            players.append(player)
        else:
            continue
    play_game()

def play_game():
    global players, placeholder, RGB
    placeholder = [0] * len(players)
    RGB = [0] * len(players)
    total_rounds = len(players) * 10000
    print()
    print("total rounds: " + str(total_rounds))
    print()
    for i in range(total_rounds):
        index = 0
        for i in players:
            player_rolls_dice(index, i, total_rounds)
            index += 1
        highest_value = placeholder.index(max(placeholder))
        RGB[highest_value] += 1
    print_winner()

def print_winner():
    global players, RGB
    print("Results: " + str(RGB))
    print()
    for i in range(len(players)):
        print(players[i].color + " is index: " + str(i))
    print()
    winner = players[RGB.index(max(RGB))].color + " " + str(max(RGB))
    print("The winner is: " + winner)

def player_rolls_dice(index, color, total_rounds):
    rnd = random.randint(0, 5)
    placeholder[index] = color.roll_dice(rnd)

def main():
    print("Ready to play some dice?")
    print("The rules are simple you pick one dice (Blue, Green, Red) and roll it 10 times")
    print("The one with the highest value are the winner")
    print("Number 0: No more players")
    print("Number 1: Red")
    print("Number 2: Green")
    print("Number 3: Blue")
    pick_color()

if __name__ == "__main__":
    main()