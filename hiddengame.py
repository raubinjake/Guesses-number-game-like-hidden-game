inc = 0
rem = 9
print("you have only ten (10) times guesess for this game")
print("Guesess only between 0 to 30 ")
while (inc < 10):

    inp = int(input("Guess the number  "))
    if inp<18 and inp!=18:
        print("try again! enter nearest greatest number ")
        print("you have left only ",rem," chance")
        inc = inc + 1
        rem = rem - 1
    elif inp>18 and inp!=18:
        print("try again! enter nearest smallest number ")
        print("you have left only ", rem, " chance")
        inc = inc + 1
        rem = rem - 1
    else:
       print("you won the game :) ")
       print("you attemp in ",inc+1,"times")
       break
if inc >= 10:
    print("Game over! You lossed the no. of guesess")
    print("try again!")
