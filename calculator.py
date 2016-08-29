import pdb

'''this is a calculator python program'''
# this program is a simple calculator

def addition(x,y):
	return x+y

def substraction (x,y):
	return x-y

def division(x,y):
	return x/y

def multiplication(x,y):
	return x*y

def program(choice):
	if client_input == 1:
		print addition(num1,num2)
	elif client_input == 2:
		print substraction(num1,num2)
	elif client_input == 3:
		print multiplication(num1,num2)
	elif client_input == 4:
		print division(num1,num2)
	else:
		exit()

print "Welcome to calculators.py"
print "Choose a program"
print "1. Addition"
print "2. Substraction"
print "3. Multiplication"
print "4, Division"
print "5. Exit"

client_input = int(input('Enter choice: '))
num1 = int(input('Value of x: '))
num2 = int(input('Value of y: '))

program(client_input)
