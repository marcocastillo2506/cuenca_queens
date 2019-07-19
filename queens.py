#This function will allow us to place a queen and check if spot is available
def place_queens(n, queens, row):
    pass

#This function will allow us to check if we will have any threats
def check_conflicts(queens, row):
    pass

#This function will allow us to create our board size
def nqueens(n):
    globals()["solutions"] = 0
    queens = [0] * n
    for i in range(n):
        queens[0] = i
        place_queens(n, queens, 1)
    return globals()["solutions"]
