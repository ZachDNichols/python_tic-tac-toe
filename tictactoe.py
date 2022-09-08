from os import system, name
from time import sleep
from turtle import pos, position      

def tie_check(positions):
    for i in range(3):
        for j in range(3):
            if positions[i][j] == ' ':
                return False
    return True


def pick_spot(player, positions):
    cpuCords = [-1, -1]

    #Checks for a horizontal line ---
    for i in range(3):
        if positions[i][0] == player and positions[i][1] == player:
            cpuCords = [i, 2]
            return cpuCords
        if positions[i][1] == player and positions[i][2] == player:
            cpuCords = [i, 0]
            return cpuCords
        if positions[i][0] == player and positions[i][2] == player:
            cpuCords = [i, 1]
            return cpuCords

    #Checks for vertical line
    for i in range(3):
        if positions[0][i] == player and positions[1][i] == player:
            cpuCords = [2, i]
            return cpuCords
        if positions[0][i] == player and positions[2][i] == player:
            cpuCords = [1, i]
            return cpuCords
        if positions[1][i] == player and positions[2][i] == player:
            cpuCords = [0, i]
            return cpuCords
    #Checks for diagonal line \
    if positions[0][0] == player and positions[1][1] == player == player:
        cpuCords = [2, 2]
        return cpuCords
    if positions[1][1] == player and positions[2][2] == player:
        cpuCords = [0, 0]
        return cpuCords
    if positions[0][0] == player and positions[2][2] == player:
        cpuCords = [1, 1]
        return cpuCords

    #Checks for diagonal line /
    if positions[2][0] == player and positions[1][1] == player:
        cpuCords = [0, 2]
        return cpuCords
    if positions[1][1] == player and positions[0][2] == player:
        cpuCords = [2, 0]
        return cpuCords
    if positions[2][0] == player and positions[0][2] == player:
        cpuCords = [1, 1]
        return cpuCords

    return cpuCords


def print_board(positions):
    print(" |     |     |     | ")
    print("_|__" + positions[0][0] + "__|__" + positions[0][1] + "__|__" + positions [0][2] + "__|_")
    print("_|__" + positions[1][0] + "__|__" + positions[1][1] + "__|__" + positions [1][2] + "__|_")
    print("_|__" + positions[2][0] + "__|__" + positions[2][1] + "__|__" + positions [2][2] + "__|_")
    print(" |     |     |     | ")

def check_range(upperRange, lowerRange, playerChoice):
    if playerChoice > upperRange or playerChoice < lowerRange:
        return False
    return True

def validateSelection(row, column, positions):
    if positions[row][column] == ' ':
        return True
    return False

def check_for_winner(positions, currentPlayer):
    if positions[0][0] == currentPlayer and positions[1][0] == currentPlayer and positions[2][0] == currentPlayer:
        return True
    if positions[0][1] == currentPlayer and positions[1][1] == currentPlayer and positions[2][1] == currentPlayer:
        return True
    if positions[0][2] == currentPlayer and positions[1][2] == currentPlayer and positions[2][2] == currentPlayer:
        return True
    if positions[0][0] == currentPlayer and positions[0][1] == currentPlayer and positions[0][2] == currentPlayer:
        return True
    if positions[1][0] == currentPlayer and positions[1][1] == currentPlayer and positions[1][2] == currentPlayer:
        return True
    if positions[2][0] == currentPlayer and positions[2][1] == currentPlayer and positions[2][2] == currentPlayer:
        return True
    if positions[0][0] == currentPlayer and positions[1][1] == currentPlayer and positions[2][2] == currentPlayer:
        return True
    if positions[2][0] == currentPlayer and positions[1][1] == currentPlayer and positions[0][2] == currentPlayer:
        return True
    
    return False
    

def clear_console():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def main():
    playerChoice = 0
    positions = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    row = 0
    column = 0
    cpuRow = 0
    cpuColumn = 0
    cpuCords = [-1, -1]
    player = ''
    cpu = ''
    isNumber = False
    pWinner = False
    cWinner = False
    validSelection = False

    #Gets info on if the player is an X or O
    while not isNumber:
        isNumber = True
        try:
            playerChoice = int(input("Do you wish to be an X or an O?\n\nX: 1\nO: 2\n\n"))
        except:
            print("You did not enter a number!")
            isNumber = False
        if isNumber:
            isNumber = check_range(2, 1, playerChoice)
    
    if playerChoice == 1:
        print("You are an X!")
        player = 'X'
        cpu = 'O'
    else:
        print("You are an O!")
        player = 'O'
        cpu = 'X'

    #Main game loop
    while not pWinner or not cWinner:
        print_board(positions)

        #Checks to make sure the selection is valid
        while not validSelection:
            isNumber = False

            #Gets info on the row the player wants
            while not isNumber:
                isNumber = True
                try:
                    playerChoice = int(input("Please select a row.\n"))
                except:
                    print("A number was not entered.")
                    isNumber = False
                if isNumber:
                    isNumber = check_range(3, 1, playerChoice)
            
            print("Row " + str(playerChoice) + " selected.\n1")
            row = playerChoice - 1
            isNumber = False
            
            #Gets info on the column the player wants
            while not isNumber:
                isNumber = True

                try:
                    playerChoice = int(input("Please select a column.\n"))
                except:
                    print("A number was not entered.")
                    isNumber = False

                if isNumber:
                    isNumber = check_range(3, 1, playerChoice)
            
            print("Column " + str(playerChoice) + "selected.\n")
            column = playerChoice - 1

            validSelection = validateSelection(row, column, positions)
            if not validSelection:
                print("Selection is already occupied.\n")
        
        #Assigns the coordinate position
        positions[row][column] = player

        clear_console()
        print_board(positions)
        print("This is your selection.\n")

        pWinner = check_for_winner(positions, player)
        if pWinner:
            break

        if tie_check(positions):
            break
        
        cpuCords = pick_spot(cpu, positions)
        cpuRow = cpuCords[0]
        cpuColumn = cpuCords[1]

        if cpuCords[0] == -1:
            cpuCords = pick_spot(player, positions)
            
        if not validateSelection(cpuRow, cpuColumn, positions):
            cpuCords = pick_spot(player, positions)
            cpuRow = cpuCords[0]
            cpuColumn = cpuCords[1]
        
        while not validateSelection(cpuRow, cpuColumn, positions):
            cpuRow += 1
            if cpuRow > 2:
                cpuRow = 0
            if validateSelection(cpuRow, cpuColumn, positions):
                break
            cpuColumn += 1
            if cpuColumn > 2:
                cpuColumn = 0
        
        sleep(1)
        positions[cpuRow][cpuColumn] = cpu
        clear_console()

        print_board(positions)
        print("This is the computer's selection.")
        sleep(1)



        cWinner = check_for_winner(positions, cpu)

        if cWinner:
            break

        if tie_check(positions):
            break

        clear_console()

        isNumber = False
        validSelection = False

    #Win condition
    if pWinner:
        print("Congratulations, you beat a computer.")
    elif cWinner:
        print("Shameful, you were beat by the computer.")
    else:
        print("You had an epic battle, but it ended in a tie. You are both equally matched.")

    isNumber = False
    while not isNumber:
        try:
            playerChoice = int(input("Would you like to play again?\n1: Yes\n2: No\n"))
        except:
            print("A number was not entered, please try again.")
            isNumber = False
        isNumber = check_range(2, 1, playerChoice)
    if playerChoice == 1:
        main()

main()