
'''
N students take K apples and distrubte them among each other evenly.
The remaining (the undivisible) part remains in the basket.
How many apples will each single student gets?
How many apples remain in the basket ?
The program reads the number N and K.
It should print the two answers for the questions above.
'''
stud = int(input("enter the number of students"))
appl = int(input("enter the number of apple"))
each = appl // stud
rem = appl % stud
print(f"Each student gets {each} apple")
print(f"The remaining number of apple is {rem}")



