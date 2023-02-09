#Program 7: Using Indexing in Lists
regions = ["North", "South", "East", "West"]
sales = [ 30000, 20000, 40000, 35000]
employees = ["Alice", "Vera", "Mary", "Mel"]
print("Region:",regions[1],"\tSales: ",sales[0])
print("Region:",regions[-1], "\tSales: ",sales[-1])

employees[2] = "Andrea"

for employee in employees:
    print(employee)