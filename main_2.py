import random


print("How many pencils would you like to use:")
while True:
    no_pencil = input()
    if not no_pencil.isdigit():
        print("The number of pencils should be numeric")
    elif no_pencil == "0":
        print("The number of pencils should be positive")
    else:
        break
print("Who will be the first (John, Jack)")
while True:
    starting_player = player = input()
    if player in ["John", "Jack"]:
        break
    print("Choose between John and Jack")
no_pencil = int(no_pencil)
while no_pencil > 0:
    print("|" * no_pencil)
    if starting_player == "John":
        if player == "John":
            player = "Jack"
            print("John's turn!")
            while True:
                pencil_taken = input()
                if pencil_taken not in ["1", "2", "3"]:
                    print("Possible values: '1', '2' or '3'")
                elif int(pencil_taken) > no_pencil:
                    print("Too many pencils were taken")
                else:
                    break
        elif player == "Jack":
            player = "John"
            print("Jack's turn:")
            if no_pencil % 4 == 2:
                pencil_taken = 1
            elif no_pencil % 4 == 3:
                pencil_taken = 2
            elif no_pencil % 4 == 0:
                pencil_taken = 3
            else:
                while True:
                    pencil_taken = random.randint(1, 3)
                    if pencil_taken <= no_pencil:
                        break
            print(pencil_taken)
        no_pencil -= int(pencil_taken)

    # Winning strategy is used for BOT aka Jack
    elif starting_player == "Jack":
        if player == "John":
            player = "Jack"
            print("John's turn!")
            while True:
                pencil_taken = input()
                if pencil_taken not in ["1", "2", "3"]:
                    print("Possible values: '1', '2' or '3'")
                elif int(pencil_taken) > no_pencil:
                    print("Too many pencils were taken")
                else:
                    break
        elif player == "Jack":
            player = "John"
            print("Jack's turn:")
            if no_pencil % 4 == 2:
                pencil_taken = 1
            elif no_pencil % 4 == 3:
                pencil_taken = 2
            elif no_pencil % 4 == 0:
                pencil_taken = 3
            else:
                while True:
                    pencil_taken = random.randint(1, 3)
                    if pencil_taken <= no_pencil:
                        break
            print(pencil_taken)
        no_pencil -= int(pencil_taken)
print(f"{player} won!")
