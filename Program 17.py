#Program 17 Nested For Loops
initalSalesGoal = 20000
multiplier = 100
offMonth = True #change this to false if you do not expect to hane an off month

for monthlyGoal in range(1,13):
    if monthlyGoal == 6 and offMonth:
        print("There is no goal for month 6")
        continue
    monthlySalesGoal = initalSalesGoal + (monthlyGoal * multiplier)
    print("Your sales goal for the month " + str(monthlyGoal) + " is $"+ str(monthlySalesGoal))
    for weeklyGoal in range(1,5):
        print("Your goal for week " + str(weeklyGoal) + "is $" + str(monthlySalesGoal/4))
print("Good luck ith your goals")