import random
import time

Dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

def Set():
    print("==========================")
    print("WELCOME TO ROLL DICE GAME")
    print("==========================")
    print("")
    while True:
        p1 = input("Enter your name. Player 1: ")
        print("")
        if p1:
            break
        else:
            print("Invalid username.\n")
    while True:
        p2 = input("Enter your name. Player 2: ")
        print("")
        if p2:
            break
        else:
            print("Invalid username.\n")
    while True:
        round = input("Enter the no. of round: ")
        print("")
        try: 
            rounds = int(round)
        except ValueError:
            print("Invalid input.\n")
            continue
        if rounds > 0:
            break
        else:
            print("The minimum round is 1.\n")
            continue
    print("...\n")
    time.sleep(2)
    print("==========================")
    print(f"P1: {p1}       P2: {p2}")
    print("==========================")
    print("")
    print("Game start in...\n")
    for i in range(5,0,-1):
        time.sleep(1)
        print(f"{i}\n")
    print("==========================")
    return p1, p2, rounds

def Roll():
    p1_dice, p2_dice = [],[]
    total_p1 = 0
    total_p2 = 0
    for x in range (4):
        roll = random.randint(1,6)
        if len(p1_dice) == 2:
            p2_dice.append(roll)
        else:
            p1_dice.append(roll)

    print("PLAYER 1: ")

    for lines in range(5):
        for dice in p1_dice:
            print(Dice_art.get(dice)[lines], end = "")
        print("")
    total_p1 = sum(p1_dice)
    print(f"Total: {total_p1}\n")
    print("==========================")

    time.sleep(2)
    print("PLAYER 2: ")

    for lines in range(5):
        for dice in p2_dice:
            print(Dice_art.get(dice)[lines], end = "")
        print("")
    total_p2 = sum(p2_dice)
    print(f"Total: {total_p2}\n")
    print("==========================")

    return total_p1, total_p2

def Dashboard(name_1, name_2, score_p1, score_p2):
    print("==========================\n")
    print(f"P1: {name_1}     P2: {name_2}\n")
    print(f"Score: {score_p1}     Score: {score_p2}\n")
    print("==========================")

def Main():
    name_1, name_2, num_round = Set()
    score_p1 = score_p2 = 0
    for i in range(num_round):
        print(f"ROUND {i+1}:\n")
        time.sleep(1)
        a, b = Roll()
        if a > b:
            score_p1 += 1
            print("Winner is Player 1 !!!\n")
        elif b > a:
            score_p2 += 1
            print("Winner is Player 2 !!!\n")
        else:
            print("Draw !!!\n")
    
        print("Scoreboard: ")
        time.sleep(2)
        Dashboard(name_1, name_2, score_p1, score_p2)
        time.sleep(5)

    print("\nFINAL RESULT:\n")
    if score_p1 > score_p2:
        print(f"🜲🜲🜲🜲🜲🜲 {name_1} WIN!!! 🜲🜲🜲🜲🜲🜲")
    elif score_p2 > score_p1:
        print(f"🜲🜲🜲🜲🜲🜲 {name_2} WIN!!! 🜲🜲🜲🜲🜲🜲")
    else:
        print("DRAW !!!")

Main()