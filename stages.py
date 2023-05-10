# Stage 4/5: Fair play
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
    player = input()
    if player in ["John", "Jack"]:
        break
    print("Choose between John and Jack")
no_pencil = int(no_pencil)
while no_pencil > 0:
    print("|" * no_pencil)
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
        while True:
            pencil_taken = input()
            if pencil_taken not in ["1", "2", "3"]:
                print("Possible values: '1', '2' or '3'")
            elif int(pencil_taken) > no_pencil:
                print("Too many pencils were taken")
            else:
                break
    no_pencil -= int(pencil_taken)

print(f"{player} won!")
