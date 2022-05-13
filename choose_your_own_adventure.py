from unicodedata import name


name = input ("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()


if answer == "left":
    answer = input("You have come to a river, you can 'walk' around it or 'swim' across. What would you like to do? ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked so many miles, ran out of water and you lost the game")
    else:
        print('Not a valid option. You lose.')

elif answer =="right":
    answer  = input("You come to a bridge. It looks wobbly, would you like to cross it or head back (Cross/Back)? ")
    if answer == "back":
        print("You have gone back. You lose.")

    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
        if answer == "yes":
            print("You talk to the stranger and they give you treasure. You WIN! ")
        elif answer == "no":
            print("You lose the chance of finding the treasure by not talking to the stranger. You lose!")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')
print("Thank you trying", name)