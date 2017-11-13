
import random

play=1
print("\n Hello!")
print("\n This is the guessing game.")
print("One Player or Two Players?")
pnumber=int(input("Type '1' or '2' to pick the number of players."))
if pnumber==1:

    while play == 1:
        print("\nTry to guess the number in the least amount of guesses.")
        print("\n What difficulty would you like?")
        print("1.Easy 2.Medium 3.Hard 4.Extreme 5.Insane 6.Dark Souls 7. Battletoads Co-op")
        str_difficulty = input("Choose your difficulty: ")
        difficulty = int(str_difficulty)

        if difficulty == 1:



            P1Score = 0


            input1 = 0

            randomnumP1 = random.randrange(1, 11)



            while input1 != randomnumP1:
                    input1 = input("\n Pick a number between 1 and 10: ")

                    if input1 > randomnumP1:
                        print("The number you entered is too high")
                        P1Score = P1Score + 1

                    elif input1 < randomnumP1:
                        print("The number you entered is too low")
                        P1Score = P1Score + 1
                    else:
                        print("Congratulations, you got it!")
                        P1Score = P1Score + 1
                        print'\nYour score is '+ str(P1Score)
                        print("\n Would you like to play again?")
                        play = input("1. Yes 2.No")
                        play = int(play)




        if difficulty == 2:

            P1Score = 0

            input1 = 0

            randomnumP1 = random.randrange(1, 21)

            while input1 != randomnumP1:
                input1 = input("\n Pick a number between 1 and 20: ")

                if input1 > randomnumP1:
                    print("The number you entered is too high")
                    P1Score = P1Score + 1

                elif input1 < randomnumP1:
                    print("The number you entered is too low")
                    P1Score = P1Score + 1
                else:
                    print("Congratulations, you got it!")
                    P1Score = P1Score + 1
                    print'\nYour score is ' + str(P1Score)
                    print("\n Would you like to play again?")
                    play = input("1. Yes 2.No")
                    play = int(play)


        if difficulty == 3:

            P1Score = 0


            input1 = 0

            randomnumP1 = random.randrange(1, 101)



            while input1 != randomnumP1:
                input1 = input("\n Pick a number between 1 and 100: ")

                if input1 > randomnumP1:
                    print("The number you entered is too high")
                    P1Score = P1Score + 1

                elif input1<randomnumP1:
                    print("The number you entered is too low")
                    P1Score = P1Score + 1
                else:
                    print("Congratulations, you got it!")
                    P1Score = P1Score + 1
                    print'\nYour score is '+ str(P1Score)
                    print("\n Would you like to play again?")
                    play = input("1. Yes 2.No")
                    play=int(play)
        if difficulty==4:

            P1Score = 0

            input1 = 0

            randomnumP1 = random.randrange(1, 1001)

            while input1 != randomnumP1:
                input1 = input("\n Pick a number between 1 and 1000: ")

                if input1 > randomnumP1:
                    print("The number you entered is too high")
                    P1Score = P1Score + 1

                elif input1 < randomnumP1:
                    print("The number you entered is too low")
                    P1Score = P1Score + 1
                else:
                    print("Congratulations, you got it!")
                    P1Score = P1Score + 1
                    print'\nYour score is ' + str(P1Score)
                    print("\n Would you like to play again?")
                    play = input("1. Yes 2.No")
                    play = int(play)

        if difficulty==5:

            P1Score = 0

            input1 = 0

            randomnumP1 = random.randrange(1, 10001)

            while input1 != randomnumP1:
                input1 = input("\n Pick a number between 1 and 10000: ")

                if input1 > randomnumP1:
                    print("The number you entered is too high")
                    P1Score = P1Score + 1

                elif input1 < randomnumP1:
                    print("The number you entered is too low")
                    P1Score = P1Score + 1
                else:
                    print("Congratulations, you got it!")
                    P1Score = P1Score + 1
                    print'\nYour score is ' + str(P1Score)
                    print("\n Would you like to play again?")
                    play = input("1. Yes 2.No")
                    play = int(play)
        if difficulty==6:

            P1Score = 0

            input1 = 0

            randomnumP1= random.randrange(1, 100001)

            while input1 != randomnumP1:
                input1 = input("\n Pick a number between 1 and 100000: ")

                if input1 > randomnumP1:
                    print("The number you entered is too high")
                    P1Score = P1Score + 1

                elif input1 < randomnumP1:
                    print("The number you entered is too low")
                    P1Score = P1Score + 1
                else:
                    print("Congratulations, you got it!")
                    P1Score = P1Score + 1
                    print'\nYour score is ' + str(P1Score)
                    print("\n Would you like to play again?")
                    play = input("1. Yes 2.No")
                    play = int(play)
        if difficulty==7:

            P1Score = 0

            input1 = 0

            randomnumP1 = random.randrange(1,1000001)

            while input1 != randomnumP1:
                input1 = input("\n Pick a number between 1 and 1000000: ")

                if input1 > randomnumP1:
                    print("The number you entered is too high")
                    P1Score = P1Score + 1

                elif input1 < randomnumP1:
                    print("The number you entered is too low")
                    P1Score = P1Score + 1
                else:
                    print("Congratulations, you got it!")
                    P1Score = P1Score + 1
                    print'\nYour score is ' + str(P1Score)
                    print("\n Would you like to play again?")
                    play = input("1. Yes 2.No")
                    play = int(play)
