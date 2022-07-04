import random


no_pencil = input("How many pencils would you like to use:\n")
while True:
    if no_pencil.isdigit():
        no_pencil = int(no_pencil)
        if no_pencil > 0:
            while True:
                next_turn = input("Who will be the first (John, Jack):\n")
                if next_turn in ["John", "Jack"]:
                    while int(no_pencil) > 0:
                        print("|" * int(no_pencil))
                        if next_turn == "John":
                            print("John's turn!")
                            next_turn = "Jack"
                            while True:
                                x = input()
                                if x in ["1", "2", "3"]:
                                    if int(x) <= no_pencil:
                                        break
                                    print("Too many pencils were taken")
                                else:
                                    print("Possible values: '1', '2' or '3'")
                            no_pencil -= int(x)
                        else:
                            print("Jack's turn!")
                            next_turn = "John"
                            if no_pencil == 1:
                                x = 1
                            elif no_pencil % 4 == 0:
                                x = 3
                            elif no_pencil % 4 == 3:
                                x = 2
                            elif no_pencil % 4 == 2:
                                x = 1
                            else:
                                x = random.choice([1, 2, 3])
                            no_pencil -= int(x)
                    print("John won!" if next_turn == "John" else "Jack won!")
                    break
                print("Choose between 'John' and 'Jack'")
            break
        print("The number of pencils should be positive")
        no_pencil = input()
        continue
    print("The number of pencils should be numeric")
    no_pencil = input()
    continue
