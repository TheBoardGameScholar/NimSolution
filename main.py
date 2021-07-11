# Main class for NimAI
# The Board Game Scholar
# Freddy Reiber

import random

initialHeaps = [3, 5, 7]


# Handles Player Turns
def playerTurn(heaps):
    # Handles picking the heap
    while True:
        heap = input("Select Heap")
        if heap == 'A':
            heap = 0
        if heap == 'B':
            heap = 1
        if heap == 'C':
            heap = 2
        if isinstance(heap, str) or heaps[heap] == 0:
            print("invalid heap (either zeroed, or out of bounds")
        else:
            break

    # Handles subtracting of heaps
    while True:
        sub = int(input("How much to subtract?"))
        if sub > heaps[heap]:
            print("Subtracted to much!")
        else:
            heaps[heap] -= sub
            break


def AITurn(heaps):
    # Calculate the nimber
    nimber = 0
    for i in range(len(heaps)):
        nimber ^= heaps[i]
    # Checks for which heap to reduce and reduces it so the nimber is 0
    for i in range(len(heaps)):
        if nimber ^ heaps[i] < heaps[i]:
            heaps[i] = nimber ^ heaps[i]
            return
    else:
        for i in range(len(heaps)):
            if heaps[i] != 0:
                heaps[i] -= 1
                return


def checkForWin(heaps):
    for i in range(len(heaps)):
        if heaps[i] != 0:
            return False
    return True


# Set up Game
while True:
    currentHeaps = initialHeaps.copy()
    while True:
        print("Player Turn\n-----------\nA B C")
        print(currentHeaps[0], currentHeaps[1], currentHeaps[2])
        playerTurn(currentHeaps)
        if checkForWin(currentHeaps):
            print(currentHeaps[0], currentHeaps[1], currentHeaps[2])
            print("You win!")
            break
        print("AI Turn\n-----------\nA B C")
        print(currentHeaps[0], currentHeaps[1], currentHeaps[2])
        AITurn(currentHeaps)
        if checkForWin(currentHeaps):
            print(currentHeaps[0], currentHeaps[1], currentHeaps[2])
            print("You lose!")
            break
    checkForPlay = input("Would you like to play again y/n?")
    if checkForPlay == 'n':
        break
