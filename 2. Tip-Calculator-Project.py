print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? Rs"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
final = float((bill * (1 + tip / 100)) / people)

final1 = float(round(final, 2))
print("Each person should pay: " + str(final1))