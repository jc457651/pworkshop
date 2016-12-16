firstname = 'harpreet'
lastname = 'kaur'

age = int(input("enter your age:"))

fruits = ["orange", 'mango', 'banana', 'melon']
sequences = [1,2,3,4,5,6,7,8,9]
print ('today is the  1st day of programming')
print (firstname + " " + lastname)
print(25, firstname + " " + lastname)
print(fruits[0])
for value in fruits:
    print (value)

for value in sequences:
    print (value)

number = 0
while (number < 10) :
    print (number)
    number = number + 1

if (age < 18):
   print ('you are too young')
elif (18<=age and age < 50):
     print ('you are major')
else:
     print ('you are too old')





