def display_grid(L1):  # L1 is the parameter for grid
    print("\n\tC1\t\tC2\t\tC3")
    print("-------------------------")
    for i in range(3):
        print("|", end="\t")
        for j in range(3):
            print(L1[i][j], end="\t|\t")
        print("", end="R{}\n".format(i + 1))
        print("-------------------------")
    print("\n")
    return L1


def check(L2):  # L2 is the parameter for grid
    result = " "
    for i in range(3):
        if L2[i][0] == L2[i][1] == L2[i][2]:
            result = L2[i][1]
    for j in range(3):
        if L2[0][j] == L2[1][j] == L2[2][j]:
            result = L2[0][j]
    if L2[0][0] == L2[1][1] == L2[2][2] or L2[2][0] == L2[1][1] == L2[0][2]:
        result = L2[1][1]

    if result == p1[0]:
        display_grid(L2)
        print(p1, "wins the game!!!")
        exit(0)
    if result == p2[0]:
        display_grid(L2)
        print(p2, "wins the game!!!")
        exit(0)


print("Welcome to Tic Tac Toe \n")

grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
p1 = input("Enter Player 1 name: ")
p2 = input("Enter Player 2 name: ")
c = 0

while True:
    c1 = 0

    display_grid(grid)

    while c1 == 0:
        print(p1 + "\'s Turn")
        row = int(input("Enter row number (1-3): ")) - 1
        col = int(input("Enter column number (1-3): ")) - 1
        if row <= 0 or col <= 0:
            print("Please enter an integer from 1-3")
            continue

        try:
            if grid[row][col] == " ":
                grid[row][col] = p1[0]
                c1 = 1
            else:
                print("Square occupied")
        except IndexError:
            print("Index error!!! Input row/column is out of bounds")
        except TypeError:
            print("Type Error!!! Please enter an integer type input")

    c1 = 0
    c += 1

    if c >= 5:
        check(grid)

    if c >= 9:
        print("\nGame Draw")
        break

    display_grid(grid)

    while c1 == 0:
        print(p2 + "\'s Turn")
        row = int(input("Enter row number (1-3): ")) - 1
        col = int(input("Enter column number (1-3): ")) - 1
        try:  # Exception Handling for index error
            if grid[row][col] == " ":
                grid[row][col] = p2[0]
                c1 = 1
            else:
                print("Square occupied")
        except IndexError:
            print("Index error!!! Input row/column is out of bounds")

    c1 = 0
    c += 1
    if c >= 5:
        check(grid)
