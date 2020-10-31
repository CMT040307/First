def master():
    #name and age
    name = input("What is your name?")
    age = int(input("How old are you?"))
    print("Hello", name)

    gender = input("Are you male or female?")
    if gender.upper() == "MALE":
        print("I am male too :)")
    else:
        print("Nice, I am male")

    fav_food = input("What is your favourite food?")
    if fav_food.upper() == "PIZZA":
        print("That's my favourite food too :) ")
    else:
        print("That's a great favourite food! Mine is pizza :) ")

    restart = input("Would you like to restart? yes = 1/no = 0")
    if restart.lower() == "1":
        master()
    else:
        exit()
master()