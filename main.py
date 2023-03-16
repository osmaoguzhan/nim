from functools import reduce
import random
import numpy as np


def createGameBoard(num, start=1, end=10):
    arr = []
    tmp = random.randint(start, end)
    for x in range(num):
        while tmp in arr:
            tmp = random.randint(start, end)
        arr.append(tmp)
    arr.sort()
    return arr


size = createGameBoard(5)
isPlayersTurn = input("Who will start (1 - Player, 2 - Computer): ") == "1"


def printBoard():
    for i in range(len(size)):
        print(i, end="|")
        for j in range(size[i]):
            print("+", end=" ")
        print()


def playerTurn():
    print("Your turn")
    hint()
    while True:
        index = int(input("Which index: "))
        if index < 0 or index >= len(size) or size[index] == 0:
            print("Invalid index")
        else:
            break
    while True:
        toRemove = int(input("How many: "))
        if toRemove <= 0 or toRemove > size[index]:
            print("Invalid number")
        else:
            break
    size[index] -= toRemove


def computerTurn(hint=False):
    index = -1
    toRemove = -1
    for i in range(len(size)):
        for j in range(1, size[i] + 1):
            temp = size.copy()
            if temp[i] - j < 0:
                break
            temp[i] -= j
            xor = reduce((lambda x, y: x ^ y), temp)
            if xor == 0:
                index = i
                toRemove = j
                break
        if index != -1:
            break
    if hint:
        return index, toRemove
    if index == -1 or toRemove == -1:
        res = np.array(size)
        arr = np.where(res != 0)[0]
        index = random.choice(arr)
        toRemove = random.randint(1, size[index])
    size[index] -= toRemove
    print("Computer removed", toRemove, "from", index)


def main():
    global isPlayersTurn
    while reduce(lambda x, y: x + y, size) > 0:
        print("Size: ", size)
        printBoard()
        if isPlayersTurn:
            playerTurn()
        else:
            computerTurn()
        isPlayersTurn = not isPlayersTurn
    if isPlayersTurn:
        print("You lose")
    else:
        print("You win")


def hint():
    index, toRemove = computerTurn(True)
    if index == -1 or toRemove == -1:
        print("No hint. Probably you will lose.")
    else:
        print("Remove ", toRemove, "from", index)


if __name__ == '__main__':
    main()
