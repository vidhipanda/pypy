# Author: Vidhi Panda <vidhimpanda@gmail.com>
# Adds two numbers
def add(a,b):
    sum=a+b
    return sum

# Says Hi
def printstrng(strng):
    say="Hi, " +strng
    return say

# Calculate amount based on SI
def amount(p,n,r):
    simplein=(p*n*r)/100
    amt=simplein+p
    return amt

# Prints table for a given no.
def table(n):
    for i in range(1,11):
        p=i*n
        print(str(n) +"*" +str(i) +"=" +str(p))

# Calculate Factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

# The Main function
def main():
    num1=input("Enter 1st number: ")
    num2=input("Enter 2nd number: ")
    x=add(int(num1),int(num2))
    print("Addition is:" +str(x))
    name=input("Enter the name: ")
    y=printstrng(name)
    print(y)
    pri=int(input("Enter the principal: "))
    year=int(input("Enter the time: "))
    rate=int(input("Enter the rate of interest: "))
    z=amount(pri,year,rate)
    print("Amount: " +str(z))
    number=int(input("Enter the number whose table you want to print: "))
    table(number)
    number1=int(input("Enter the number whose factorial you want to print: "))
    s=factorial( number1)
    print("Factorial:" +str(s))


main()
