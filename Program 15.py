#Program 15 For Loops
initialSalesGoal =  20000
multiplier = 100

for monthlyGoa in range(1,13):
    if monthlyGoa == 6:
        print("There is no goal for month 6")
        continue
    monthlySalesGoal = initialSalesGoal + (monthlyGoa * multiplier)
    print ("Your sales goal for the month " + str(monthlyGoa) + " is "+ str(monthlyGoa))

print("Good luck with your goals")