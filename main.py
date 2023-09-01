
name = input("Whats your name? ")

print( name, "your are lost in the forest. \n Behind you is a wall.")
print("1. to the right side \n2. to the left side \n3. forward ")
choise = int(input("Where woud you like to go?: "))
if choise == 1:  #startpoint
    print("Your are still in the Forest and there is only 1 way ")
    forest_right_side = int(print("1.go the only way  \n2. go back : "))
    if forest_right_side == 1:
        print("Your are still in the forest \n Now you have 2 ways")
        forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
        if forest_right_side_2 == 1:
            print("You are still in the forest and there is a dead end you go back where you came")
            print("Your are still in the forest \n Now you have 2 ways")
            forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
            if forest_right_side_2 == 1:
                print("You are still in the forest and there is a dead end you go back where you came")
                print("Your are still in the forest \n Now you have 2 ways")
                forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
                if forest_right_side_2 == 1:
                    print("Because you are running in circles animels have spotted you and now you are dead \n Game Over ")
                    #break
                elif forest_right_side_2 == 2:
                    print("You are still in the forest and you have 2 ways")
                    forest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
                    if forest_right_side_3 == 1:
                        print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                        #break
                    elif forest_right_side_3 == 2:
                        print("You left the forest \n You Won this Game")
                        #break
                    elif forest_right_side_3 == 3:
                        print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                        #break finish here
                elif forest_right_side_2 == 3:
                    print("You are still in the forest and you have 1 ways")
                    forest_right_side = int(input("1. go to the right side \n2. go back: "))
                    if forest_right_side == 1:
                        print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                   # break
                elif forest_right_side == 2:
                    print("You left the forest \n You Won this Game")
                   # break
                elif forest_right_side == 3:
                    print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                   # break
        elif forest_right_side_2 == 2:
            print("You are still in the forest and you have 2 ways")
            forest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
            if forest_right_side_3 == 1:
                print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
               # break
            elif forest_right_side_3 == 2:
                print("You left the forest \n You Won this Game")
               # break
            elif forest_right_side_3 == 3:
                print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
               # break
        elif forest_right_side_2 == 3:
            print("Your are still in the Forest and there is only 1 way ")
            forest_right_side = int(print("1. go back \n2 go the only way: "))
            if forest_right_side == 1:
                print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
               # break
            elif forest_right_side == 2:
                print("You are back where you started. \n You give up \n Game Over")
               # break
    elif forest_right_side == 2:
        print("You are back where you started.")
        print("1. to the right side \n2. to the left side \n3. forward ")
        choise = int(input("Where woud you like to go?: "))
        if choise == 1:
            print("Your are still in the Forest and there is only 1 way ")
            forest_right_side = int(print("1.go the only way  \n2. go back : "))
            if forest_right_side == 1:
                print("Your are still in the forest \n Now you have 2 ways")
                forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
                if forest_right_side_2 == 1:
                    print("You are still in the forest and there is a dead end you go back where you came")
                    print("Your are still in the forest \n Now you have 2 ways")
                    forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
                    if forest_right_side_2 == 1:
                        print("You are still in the forest and there is a dead end you go back where you came")
                        print("Your are still in the forest \n Now you have 2 ways")
                        forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
                        if forest_right_side_2 == 1:
                            print("Because you are running in circles animels have spotted you and now you are dead \n Game Over ")
                           # break
                        elif forest_right_side_2 == 2:
                            print("You are still in the forest and you have 2 ways")
                            forest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
                            if forest_right_side_3 == 1:
                                print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                               # break
                            elif forest_right_side_3 == 2:
                                print("You left the forest \n You Won this Game")
                               # break
                            elif forest_right_side_3 == 3:
                                print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                               # break
                        elif forest_right_side_2 == 2:
                            print("You are still in the forest and you have 2 ways")
                            forest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
                            if forest_right_side_3 == 1:
                                print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                                #break
                            elif forest_right_side_3 == 2:
                                print("You left the forest \n You Won this Game")
                               # break
                            elif forest_right_side_3 == 3:
                                print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                               # break
                            elif forest_right_side_2 == 2:
                                print("You are still in the forest and you have 2 ways")
                                forest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
                                if forest_right_side_3 == 1:
                                    print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                                   #break
                                elif forest_right_side_3 == 2:
                                    print("You left the forest \n You Won this Game")
                                   # break
                                elif forest_right_side_3 == 3:
                                    print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                                   # break
                            elif forest_right_side_2 == 3:
                                print("Your are still in the Forest and there is only 1 way ")
                                forest_right_side = int(print("1. go the only way  \n2 go back: "))
                                if forest_right_side == 1:
                                    print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                                   # break
                                elif forest_right_side == 2:
                                    print("You are back where you started. \n You give up \n Game Over")
                                    #break
