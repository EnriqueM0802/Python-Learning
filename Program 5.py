#Program 5: Using Variables and Type Casting
price = 3.95
widgets = 5
print("The price is", price, "for", widgets, "total widgets")
price = 3.45
print("Big sale! The price is now", price)
print("The total price for all the widget is", (price * widgets))

print("The type of price is", type(price))
print("The type of widgets is", type(widgets))

print("If price was an int it would be", int(price))
print("If widgets was a float it would be", float(widgets))