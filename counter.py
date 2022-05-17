
# Counts value of coins and converts to dollars

print("Please enter number of coins")
def sum(quarters, dimes, nickels, pennies):
    return (quarters + dimes + nickels + pennies)

quarters = int(input('# of quarters: '))
dimes = int(input('# of dimes: '))
nickels = int(input('# of nickels: '))
pennies = int(input('# of pennies: '))
value = quarters *.25 + dimes*.1 + nickels*.05 + pennies*.01

print("The total is $", value)


