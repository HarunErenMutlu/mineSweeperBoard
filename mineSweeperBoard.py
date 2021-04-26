import random
def createField():
    length = random.randint(5, 15)
    field = []
    for i in range(length):
        field.append([])
        for j in range(length):
            field[i].append("-")
            option = random.randint(1,10)
            if option == 1:
                field[i-1][j-1] = "#"
    return field

def checkMineInRow(field,currentRow,CurrentColumn,checkRow,checkColoumn):
    lastRow = currentRow+2
    initialRow = currentRow-1
    initialColoumn= CurrentColumn-1
    lastColoumn= CurrentColumn+1
    if checkRow =="first":
        initialRow +=1
    elif checkRow == "last":
        lastRow -=1
    if checkColoumn== "first":
        initialColoumn+=1
    elif checkColoumn == "last":
        lastColoumn -= 1
    count = 0
    for i in range(initialRow,lastRow):
        for j in range(initialColoumn,lastColoumn+1):
            if field[i][j] == "#":
                count +=1
    return str(count)

def showField():
    field = createField()
    for i in range(len(field)):
        for j in range(len(field)):
            current = field[i][j]
            if i == 0 or i == len(field)-1:
                if current != "#":
                    if i == 0:
                        if j not in [0,len(field)-1]:
                            field[i][j] = checkMineInRow(field,i,j,"first","")
                        elif j == 0:
                            field[i][j] = checkMineInRow(field,i,j,"first","first")
                        elif j == len(field)-1:
                            field[i][j] = checkMineInRow(field,i,j,"first","last")
                        
                    elif i == len(field)-1:
                        if j not in [0,len(field)-1]:
                            field[i][j] = checkMineInRow(field,i,j,"last","")
                        elif j == 0:
                            field[i][j] = checkMineInRow(field,i,j,"last","first")
                        elif j == len(field)-1:
                            field[i][j] = checkMineInRow(field,i,j,"last","last")
                        
                pass
            else:
                if current != "#":
                    if j not in [0,len(field)-1]:
                        field[i][j] = checkMineInRow(field,i,j,"","")
                    elif j == 0:
                        field[i][j] = checkMineInRow(field,i,j,"","first")
                    elif j == len(field)-1:
                        field[i][j] = checkMineInRow(field,i,j,"","last")
    return field
field = showField()
liste = []
for line in field:
    liste.append(" ".join(line))
for i in liste:
    print(i)