if pnumber==2:
    while play == 1:
        print("\n What difficulty would you like?")
        print("1.Easy 2.Medium 3.Hard 4.Exteme 5.Insane 6. Dark Souls 7. Battletoads Co-op")
        str_difficulty = input("Choose your difficulty")
        difficulty= int(str_difficulty)

        if difficulty == 1:
            PlayerOne = raw_input("Who is player one?")
            PlayerTwo = raw_input("Who is player two?")


            P1Score = 0
            P2Score = 0
            for i in [1,2,3]:
                input1 = 0
                input2 = 0
                randomnumP1 = random.randrange(1, 11)
                randomnumP2 = random.randrange(1, 11)
                print '\nROUND' + str(i)

                while input1 != randomnumP1:
                    input1 = input("\n"+PlayerOne+", Pick a number between 1 and 10: ")

                    if input1>randomnumP1:
                        print("The number you entered is too high")
                        P1Score=P1Score+1

                    elif  input1<randomnumP1:
                        print("The number you entered is too low")
                        P1Score = P1Score + 1
                    else:
                        print("Congratulations, you got it!")
                        P1Score = P1Score + 1
                        print(PlayerOne+"'s score is", P1Score)

                while input2 != randomnumP2:
                    input2=input("\n"+PlayerTwo+", Pick a number between 1 and 10: ")

                    if input2 > randomnumP2:
                        print("The number you entered is too high")
                        P2Score = P2Score + 1
                    elif input2 < randomnumP2:
                        print("The number you entered is too low")
                        P2Score = P2Score + 1
                    else:
                        print("Congratulations, you got it!")
                        P2Score = P2Score + 1
                        print(PlayerTwo+"'s score is", P2Score)

            if  P1Score>P2Score:
                print(PlayerTwo+" Wins!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)
            elif  P2Score>P1Score:
                print(PlayerOne+" Wins!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)
            else:
                print("It's a tie!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)



        if difficulty == 2:
            PlayerOne = raw_input("Who is player one?")
            PlayerTwo = raw_input("Who is player two?")


            P1Score = 0
            P2Score = 0
            for i in [1,2,3]:
                input1 = 0
                input2 = 0
                randomnumP1 = random.randrange(1, 21)
                randomnumP2 = random.randrange(1, 21)
                print '\nROUND' + str(i)

                while input1 != randomnumP1:
                    input1 = input("\n"+PlayerOne+", Pick a number between 1 and 20: ")

                    if input1>randomnumP1:
                        print("The number you entered is too high")
                        P1Score=P1Score+1

                    elif  input1<randomnumP1:
                        print("The number you entered is too low")
                        P1Score = P1Score + 1
                    else:
                        print("Congratulations, you got it!")
                        P1Score = P1Score + 1
                        print(PlayerOne+"'s score is", P1Score)

                while input2 != randomnumP2:
                    input2=input("\n"+PlayerTwo+", Pick a number between 1 and 20: ")

                    if input2 > randomnumP2:
                        print("The number you entered is too high")
                        P2Score = P2Score + 1
                    elif input2 < randomnumP2:
                        print("The number you entered is too low")
                        P2Score = P2Score + 1
                    else:
                        print("Congratulations, you got it!")
                        P2Score = P2Score + 1
                        print(PlayerTwo+"'s score is", P2Score)
            if  P1Score>P2Score:
                print(PlayerTwo+" Wins!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)
            elif  P2Score>P1Score:
                print(PlayerOne+" Wins!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)
            else:
                print("It's a tie!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)



        if difficulty == 3:
            PlayerOne = raw_input("Who is player one?")
            PlayerTwo = raw_input("Who is player two?")


            P1Score = 0
            P2Score = 0
            for i in [1,2,3]:
                input1 = 0
                input2 = 0
                randomnumP1 = random.randrange(1, 101)
                randomnumP2 = random.randrange(1, 101)
                print '\nROUND' + str(i)

                while input1 != randomnumP1:
                    input1 = input("\n"+PlayerOne+", Pick a number between 1 and 100: ")

                    if input1>randomnumP1:
                        print("The number you entered is too high")
                        P1Score=P1Score+1

                    elif  input1<randomnumP1:
                        print("The number you entered is too low")
                        P1Score = P1Score + 1
                    else:
                        print("Congratulations, you got it!")
                        P1Score = P1Score + 1
                        print(PlayerOne+"'s score is", P1Score)

                while input2 != randomnumP2:
                    input2=input("\n"+PlayerTwo+", Pick a number between 1 and 100: ")

                    if input2 > randomnumP2:
                        print("The number you entered is too high")
                        P2Score = P2Score + 1
                    elif input2 < randomnumP2:
                        print("The number you entered is too low")
                        P2Score = P2Score + 1
                    else:
                        print("Congratulations, you got it!")
                        P2Score = P2Score + 1
                        print(PlayerTwo+"'s score is", P2Score)

            if  P1Score>P2Score:
                print(PlayerTwo+" Wins!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)
            elif  P2Score>P1Score:
                print(PlayerOne+" Wins!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)
            else:
                print("It's a tie!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)
        if difficulty == 4:
            PlayerOne = raw_input("Who is player one?")
            PlayerTwo = raw_input("Who is player two?")


            P1Score = 0
            P2Score = 0
            for i in [1,2,3]:
                input1 = 0
                input2 = 0
                randomnumP1 = random.randrange(1, 1001)
                randomnumP2 = random.randrange(1, 1001)
                print '\nROUND' + str(i)

                while input1 != randomnumP1:
                    input1 = input("\n"+PlayerOne+", Pick a number between 1 and 1000: ")

                    if input1>randomnumP1:
                        print("The number you entered is too high")
                        P1Score=P1Score+1

                    elif  input1<randomnumP1:
                        print("The number you entered is too low")
                        P1Score = P1Score + 1
                    else:
                        print("Congratulations, you got it!")
                        P1Score = P1Score + 1
                        print(PlayerOne+"'s score is", P1Score)

                while input2 != randomnumP2:
                    input2=input("\n"+PlayerTwo+", Pick a number between 1 and 1000: ")

                    if input2 > randomnumP2:
                        print("The number you entered is too high")
                        P2Score = P2Score + 1
                    elif input2 < randomnumP2:
                        print("The number you entered is too low")
                        P2Score = P2Score + 1
                    else:
                        print("Congratulations, you got it!")
                        P2Score = P2Score + 1
                        print(PlayerTwo+"'s score is", P2Score)

            if  P1Score>P2Score:
                print(PlayerTwo+" Wins!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)
            elif  P2Score>P1Score:
                print(PlayerOne+" Wins!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)
            else:
                print("It's a tie!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)

        if difficulty == 5:
            PlayerOne = raw_input("Who is player one?")
            PlayerTwo = raw_input("Who is player two?")


            P1Score = 0
            P2Score = 0
            for i in [1,2,3]:
                input1 = 0
                input2 = 0
                randomnumP1 = random.randrange(1, 10001)
                randomnumP2 = random.randrange(1, 10001)
                print '\nROUND' + str(i)

                while input1 != randomnumP1:
                    input1 = input("\n"+PlayerOne+", Pick a number between 1 and 10000: ")

                    if input1>randomnumP1:
                        print("The number you entered is too high")
                        P1Score=P1Score+1

                    elif  input1<randomnumP1:
                        print("The number you entered is too low")
                        P1Score = P1Score + 1
                    else:
                        print("Congratulations, you got it!")
                        P1Score = P1Score + 1
                        print(PlayerOne+"'s score is", P1Score)

                while input2 != randomnumP2:
                    input2=input("\n"+PlayerTwo+", Pick a number between 1 and 10000: ")

                    if input2 > randomnumP2:
                        print("The number you entered is too high")
                        P2Score = P2Score + 1
                    elif input2 < randomnumP2:
                        print("The number you entered is too low")
                        P2Score = P2Score + 1
                    else:
                        print("Congratulations, you got it!")
                        P2Score = P2Score + 1
                        print(PlayerTwo+"'s score is", P2Score)

            if  P1Score>P2Score:
                print(PlayerTwo+" Wins!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)
            elif  P2Score>P1Score:
                print(PlayerOne+" Wins!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)
            else:
                print("It's a tie!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)

        if difficulty == 6:
            PlayerOne = raw_input("Who is player one?")
            PlayerTwo = raw_input("Who is player two?")


            P1Score = 0
            P2Score = 0
            for i in [1,2,3]:
                input1 = 0
                input2 = 0
                randomnumP1 = random.randrange(1, 100001)
                randomnumP2 = random.randrange(1, 100001)
                print '\nROUND' + str(i)

                while input1 != randomnumP1:
                    input1 = input("\n"+PlayerOne+", Pick a number between 1 and 100000: ")

                    if input1>randomnumP1:
                        print("The number you entered is too high")
                        P1Score=P1Score+1

                    elif  input1<randomnumP1:
                        print("The number you entered is too low")
                        P1Score = P1Score + 1
                    else:
                        print("Congratulations, you got it!")
                        P1Score = P1Score + 1
                        print(PlayerOne+"'s score is", P1Score)

                while input2 != randomnumP2:
                    input2=input("\n"+PlayerTwo+", Pick a number between 1 and 100000: ")

                    if input2 > randomnumP2:
                        print("The number you entered is too high")
                        P2Score = P2Score + 1
                    elif input2 < randomnumP2:
                        print("The number you entered is too low")
                        P2Score = P2Score + 1
                    else:
                        print("Congratulations, you got it!")
                        P2Score = P2Score + 1
                        print(PlayerTwo+"'s score is", P2Score)

            if  P1Score>P2Score:
                print(PlayerTwo+" Wins!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)
            elif  P2Score>P1Score:
                print(PlayerOne+" Wins!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)
            else:
                print("It's a tie!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)

        if difficulty == 7:
            PlayerOne = raw_input("Who is player one?")
            PlayerTwo = raw_input("Who is player two?")


            P1Score = 0
            P2Score = 0
            for i in [1,2,3]:
                input1 = 0
                input2 = 0
                randomnumP1 = random.randrange(1, 1000001)
                randomnumP2 = random.randrange(1, 11)
                print '\nROUND' + str(i)

                while input1 != randomnumP1:
                    input1 = input("\n"+PlayerOne+", Pick a number between 1 and 1000000: ")

                    if input1>randomnumP1:
                        print("The number you entered is too high")
                        P1Score=P1Score+1

                    elif  input1<randomnumP1:
                        print("The number you entered is too low")
                        P1Score = P1Score + 1
                    else:
                        print("Congratulations, you got it!")
                        P1Score = P1Score + 1
                        print(PlayerOne+"'s score is", P1Score)

                while input2 != randomnumP2:
                    input2=input("\n"+PlayerTwo+", Pick a number between 1 and 1000000: ")

                    if input2 > randomnumP2:
                        print("The number you entered is too high")
                        P2Score = P2Score + 1
                    elif input2 < randomnumP2:
                        print("The number you entered is too low")
                        P2Score = P2Score + 1
                    else:
                        print("Congratulations, you got it!")
                        P2Score = P2Score + 1
                        print(PlayerTwo+"'s score is", P2Score)

            if  P1Score>P2Score:
                print(PlayerTwo+" Wins!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)
            elif  P2Score>P1Score:
                print(PlayerOne+" Wins!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)
            else:
                print("It's a tie!")
                print("\n Would you like to play again?")
                play = input("1. Yes 2.No")
                play = int(play)


