instruction="welcome to our program.\ninput negative number into numbe of item to quit"


print(instruction)
numberofitem=1
while numberofitem>0:
    numberofitem = int(input('enter number of items:'))
    costperitem = float (input('enter cost:$'))
    salesofitem = numberofitem * costperitem
    if salesofitem > 100:
        salesofitem = salesofitem - (salesofitem * 0.1)
        print("the total cost:",salesofitem)