elif choise == 2: #startpoint
    print("You are still in the forest. \n You have only 1 way")
    forest_left_side = int(input("1. go the way \n2. go back: "))
    if forest_left_side == 1:
        print("You are still in the forest. \n You have only 1 way")
        forest_left_side_2 = int(input("1. go the way \n2. go back: "))
        if forest_left_side_2 == 1:
            print("You are still in the forest. \n You have only 1 way")
            forest_left_side_3 = int(input("1. go forwand \n2. go back: "))
            if forest_left_side_3 == 1:
                print("You are back where you started")
                print("1. to the right side \n2. to the left side \n3. forward ")
choise = int(input("Where woud you like to go?: "))
if choise == 1:
    print("Your are still in the Forest and there is only 1 way ")
    forest_right_side = int(print("1.go the only way  \n2. go back : "))
    if forest_right_side == 1:
        print("Your are still in the forest \n Now you have 2 ways")
        forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
        if forest_right_side_2 == 1:
            print("You are still in the forest and there is a dead end you go back where you came")
            print("Your are still in the forest \n Now you have 2 ways")
            forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
            if forest_right_side_2 == 1:
                print("You are still in the forest and there is a dead end you go back where you came")
                print("Your are still in the forest \n Now you have 2 ways")
                forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
                if forest_right_side_2 == 1:
                    print("Because you are running in circles animels have spotted you and now you are dead \n Game Over ")
                   # break
                elif forest_right_side_2 == 2:
                    print("You are still in the forest and you have 2 ways")
                    forest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
                    if forest_right_side_3 == 1:
                        print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                       # break
                    elif forest_right_side_3 == 2:
                        print("You left the forest \n You Won this Game")
                       # break
                    elif forest_right_side_3 == 3:
                        print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                        #break
            if forest_right_side_2 == 2:
                print("You are still in the forest and you have 2 ways")
                orest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
                if forest_right_side_3 == 1:
                    print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                   # break
            elif forest_right_side_3 == 2:
                print("You left the forest \n You Won this Game")
               # break
            elif forest_right_side_3 == 3:
                print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
               # break
        elif forest_right_side_2 == 2:
            print("You are still in the forest and you have 2 ways")
            forest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
            if forest_right_side_3 == 1:
                print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
               # break
            elif forest_right_side_3 == 2:
                print("You left the forest \n You Won this Game")
               # break
            elif forest_right_side_3 == 3:
                print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
               # break
        elif forest_right_side_2 == 3:
            print("Your are still in the Forest and there is only 1 way ")
            forest_right_side = int(print("1. go back \n2 go the only way: "))
            if forest_right_side == 1:
                print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                #break
            elif forest_right_side == 2:
                print("You are back where you started. \n You give up \n Game Over")
                #break
    elif forest_right_side == 2:
        print("You are back where you started.")
        print("1. to the right side \n2. to the left side \n3. forward ")
        choise = int(input("Where woud you like to go?: "))
        if choise == 1:
            print("Your are still in the Forest and there is only 1 way ")
            forest_right_side = int(print("1.go the only way  \n2. go back : "))
            if forest_right_side == 1:
                print("Your are still in the forest \n Now you have 2 ways")
                forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
                if forest_right_side_2 == 1:
                    print("You are still in the forest and there is a dead end you go back where you came")
                    print("Your are still in the forest \n Now you have 2 ways")
                    forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
                    if forest_right_side_2 == 1:
                        print("You are still in the forest and there is a dead end you go back where you came")
                        print("Your are still in the forest \n Now you have 2 ways")
                        forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
                        if forest_right_side_2 == 1:
                            print("Because you are running in circles animels have spotted you and now you are dead \n Game Over ")
                            #break
                        elif forest_right_side_2 == 2:
                            print("You are still in the forest and you have 2 ways")
                            forest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
                            if forest_right_side_3 == 1:
                                print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                               # break
                            elif forest_right_side_3 == 2:
                                print("You left the forest \n You Won this Game")
                               # break
                            elif forest_right_side_3 == 3:
                                print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                               # break
                            if forest_right_side_2 == 2:
                                print("You are still in the forest and you have 2 ways")
                                orest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
                                if forest_right_side_3 == 1:
                                    print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                                    #break
                                elif forest_right_side_3 == 2:
                                    print("You left the forest \n You Won this Game")
                                   # break
                                elif forest_right_side_3 == 3:
                                    print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                                    #break
                                elif forest_right_side_2 == 2:
                                    print("You are still in the forest and you have 2 ways")
                                    forest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
                                    if forest_right_side_3 == 1:
                                        print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                                        #break
                                elif forest_right_side_3 == 2:
                                    print("You left the forest \n You Won this Game")
                                    #break
                                elif forest_right_side_3 == 3:
                                    print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                                    #break
                                elif forest_right_side_2 == 3:
                                    print("Your are still in the Forest and there is only 1 way ")
                                    forest_right_side = int(print("1. go the only way  \n2 go back: "))
                                    if forest_right_side == 1:
                                        print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                                        #break
                                    elif forest_right_side == 2:
                                        print("You are back where you started. \n You give up \n Game Over")
                                        #break
