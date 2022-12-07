# This program finds the minimum number of coins needed for user entered amount
print("Please enter the amount of money to convert:")

#requests dollars to be entered
print("# of dollars:")
dollars = int(input()) * 100

#requests coins to be entered
print("# of cents:")
cents = int(input())

#finds minimum amount of coins needed from user generated amount 
total = dollars + cents
maxquarters = total // 25
afterquarters = total % 25
dimes = afterquarters // 10
afterdimes = afterquarters % 10
nickels = afterdimes // 5
afternickels = afterdimes % 5
pennies = afternickels // 1

###final output
print("The coins are", quarters,"quarters,", dimes, "dimes,", nickels,"nickels and", pennies, "pennies")
