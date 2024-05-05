#Calculator Assignment

#Operations Menu
print("\n======================================= \n\n")
print("\t \t \tCalculator Dev \n\n")

print("***************************************")
print("\t \t \t \tMENU")
print("***************************************\n")

print("Choose an Option :\n")
choose = int(input(print(" 1) Add Numbers \n 2) Subtract Numbers \n 3) Divide Numbers \n 4) Multiply Numbers \n 5) Exponent Numbers \n 6) Modulus Numbers")))

#Taking Input from user

if choose ==1 | choose ==2 | choose ==3 | choose ==4 | choose ==5 | choose ==6:
    numOne = int(input(print("Enter Your First Number :")))
    numTwo = int(input(print("Enter Your Second Number :")))

#Addition Operation

if choose == 1:
    numOne = int(input(print("Enter Your First Number :")))
    numTwo = int(input(print("Enter Your Second Number :")))
    sum = numOne + numTwo
    print("Sum Of Numbers = ",sum)

#Subtraction Operation

elif choose == 2:
    numOne = int(input(print("Enter Your First Number :")))
    numTwo = int(input(print("Enter Your Second Number :")))
    sub = numOne - numTwo
    print("Differene Of Numbers = ", sub)

#Division Opreation

elif choose == 3:
    numOne = int(input(print("Enter Your First Number :")))
    numTwo = int(input(print("Enter Your Second Number :")))
    div = numOne / numTwo
    print("Division Of Numbers = ",div)
#Multiplication Operation

elif choose == 4:
    numOne = int(input(print("Enter Your First Number :")))
    numTwo = int(input(print("Enter Your Second Number :")))
    mul = numOne * numTwo
    print("Multiple Of Numbers = ",mul)

#Exponential Operation

elif choose == 5:
    numOne = int(input(print("Enter Your First Number :")))
    numTwo = int(input(print("Enter Your Second Number :")))
    exp = numOne ** numTwo
    print("Exponent Of Numbers = ",exp)

#Modulus Operation

elif choose == 6:
    numOne = int(input(print("Enter Your First Number :")))
    numTwo = int(input(print("Enter Your Second Number :")))
    mod = numOne % numTwo
    print("Modulus Of Numbers = ",mod)
else :
    print("Invalid Choice!")