elif choise == 2: #startpoint
    print("You are still in the forest. \n You have only 1 way")
    forest_left_side = int(input("1. go the way \n2. go back: "))
    if forest_left_side == 1:
        print("You are still in the forest. \n You have only 1 way")
        forest_left_side_2 = int(input("1. go the way \n2. go back: "))
        if forest_left_side_2 == 1:
            print("You are still in the forest. \n You have only 1 way")
            forest_left_side_3 = int(input("1. go forwand \n2. go back: "))
            if forest_left_side_3 == 1:
                print("You are back where you started and animels have spotted you. \n You are dead \n Game Over")
                #break
            elif forest_left_side_3 == 2:
                print("You are still in the forest. \n You have only 1 way")
                forest_left_side_2 = int(input("1. go the way \n2. go back: "))
                if forest_left_side_2 == 1:
                    print("You are still in the forest. \n You have only 1 way")
                    forest_left_side_3 = int(input("1. go forwand \n2. go back: "))
                    if forest_left_side_3 == 1:
                        print("You are back where you started and animels have spotted you. \n You are dead \n Game Over")
                    #break
                    elif forest_left_side_3 == 2:
                        print("You are back where you started and animels have spotted you. \n You are dead \n Game Over")
                #break
                elif forest_left_side_2 == 2:
                    print("You are back where you started and animels have spotted you. \n You are dead \n Game Over")
                    #break
        elif forest_left_side_2 == 2:
            print("You are back where you started and animels have spotted you. \n You are dead \n Game Over")
            #break
    elif forest_left_side == 2: # geht zum anfang wieder
        print("Your are still in the Forest and there is only 1 way ")
        forest_right_side = int(print("1.go the only way  \n2.go back: "))
    if forest_right_side == 1:
        print("Your are still in the forest \n Now you have 2 ways")
        forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
        if forest_right_side_2 == 1:
            print("You are still in the forest and there is a dead end you go back where you came")
            print("Your are still in the forest \n Now you have 2 ways")
            forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
            if forest_right_side_2 == 1:
                print("You are still in the forest and there is a dead end you go back where you came")
                print("Your are still in the forest \n Now you have 2 ways")
                forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
                if forest_right_side_2 == 1:
                    print("Because you are running in circles animels have spotted you and now you are dead \n Game Over ")
                    #break
                elif forest_right_side_2 == 2:
                    print("You are still in the forest and you have 2 ways")
                    forest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
                    if forest_right_side_3 == 1:
                        print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                        #break
                    elif forest_right_side_3 == 2:
                        print("You left the forest \n You Won this Game")
                        #break
                    elif forest_right_side_3 == 3:
                        print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                        #break finish here
                elif forest_right_side_2 == 3:
                    print("You are still in the forest and you have 1 ways")
                    orest_right_side = int(input("1. go to the right side \n2. go back: "))
                    if forest_right_side_3 == 1:
                        print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                   # break
                elif forest_right_side_3 == 2:
                    print("You left the forest \n You Won this Game")
                   # break
                elif forest_right_side_3 == 3:
                    print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                   # break
        elif forest_right_side_2 == 2:
            print("You are still in the forest and you have 2 ways")
            forest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
            if forest_right_side_3 == 1:
                print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
               # break
            elif forest_right_side_3 == 2:
                print("You left the forest \n You Won this Game")
               # break
            elif forest_right_side_3 == 3:
                print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
               # break
        elif forest_right_side_2 == 3:
            print("Your are still in the Forest and there is only 1 way ")
            forest_right_side = int(print("1. go back \n2 go the only way: "))
            if forest_right_side == 1:
                print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
               # break
            elif forest_right_side == 2:
                print("You are back where you started. \n You give up \n Game Over")
               # break
    elif forest_right_side == 2:
        print("You are back where you started.")
        print("1. to the right side \n2. to the left side \n3. forward ")
        choise = int(input("Where woud you like to go?: "))
        if choise == 1:
            print("Your are still in the Forest and there is only 1 way ")
            forest_right_side = int(print("1.go the only way  \n2. go back : "))
            if forest_right_side == 1:
                print("Your are still in the forest \n Now you have 2 ways")
                forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
                if forest_right_side_2 == 1:
                    print("You are still in the forest and there is a dead end you go back where you came")
                    print("Your are still in the forest \n Now you have 2 ways")
                    forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
                    if forest_right_side_2 == 1:
                        print("You are still in the forest and there is a dead end you go back where you came")
                        print("Your are still in the forest \n Now you have 2 ways")
                        forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
                        if forest_right_side_2 == 1:
                            print("Because you are running in circles animels have spotted you and now you are dead \n Game Over ")
                           # break
                        elif forest_right_side_2 == 2:
                            print("You are still in the forest and you have 2 ways")
                            forest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
                            if forest_right_side_3 == 1:
                                print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                               # break
                            elif forest_right_side_3 == 2:
                                print("You left the forest \n You Won this Game")
                               # break
                            elif forest_right_side_3 == 3:
                                print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                               # break
                        elif forest_right_side_2 == 2:
                            print("You are still in the forest and you have 2 ways")
                            orest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
                            if forest_right_side_3 == 1:
                                print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                                #break
                            elif forest_right_side_3 == 2:
                                print("You left the forest \n You Won this Game")
                               # break
                            elif forest_right_side_3 == 3:
                                print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                               # break
                            elif forest_right_side_2 == 2:
                                print("You are still in the forest and you have 2 ways")
                                forest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
                                if forest_right_side_3 == 1:
                                    print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                                    #break
                                elif forest_right_side_3 == 2:
                                    print("You left the forest \n You Won this Game")
                                   # break
                                elif forest_right_side_3 == 3:
                                    print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                                   # break
                            elif forest_right_side_2 == 3:
                                print("Your are still in the Forest and there is only 1 way ")
                                forest_right_side = int(print("1. go the only way  \n2 go back: "))
                                if forest_right_side == 1:
                                    print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                                   # break
                                elif forest_right_side == 2:
                                    print("You are back where you started. \n You give up \n Game Over")
                                    #break

                


            
