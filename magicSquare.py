square = []
rawnums = []
length = int(input("What side length should the square be? "))
rowsEqual = False
colsEqual = False
diagsEqual = False

def make2DArray(size):
    for y in range(size):        
        square.append([])
        for x in range(size):
            square[y].append(rawnums.pop(0))

def rowSum(rowNum):
    sum = 0
    for i in range(length):
        sum+= square[rowNum][i]
    return sum

def colSum(colNum):
    sum = 0
    for i in range(length):
        sum+= square[i][colNum]
    return sum

def checkCols():
    colsEqual = True
    firstSum = colSum(0)
    for y in range(1,length):
        if(colSum(y) != firstSum):
            colsEqual = False
    if(colsEqual == True):
        return True
    else:
        return False

def checkRows():
    rowsEqual= True
    firstSum = rowSum(0)
    for row in range(1,length):
        if(rowSum(row) != firstSum):
            rowsEqual = False
    if(rowsEqual == True):
        return True
    else:
        return False

def getTopLeftDiagSum():
    sum = 0
    for i in range(length):
        sum+=square[i][i]
    return sum
    
def getTopRightDiagSum():
    sum = 0
    row = 0
    for i in range(length-1,-1,-1):
        sum+=square[row][i]
        row+=1
    return sum

def checkDiags():
    if(getTopLeftDiagSum() == getTopRightDiagSum()):
        return True
    else:
        return False

for x in range(length*length):
    rawnums.append(int(input("Enter a number. ")))

make2DArray(length)
if(checkRows() and checkCols() and checkDiags()):
    if(rowSum(0) == colSum(0) and rowSum(0) == getTopLeftDiagSum()):
        print("It's a magic square!")
    else:
        print("It's not a magic square.")
else:
    print("It's not a magic square.")