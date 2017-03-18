#Create a simple program that mimics the functionality of a calculator. It should;
#	Input: the user should provide the two numbers to be manipulated and the operation to be used.
#	Output: the user should get an answer based on the operation specified.
#Your calculator should be user friendly in that it should provide instructions on how the user should use it.
#The operations it should carry out include:
#	Addition
#	Subtraction
#	Multiplication
#	Division
#	Square of a number


a=int(input("Enter a number"))
b=int(input("Enter a number"))
operator=input("enter an operator")
if operator is'+':
    print(a+b)
if operator is'-':
    print(a-b)
if operator is'*':
    print(a*b)
if operator is'/':
    print(a/b)
if operator is'**':
    print(a**b)