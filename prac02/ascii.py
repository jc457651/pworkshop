__author__ = 'jc449767'
lower = 33
upper = 100
print("Enter a number ({} - {}):".format(lower,upper))
print("ASCII Code   CHAR")
print("----------   ----")
for i in range(lower, upper):
    print("{:>6} {:>8}".format(i, chr(i)))

