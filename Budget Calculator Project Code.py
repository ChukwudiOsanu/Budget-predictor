#Asks the user to input their Income, dependents, car, and counties (Base code, spell check Emma Berman)
Income = float(input("Input monthly income: "))
Adults = float(input("Input number of adults dependents: "))
Child = float(input("Input number of child dependents: "))
Car = input("Do you own a car? (Yes or No): ")
County= input("Enter county (Cobb, Gwinnett, Fulton, Clayton, Dekalb): ")


#All Variables that would be calculated for are listed below
food = 0
housing = 0
insurance = 0
utility = 0
transportation_insurance= 0
miscellaneous = 0
savings = 0

#County if state,ents start (Rabin-Research and Code)
#First County Cobb
if County.lower() == "cobb":
    #Checks if user has car (Solution to .islower- Rabin Roy, Kahlil Mays)
    if Car.lower() == "yes":
        housing += 1255
        food += ((250 + (250 * Adults) + (150 * Child))*1.06)
        utility += 245
        transportation_insurance += (Income * 0.04)
        insurance += (527 + (527 * Adults) + (315 * Child))
    #If you answer no to having a car
    elif Car.lower() == "no":
        housing += 1255
        food += (250 + (250 * Adults) + (150 * Child))
        utility += 245
        insurance += (527 + (527 * Adults) + (315 * Child))
    #If user inputs something other than yes or no, this is returned to them
    else:
        print("Not valid car entry")

#Checks if county is Gwinnett (Emma Berman-Research and code)
elif County.lower() == "gwinnett":
    if Car.lower() == "yes":
        housing += 1338
        food += ((250 + (250 * Adults) + (150 * Child))*1.06)
        utility += 270
        transportation_insurance += (Income * 0.04)
        insurance += (527 + (527 * Adults) + (315 * Child))
    elif Car.lower() == "no":
        housing += 1338
        food += (250 + (250 * Adults) + (150 * Child))
        utility += 270
        insurance += (527 + (527 * Adults) + (315 * Child))
    else:
        print("Not valid car entry")

#Checks if county is Fulton (Kahlil Mays- Research and Code)
elif County.lower() == "fulton":
    if Car.lower() == "yes":
        housing += 1324
        food += ((250 + (250 * Adults) + (150 * Child))*1.089)
        utility += 296.10
        transportation_insurance += (Income * 0.04)
        insurance += (527 + (527 * Adults) + (315 * Child))
    elif Car.lower() == "no":
        housing += 1324
        food += (250 + (250 * Adults) + (150 * Child))
        utility += 296.10
        insurance += (527 + (527 * Adults) + (315 * Child))
    else:
        print("Not valid car entry")
#Checks if county is Clayton (Chukwudi Osanu- Research and Code)
elif County.lower() == "clayton":
    if Car.lower() == "yes":
        housing += 1050
        food += ((250 + (250 * Adults) + (150 * Child))*1.08)
        utility += 205
        transportation_insurance += (Income * 0.04)
        insurance += (527 + (527 * Adults) + (315 * Child))
    elif Car.lower() == "no":
        housing += 1050
        food += (250 + (250 * Adults) + (150 * Child))
        utility += 205
        insurance += (527 + (527 * Adults) + (315 * Child))
    else:
        print("Not valid car entry")

#Checks if county is Dekalb(Eliyas Abdi- Research and Code)
elif County.lower() == "dekalb":
    if Car.lower() == "yes":
        housing += 1260
        food += ((250 + (250 * Adults) + (150 * Child))*1.08)
        utility += 223
        transportation_insurance += (Income * 0.04)
        insurance += (527 + (527 * Adults) + (315 * Child))
    elif Car.lower() == "no":
        housing += 1260
        food += (250 + (250 * Adults) + (150 * Child))
        utility += 223
        insurance += (527 + (527 * Adults) + (315 * Child))
    else:
        print("Not valid car entry")

#If input is not one of the chosen counties this is printed (Collective)
else:
    print("Not valid county entry")

#Gives a budget with each category broken down
#If there isn't enough money, it tells the user they cannot afford to live there
Leftover = Income - savings - housing - food- utility - transportation_insurance - insurance
if Leftover < 0:
    print("You do not have enough money to live in", County)
#Runs final calculations for savings and miscellaneous 
else:
    savings = ((Income - savings - housing - food- utility - transportation_insurance - insurance) * .10)
    miscellaneous = (Income - savings - housing - food- utility - transportation_insurance - insurance)
#Prints out each $ amount per category ($ idea and round()- Emma Berman)
    print("Your budget is: ")
    print("Food: ", "$", round(food,2))
    print("Housing: ", "$", round(housing,2))
    print("Insurance: ", "$", round(insurance,2))
    print("Utility: ", "$", round(utility,2))
    print("Transportation Insurance: ", "$", round(transportation_insurance,2))
    print("Savings: ", "$",round(savings,2))
    print("Miscellaneous: ", "$", round(miscellaneous,2))


