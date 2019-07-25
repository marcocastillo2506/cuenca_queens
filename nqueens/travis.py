def place_queens(n, queens, row):
    for i in range(n):
        queens[row] = i
        if check_conflicts(queens, row):
            if row == n - 1:
                squeens.extend(queens)
                print(queens)
                globals()["solutions"] += 1
            else:
                place_queens(n, queens, row + 1)

def check_conflicts(queens, row):
    current = queens[row]
    for i in range(row):
        if queens[i] == current:
            return False
    for index, queen in enumerate(queens[:row]):
        distance = row - index
        if abs(queen - current) == distance:
            return False
    return True

def nqueens(n):
    globals()["squeens"] = []
    globals()["size"] = n
    globals()["solutions"] = 0
    globals()["queens"] = [0] * n
    for i in range(n):
        queens[0] = i
        place_queens(n, queens, 1)
    return globals()["solutions"]
