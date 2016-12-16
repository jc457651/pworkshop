__author__ = 'preet'
def square_number(num):
    return(num * num)
print(square_number(5))

def is_prime(value):
    i = 2
    while i < value:
        remainder = value % i
        if remainder == 0:
            return False
        i += 1
    return True

print(is_prime(5))


def inch_to_meter(inch):
    meter = inch/39.37
    return meter
    inch = float(input("enter income"))
    meter = inch_to_meter(inch)
    print("()inches is (:4f)meters".format(inch,meter))

def tax_return(income):
    tax=0
    if income >=16000:
        tax = (income-16000)*0.3
    return tax

income = float(input("enter your income"))
tax = tax_return(income)
if tax==0:
    print("it is not your tax")
else:
    print("tax for income ${:.2f} is $ {:.2f}".format(income,tax))