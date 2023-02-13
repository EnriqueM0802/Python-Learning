#Program 13: If statements
gamerPoints = 10000
region = "Gayville"
if gamerPoints >= 30000:
    print("YOU ARE ULTIMATE GAMER!!!!!!!!!!!!!!!!!!!!!")
elif gamerPoints >= 10000:
    print("You are an ok gamer i guess")
    if region == "Gamerville":
        print("You live in the best gamer place")
    else:
        print("Suffer for all eternity.")
elif gamerPoints >= 20000:
    print("You are a decent gamer")
print("Good luck.")