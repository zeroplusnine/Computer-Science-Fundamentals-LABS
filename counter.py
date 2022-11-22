
print("Please enter the number of coins:")

print("# of quarters:")
quarters = int(input())
total_quarters = quarters *25

print("# of dimes:")
dimes = int(input())
total_dimes = dimes * 10

print("# of nickels:")
nickels = int(input())
total_nickels = nickels *5

print("# of pennies:")
pennies = int(input())
total_pennies = pennies *1

total = total_quarters + total_dimes +total_nickels +total_pennies

dollars = total // 100
cents = total % 100

print("The total is", dollars, "dollars and", cents, "cents")