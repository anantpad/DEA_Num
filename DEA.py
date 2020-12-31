from random import randint
import random

def generateDEANum(name):
    list = []
    y = random.choice([random.choice("B"), random.choice("M")])
    list.append(y)
    for c in name:
        list.append(c.upper())
        break
    x = str(randint(100000, 999999))
    for i in x:
        list.append(i)
    # Add together the first, third and fifth digits,
    # Add together the second, fourth, and sixth digit and multiply this sum by two.
    # Add the result of step one and two together.
    # The last digit of this sum should correspond with the ninth digit of the DEA registration number
    ld = int(((int(list[2]) + int(list[4]) + int(list[6])) + ((int(list[3]) + int(list[5]) + int(list[7])) * 2))%10)
    ld = str(ld)
    list.append(ld)
    deanum = list[0] + list[1] + list[2] + list[3] + list[4] + list[5] + list[6] + list[7] + list[8]
    return deanum

print(generateDEANum("Atharva"))