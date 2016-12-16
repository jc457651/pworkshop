sale = float(input("enter your sale: "))

if (sale < 1000):
    bonus = 10/100 * sale
    print("enter bonus is: ",bonus)
elif (1000<=sale):
    bonus = 15/100 * sale
    print("enter bonus is: ",bonus)

