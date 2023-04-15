# Stage 3/5: Working on the gameplay
no_pencil = int(input("How many pencils would you like to use:\n"))
player = input("Who will be the first (John, Jack):\n")
while no_pencil > 0:
    print("|" * no_pencil)
    pencils = int(input(f"{player}'s turn:\n"))
    no_pencil -= pencils
    if player == "John":
        player = "Jack"
    else:
        player = "John"
