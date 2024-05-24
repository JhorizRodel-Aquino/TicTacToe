grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
switcher = 1  # this will determine which to play, whether X or O
play = "X"  # placeholder for X or O -- initial is X
breaker = False

while breaker is False:
    print("---------")
    for column in grid:
        row = " ".join(column)
        print(f"| {row} |")
    print("---------")

    combined_grid = [b for a in grid for b in a]
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8]]
    for line in wins:
        for v in line:
            if not (combined_grid[v] == play):
                break
            if line[2] == v:
                print(play + " wins")
                breaker = True

    if breaker is True:
        continue

    if switcher % 2 == 1:
        play = "X"
    else:
        play = "O"

    try:
        y, x = input("Enter the coordinates: ").split()
        y = int(y) - 1
        x = int(x) - 1

    except:
        if type(y) == str:
            print("You should enter numbers!")
        else:
            print("You should enter 2 coordinates!")

    else:
        if y > 2 or x > 2:
            print("Coordinates should be from 1 to 3!")
        else:
            if grid[y][x] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                grid[y][x] = play

                switcher += 1
