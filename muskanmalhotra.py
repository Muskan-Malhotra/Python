import copy
import random

board = [
    ".........",
    ".........",
    ".........",
    ".........",
    ".........",
    ".........",
    ".........",
    ".........",
    "........."
]

def main():
    global board
    for idx,line in enumerate(board):
        board[idx] = list(line)
        
    solve()
    printBoard()
    
    

       
def solve():
    global board
    
    try:
        fillAllObvious()
        
    except:
        return False
    
    if isComplete():
        print(" ")
        return True
        
    
    i,j = 0,0
    for rowIdx,row in enumerate(board):
        for colIdx,col in enumerate(row):
            if col == ".":
                i,j = rowIdx, colIdx
                
    possibilities = getPossibilities(i,j)
    for value in possibilities:
        snapshot = copy.deepcopy(board)
    
        board[i][j] = value
        result = solve()
        if result == True:
            
            return True
        else:
            
            board = copy.deepcopy(snapshot)
            
    return False

def fillAllObvious():
    global board
    while True:
        somethingChanged = False
        for i in range(0,9):
            for j in range(0,9):
                possibilities = getPossibilities(i,j)
                if possibilities == False:
                    continue
                if len(possibilities) == 0:
                    raise RuntimeError("No moves left")
                if len(possibilities) == 1:
                    board[i][j] = possibilities[0]
                    somethingChanged = True
                    
                    
        if somethingChanged == False:
            return

        
                
def getPossibilities(i,j):
    global board
    if board[i][j] != ".":
    
        return False
        
    possibilities = {str(n) for n in range(1,10)}
    
    for val in board[i]:
        possibilities -= set(val)
        
    for idx in range(0,9):
        possibilities -= set( board[idx][j] )
        
    iStart = (i // 3) * 3
    jStart = (j // 3) * 3
    
    subboard = board[iStart:iStart+3]
    for idx,row in enumerate(subboard):
        subboard[idx] = row[jStart:jStart+3]
    
    for row in subboard:
        for col in row:
            possibilities -= set(col)
            
    return list(possibilities)

def printBoard():
    global board
    for row in board:
        for col in row:
            
            print(format(col,"<2"),end="")

        print("")
    print(" ")
    print("This is a valid Sudoku Grid")
        
        
        
def isComplete():
    for row in board:
        for col in row:
            if (col == "."):
                
                return False
           
    return True

main()


    
    
a = [
     "6 . . 8 7 4 . 1 .",
     ". . 9 . 3 6 . . .",
     ". . . 1 9 . 8 . .",
     "7 9 4 6 . . . . .",
     ". . 1 . 8 9 4 . .",
     ". . . 4 1 . . 6 9",
     ". 7 . . 5 . . 9 .",
     ". 5 3 9 . 7 6 . .",
     "9 . 2 . 6 1 . 4 7"
]

b = ["3 . . . . 4 . 1 .",
     ". . 9 . 3 6 . . .",
     ". . . 1 9 . 8 . .",
     ". . 4 6 . . . . .",
     ". . 1 . 8 . 4 . .",
     ". . . 4 1 . . 6 9",
     ". 7. . 5 . . 9 . ",
     ". 5 . 9 . 7 6 . .",
     "9 . . . . 1 . 4 7"
]

c = [
      ". . . . 7 . . 1 .",
     ". . 9 . . 6 . . .",
     ". . . 1 9 . 8 . .",
     "7 . 4 . . . . . .",
     ". . 1 . . 9 . . .",
     ". . . . 1 . . . 9",
     ". 7 . . 5 . . 9 .",
     ". 5 . . . 7 . . .",
     "9 . 2 . 6 . . . ."
     
]
d = [
     ". . . . . . . . .",
     "5 . 3 . . 7 . . .",
     "9 . . 3 . 2 . . .",
     ". . . . . 4 . . .",
     ". . 1 . . . 7 2 .",
     ". . 2 . 1 . . . .",
     ". 3 . . . . . . 9",
     ". . . 1 . . 2 . .",
     ". . . 7 . . 8 . 6"
    
]
e = [
     ". . . . . . . . .",
     ". 2 . 7 . . . . .",
     ". . . . . . . . .",
     ". . 5 . . . 8 . .",
     ". . . . . . . . .",
     ". . 8 . . 4 . . .",
     ". 9 . . . . . 6 .",
     ". . . . 3 . . . .",
     "1 . . 5 . . . . ."
]

k=[]

my_list=['a','b','c','d','e']
my_list.index('a',0)
my_list.index('b',1)
print(" ")
m = int(input("Choose the level of difficulty from 1 to 5: "))

if m == 1:
    my_list[0]= print(*a, sep = "\n") 
    k = a
elif m == 2:
    my_list[1]= print(*b, sep = "\n") 
    k = b
elif m == 3:
    my_list[2]= print(*c, sep = "\n") 
    k = c
elif m == 4:
    my_list[3]= print(*d, sep = "\n")
    k =d
elif m == 5:
    my_list[4]= print(*e, sep = "\n")
    k = e





def main1():
    global k
    for idx,line in enumerate(k):
        k[idx] = list(line)

    
    
    solve1()
    printBoard1()


def solve1():
    global k

    try:
        fillAllObvious1()

    except:
        return False

    if isComplete1():
        print(" ")
        return True


    i,j = 0,0
    for rowIdx,row in enumerate(k):
        for colIdx,col in enumerate(row):
            if col == ".":
                i,j = rowIdx, colIdx

    possibilities = getPossibilities1(i,j)
    for value in possibilities:
        snapshot = copy.deepcopy(k)

        k[i][j] = value
        result = solve1()
        if result == True:

            return True
        else:

            k = copy.deepcopy(snapshot)

    return False

def fillAllObvious1():
    global k
    while True:
        somethingChanged = False
        for i in range(0,9):
            for j in range(0,9):
                possibilities = getPossibilities1(i,j)
                if possibilities == False:
                    continue
                if len(possibilities) == 0:
                    raise RuntimeError("No moves left")
                if len(possibilities) == 1:
                    k[i][j] = possibilities[0]
                    somethingChanged = True


        if somethingChanged == False:
            return



def getPossibilities1(i,j):
    global k
    if k[i][j] != ".":

        return False

    possibilities = {str(n) for n in range(1,10)}

    for val in k[i]:
        possibilities -= set(val)

    for idx in range(0,9):
        possibilities -= set( k[idx][j] )

    iStart = (i // 3) * 3
    jStart = (j // 3) * 3

    subboard = k[iStart:iStart+3]
    for idx,row in enumerate(subboard):
        subboard[idx] = row[jStart:jStart+3]

    for row in subboard:
        for col in row:
            possibilities -= set(col)

    return list(possibilities)

def printBoard1():
    global k
    for row in k:
        for col in row:

            print(format(col,"<1"),end="")

        print("")
    print(" ")
    print("This is a valid Sudoku Grid")



def isComplete1():
    for row in k:
        for col in row:
            if (col == "."):

                return False

    return True



import time
start_time = time.time()



print("")
main1()
print("")



print("--- %s seconds ---" % (time.time() - start_time)) 
print(" ")



   





    