
def check_game_over(count): #checking for game over here
    if count <=0:
        print("Because you are running in circles animels have spotted you and now you are dead \n Game Over ")
        return True
    else:
        return False
    


def start_game():
    print( name, "your are lost in the forest. \nBehind you is a wall.")
    choise_true = False
    while not choise_true:
        print("1. to the right side \n2. to the left side \n3. forward ")
        choise = int(input("Where woud you like to go?: "))
        if choise == 1:
            feld_1_at_right()
        elif choise == 2:
            feld_1_at_left()
        elif choise == 3:
            feld_1_at_left() # is Reversed dircetion but the same text and choises
        else:
            print("Invalid choice. Please select a valid option.")




def startpoint():
    global count
    print( name, "your are stiil lost in the forest. \nBehind you is a wall. Know you are rembered that this was your startpoint")
    count -= 1
    if check_game_over(count):
        exit
    choise_true = False
    while not choise_true:
        print("1. to the right side \n2. to the left side \n3. forward ")
        choise = int(input("Where woud you like to go?: "))
        if choise == 1:
            feld_1_at_right()
        elif choise == 2:
            feld_1_at_left()
        elif choise == 3:
            feld_1_at_left() # is Reversed dircetion but the same text and choises
        else:
            print("Invalid choice. Please select a valid option.")

def feld_1_at_right():
    global count
    print("Your are still in the Forest and there is only 1 way ")
    count = count - 1
    if check_game_over(count):
        exit()
    choise_true = False
    while not choise_true:
        print("1.go the only way  \n2. go back : ")
        forest_right_side = int(input("Where woud you like to go?: "))
        if forest_right_side == 1:
            feld_2_at_right()
        elif forest_right_side == 2:
            startpoint()
        else:
            print("Invalid choice. Please select a valid option.")


def feld_2_at_right():
    global count
    print("Your are still in the forest \nNow you have 2 ways")
    count -= 1
    if check_game_over(count):
        exit()
    choise_true = False
    while not choise_true:
        print("1. go forwand \n2. to to the right side \n3. go back")
        forest_right_side2 = int(input("Where woud you like to go?: "))
        if forest_right_side2 == 1:
            print("You are still in the forest and there is a dead end you go back where you came")
            feld_1_at_right()
        elif forest_right_side2 == 2:
            feld_3_at_right()
        else:
            print("Invalid choice. Please select a valid option.")


def feld_3_at_right():
    global count
    print("You are still in the forest and you have 2 ways")
    count -= 1
    if check_game_over(count):
        exit()
    choise_true = False
    while not choise_true:
        print("1. go to the right side \n2. go the left side \n3. go back")
        forest_right_side_3 = int(input("Where woud you like to go?: "))
        if forest_right_side_3 == 1:
            print("you are out of the forest:\nYOU WON {name}")
        elif forest_right_side_3 == 2:
            print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
        elif forest_right_side_3 == 3:
            feld_2_at_right()
        else:
            print("Invalid choice. Please select a valid option.")



def feld_1_at_left():
    global count
    print("You are still in the forest. \n You have only 1 way")
    count -= 1
    if check_game_over(count):
        exit()
    choise_true = False
    while not choise_true:
        print("1. go the way \n2. go back: ")
        forest_left_side = int(input("Where woud you like to go?: "))
        if forest_left_side == 2:
            startpoint()
        elif forest_left_side == 1:
            feld_2_at_left()
        else:
            print("Invalid choice. Please select a valid option.")



def feld_2_at_left():
    global count
    print("You are still in the forest. \n You have only 1 way")
    count -= 1
    if check_game_over(count):
        exit()
    choise_true = False
    while not choise_true:
        print("1. go the way \n2. go back: ")
        forest_left_side_2 = int(input("Where woud you like to go?: "))
        if forest_left_side_2 == 2:
            feld_1_at_left()
        elif forest_left_side_2 == 1:
            feld_3_at_right()
        else:
            print("Invalid choice. Please select a valid option.")

def feld_3_at_right():
    global count
    print("You are still in the forest. \n You have only 1 way")
    count -= 1
    if check_game_over(count):
        exit()
    choise_true = False
    while not choise_true:
        print("1. go forwand \n2. go back: ")
        feld_3_at_left= int(input("Where woud you like to go?: "))
        if feld_3_at_left == 2:
            feld_2_at_left()
        elif feld_3_at_left == 1:
            startpoint()
        else:
            print("Invalid choice. Please select a valid option.")


count = 0
name = input("Whats your name? ")
choise_true = False
while not choise_true:
    print("Wich mode do you want\n1.easy\n2.normal\n3.hard\n4.hell")
    mode = int(input("Wich mode ?: "))
    if mode == 1:
        count += 99
        start_game()
    elif mode == 2:
        count += 50
        start_game()
    elif mode == 3:
        count += 35
        start_game()
    elif mode == 4:
        count += 15
        start_game()
    else:
        print("Invalid choice. Please select a valid option.")



