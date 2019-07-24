#This function will allow us to place a queen and check if spot is available
def place_queens(n, queens, row):
    for i in range(n):
        queens[row] = i
        if check_conflicts(queens, row):
            if row == n - 1:
                squeens.extend(queens)
                globals()["solutions"] += 1
            else:
                place_queens(n, queens, row + 1)

#This function will allow us to check if we will have any threats
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

#This function will allow us to create our board size
def nqueens(n):
    globals()["squeens"] = []
    globals()["size"] = n
    globals()["solutions"] = 0
    globals()["queens"] = [0] * n
    for i in range(n):
        queens[0] = i
        place_queens(n, queens, 1)
    return globals()["solutions"]

nqueens(8)

#This funcion will allow us to split our main array to determain each solution individually
def split(arr, size):
     globals()["solucion_individual"] = []
     while len(arr) > size:
         pice = arr[:size]
         solucion_individual.append(pice)
         arr   = arr[size:]
     solucion_individual.append(arr)
     return solucion_individual

split(squeens, size)
print(size)
