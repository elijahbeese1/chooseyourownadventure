print("Welcome to Choose Your Own Adventure!")
print(" ")
print("Make sure to type your answer exactly how it is printed in the question!")
print(" ")
print(" ")
print("Do you walk across the street?")
choice = input("yes or no?")
if choice == 'yes':
    print("You suddenly feel the need to commit a crime. Do you kill a pedestrian?")
    choice2 = input("yes or no?")
    if choice2 == 'yes':
        print("You, a white man, killed a black woman. BLM protests erupt throughout the nation, and you are charged with murder. Do you attempt to flee the country or plead insanity?")
        choice3 = input("flee or plead?")
        if choice3 == 'flee':
            print("You decide to seek refuge in Canada. However, you are torn between two fake names. Should it be Ben Dover or Dixie Normous?")
            choice4 = input("Ben or Dixie?")
            if choice4 == 'Ben':
                print("You successfully live a life as Ben Dover up until the ripe old age of 67.")
            if choice4 == 'Dixie':
                print("The police eventually catch up to you. As you flee your apartment, you are trampled and killed by a horse.")
            
        elif choice3 == 'plead':
            print("You are convicted as being insane. You spend your final years in the loony bin.") 

    elif choice2 == 'no':
        print("As you continue, you find a lottery ticket on the sidewalk. Do you pick it up?")
        

        choice5 = input("yes or no?")
        if choice5 == 'no':
            print("You continue down the sidewalk, and are confronted by a thug. Do you do what he says?")
            choice6 = input("yes or no?")
            if choice6 == 'yes':
                print("You give him everything you have, and go on to live an uneventful, mediocre at best, life")
            elif choice6 == 'no':
                print("You are shot in street because you didn't give the thug the $12 in your pocket, and your killer is never found. No one attends your funeral.")

        elif choice5 == 'yes':
            print("Do you return it to the store or play it?")
            choice7 = input("return or play")
            if choice7 == 'return':
                print("The next day you hear on the news that the ticket you returned was worth 28 million dollars. News of this leads to your suicide.")
            elif choice7 == 'play':
                print("It's a winner! You live a happy life up until the day your wife murders you for your money.")
            
elif choice == 'no':
    print("Your stomach begins to grumble. Do you want a BigMac or some thai?")
    choice8 = input("BigMac or thai?")
    if choice8 == 'BigMac':
        print("You are the one billionth customer, and get your meal for free! Do you repay this act of kindness by donating to St. Judes Foundation at checkout?")
        choice9 = input("yes or no?")
        if choice9 == 'yes':
            print("People cheer as you drop a couple of dimes into the bucket. You are featured on the local news as being the kindest man in town. You contemplate running for city office. Do you?")
            choice10 = input("yes or no?")
            if choice10 == 'yes':
                print("You go on to have a successful career in local politics, and eventually become town mayor.")
            elif choice10 == 'no':
                print("You die twelve years later. The only thing to your name is a certificate naming you the one billionth customer of McDonald's.")
        elif choice9 == 'no':
            print("On your way out the building someone calls you a dimwit. Do you attack him?")
            choice11 = input("yes or no?")
            if choice11 == 'yes':
                print("You are charged with assualt and spend 9 months in jail.")
            elif choice11 == 'no':
                print("You walk out and never return to another McDonald's again.")
        elif choice9 == 'no':
            print("You die twelve years later. All you have to your name is a certificate that names you McDonald's billionth customer.")
            
    elif choice8 == 'thai':
        print("You order some spicy shrimp soup. As you are eating, you choke on a piece of shrimp and die.")
        
print(" ")
print(" ")
print(" ")
print("Game Over!")
print("Thanks for playing...")