elif choise == 3: #startpoint
    print("You are still in the forest and have only 1 way")
    forest_left_side_other = int(input("1. go the way \n2. go back: "))
    if forest_left_side_other == 1:
        print("Your are still in the forest, you have only 1 way")
        forest_left_side_other_2 = int(input("1. go the way \n2. go back: "))
        if forest_left_side_other_2 == 1:
            print("Your are still in the forest, you have only 1 way")
            forest_left_side_other_3 = int(input("1. go the way \n2. go back: "))
            if forest_left_side_other_3 == 1:
                print("You are back where you started")
                print("1. to the right side \n2. to the left side \n3. forward ")
                choise = int(input("Where woud you like to go?: "))
                if choise == 1:  #startpoint
                    print("Your are still in the Forest and there is only 1 way ")
                    forest_right_side = int(print("1.go the only way  \n2. go back : "))
                    if forest_right_side == 1:
                        print("Your are still in the forest \n Now you have 2 ways")
                        forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
                        if forest_right_side_2 == 1:
                            print("You are still in the forest and there is a dead end you go back where you came")
                            print("Your are still in the forest \n Now you have 2 ways")
                            forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
                            if forest_right_side_2 == 1:
                                print("You are still in the forest and there is a dead end you go back where you came")
                                print("Your are still in the forest \n Now you have 2 ways")
                                forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
                                if forest_right_side_2 == 1:
                                    print("Because you are running in circles animels have spotted you and now you are dead \n Game Over ")
                                    #break
                                elif forest_right_side_2 == 2:
                                    print("You are still in the forest and you have 2 ways")
                                    forest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
                                    if forest_right_side_3 == 1:
                                        print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                                         #break
                                    elif forest_right_side_3 == 2:
                                        print("You left the forest \n You Won this Game")
                                         #break
                                    elif forest_right_side_3 == 3:
                                        print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                                        #break finish here
                                elif forest_right_side_2 == 3:
                                    print("You are still in the forest and you have 1 ways")
                                    forest_right_side = int(input("1. go to the right side \n2. go back: "))
                                    if forest_right_side == 1:
                                        print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                                         # break
                                    elif forest_right_side_3 == 2:
                                        print("You left the forest \n You Won this Game")
                                        # break
                                    elif forest_right_side_3 == 3:
                                        print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                                        # break
                            elif forest_right_side_2 == 2:
                                print("You are still in the forest and you have 2 ways")
                                forest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
                                if forest_right_side_3 == 1:
                                    print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                                    # break
                                elif forest_right_side_3 == 2:
                                    print("You left the forest \n You Won this Game")
                                     # break
                                elif forest_right_side_3 == 3:
                                    print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                                    # break
                            elif forest_right_side_2 == 3:
                                print("Your are still in the Forest and there is only 1 way ")
                                forest_right_side = int(print("1. go back \n2 go the only way: "))
                                if forest_right_side == 1:
                                    print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                                    # break
                                elif forest_right_side == 2:
                                    print("You are back where you started. \n You give up \n Game Over")
                                    # break
                                elif forest_right_side == 2:
                                    print("You are back where you started.")
                                    print("1. to the right side \n2. to the left side \n3. forward ")
                                    choise = int(input("Where woud you like to go?: ")) #startpoint
                                    if choise == 1:
                                        print("Your are still in the Forest and there is only 1 way ")
                                        forest_right_side = int(print("1.go the only way  \n2. go back : "))
                                        if forest_right_side == 1:
                                            print("Your are still in the forest \n Now you have 2 ways")
                                            forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
                                            if forest_right_side_2 == 1:
                                                print("You are still in the forest and there is a dead end you go back where you came")
                                                print("Your are still in the forest \n Now you have 2 ways")
                                                forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
                                                if forest_right_side_2 == 1:
                                                    print("You are still in the forest and there is a dead end you go back where you came")
                                                    print("Your are still in the forest \n Now you have 2 ways")
                                                    forest_right_side_2 = int(input("1. go forwand \n2. to to the right side \n3. go back"))
                                                    if forest_right_side_2 == 1:
                                                        print("Because you are running in circles animels have spotted you and now you are dead \n Game Over ")
                                                        # break
                                            elif forest_right_side_2 == 2:
                                                print("You are still in the forest and you have 2 ways")
                                                forest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
                                                if forest_right_side_3 == 1:
                                                    print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                                                    # break
                                                elif forest_right_side_3 == 2:
                                                    print("You left the forest \n You Won this Game")
                                                    # break
                                                elif forest_right_side_3 == 3:
                                                    print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                                                    # break
                                        elif forest_right_side_2 == 2:
                                            print("You are still in the forest and you have 2 ways")
                                            orest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
                                            if forest_right_side_3 == 1:
                                                print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                                                #break
                                            elif forest_right_side_3 == 2:
                                                print("You left the forest \n You Won this Game")
                                                # break
                                            elif forest_right_side_3 == 3:
                                                print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                                                 # break
                            elif forest_right_side_2 == 2:
                                print("You are still in the forest and you have 2 ways")
                                forest_right_side_3 = int(input("1. go to the right side \n2. go the left side \n3. go back"))
                                if forest_right_side_3 == 1:
                                    print("You are still in the forest and you did run in a animel and you are dead \n Game Over")
                                   #break
                                elif forest_right_side_3 == 2:
                                    print("You left the forest \n You Won this Game")
                                   # break
                                elif forest_right_side_3 == 3:
                                    print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                                   # break
                            elif forest_right_side_2 == 3:
                                print("Your are still in the Forest and there is only 1 way ")
                                forest_right_side = int(print("1. go the only way  \n2 go back: "))
                                if forest_right_side == 1:
                                    print("You are still in the forest and a animel have spotted you. You are dead \n Game Over")
                                   # break
                                elif forest_right_side == 2:
                                    print("You are back where you started. \n You give up \n Game Over")
                                    #break
