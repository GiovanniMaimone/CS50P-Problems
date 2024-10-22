#Amount due value
amount_due = int(50)

#Loop until amount due is greater than 0
while amount_due > 0:
    print("Amount Due:", amount_due)

#Insert coin value and subtract from amount due
    coin =int(input("Insert Coin: "))
    if coin in [25,10,5]:
        amount_due -= coin

#Print how many cents in change the user is owed
print("Change Owed: ",abs(amount_due),sep="")
