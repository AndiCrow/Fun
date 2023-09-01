# This is a game, where you need to find the exit
#Rules: 
#1. you will writt what you be asked 
#2. if you go back, then you go to your orignal postion




name = input("Whats your name? ")
#Startpoint
print( name, "your are lost in the forest. \nBehind you is a wall.")
print("1. to the right side \n2. to the left side \n3. forward ")
choise = int(input("Where woud you like to go?: "))
#Right side of the forest 1
if choise == 1:
    print("Your are still in the Forest and there is only 1 way ")
    print("1.go the only way  \n2. go back : ")
    forest_right_side = int(input("Where woud you like to go?: "))
    #You are on the 2 feld on the right

    if forest_right_side == 1:
         print("Your are still in the forest \nNow you have 2 ways")
         print("1. go forwand \n2. to to the right side \n3. go back")
         forest_right_side2 = int(input("Where woud you like to go?: "))
         #You are at a deadend, you go beck
         if forest_right_side2 == 1:
               print("You are still in the forest and there is a dead end you go back where you came")