__author__ = 'jc457651'
"""
CP1404/CP5632 Practical
Color names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
COLOR_NAMES = {"AliceBlue" : "#fof8ff", "AntiqueWhite" : "#faebd7", "AntiqueWhite1" : "#ffefdb", "AntiqueWhite2" : "#eedfcc",
               "AntiqueWhite3" : "#cdcobo", "AntiqueWhite4" : "#8b8378", "aquamarine1" : "#7fffd4"}

color = input("Enter color: ")
while color != "":
    if color in COLOR_NAMES:
        print(color, "is", COLOR_NAMES[color])
    else:
        print("Invalid color")
    color = input("Enter color: ")
    for key in COLOR_NAMES:
        print("{} is {}".format(key,COLOR_NAMES[key]))


