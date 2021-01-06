print('i\'m abdulrahma ibraheem'.title() )
print('python is the best!'.title())
print('the cat said mewo!!')


# this program display person's 
# name and addresss

print('\n\nmy name is abdulrhman ibraheem'.title())
print('i\'m living in malaysis-selangor-bsp21\n\n' .title())


# this program display the person's room number!

roomNumber = 503
name = 'abdulrahman ibaraheem'

print('my name is '.title() )
print(name.title())
print('my room\'s number is '.title() ) 
print(roomNumber)

print('\n\nmy name is '.title() + name.title() + 'i am staying in room number'.title() + ' ' + str( roomNumber) )
print('\n\n')

# this program used two variables , topSpeed and distance 

topSpeed = 160
distance = 1322

print('the top speed is '.title() )
print(topSpeed)
print('the sistance is !'.title() )
print(distance)

print('\n\nthe top-speed alowed is '.title() + str( topSpeed ) + ' and the distance is '.title() + str( distance ) + '\n\n')   

# this program used to reassignet a variable

# this program used to assgn the dollar Value 

dollar = 2075
print('i only have '.title() , dollar, ' in my account'.title())
print('i only have ' + str(dollar) + 'in my account!'.title())
print('\n\n')

# here i reassgned the valriable dollar to a new value
dollar = 99.5
print('i only have '.title(), dollar, ' in my account!'.title())
print('i only have '.title() + str( dollar ) + ' ' + 'in my account'.title() )
print('but now i have '.title() + str( dollar ) + ' in my account\n\n'.title() )

# this program used to assign two string Value

fName = 'abdulrahman'
lNmae = 'ibraheem'

# display the vaue reffer to the tr variables 

print('my first name is '.title() + 'my last name is '.title() + lNmae)
print('my full name is '.title() + (fName.title() + ' ' + lNmae.title()))
print('\n\n')

myValue = 99
myValue =0
print(myValue)
print('\n\n')

# Read input from the user 
# title() is build in function used to convert the first letter from each world to upperase

userName = input('what is your name? '.title() )
print('my name is '.title() + userName.title() )
print('\n\n')

# this program will print a grating to the user

# Read the user firstName and lastName
firstName = input('what\'s your first name? '.title() )
lastNmae = input('what\'s yourlastname? '.title() )

print('greating '.title() + (firstName + ' ' + lastNmae))
print('\n\n')

# not: the input function usually return a string value 
# this will case a problem is we used a mathmatical operators
# int(item) the int funcition will conver the variable item into the int Value 
# float(item) the float function will convert the item variable into a floating Value
# age = input('age') => value = '20' eg.... int(age) = 20.. float(age) = 20.0
# int() convert into int value.... float convert into floating value....
# str() conver into string value

workHours = input('how many hours did you work? '.title() )
workHours = int( workHours ) # convert workHour into int value 

# convert workHore into str
print('your allowed to work '.title() + str (workHours) + ' ' + 'per week!!'.title()) 
print('\n\n')

# this program will Read the user input as astring and the will convert to
# floating vlaue then will concanate and print the statment as following

payRate = float( input('what\'s your pay rate? '.title() ) )

print('your total pay rate is '.title() + '$' + str(payRate) + ' ' + 'per year'.title() )
print('\n\n')

# this program to Read the user data... name, age and income

name = input('what is your name? '.title() )
age = int( input('what is your age? '.title() ) )
income = float( input('what is your income? '.title()) )

# here will display the data

print('\n\nhere is the data you entred '.title() )
print('your name is '.title() + name )
print('your age is '.title() + str(age) + ' ' + 'years old'.title() )
print('your monthly income in is '.title() + '$' + str(income) + '\n\n')


# Read the user input cand assign it to the salary varable

salary = input('enter your salary please: '.title() )
bonus = input('enter your bonus: ')
print(type(salary), type(bonus), sep = '\n') # check the type of old variables and print each in one line.

total = int(salary) + int(bonus) # creat a new variable and conver the old variables into int value
print(type(total) ) # check the type of the total variable
print('your pay is '.title() + '$' + str(total) + '\n\n')

# calculat the percentage 

orignalPrice = float( input('what\'s the orignal price? '.title() ) )
discount = float( input('what\'s the discount amount? '.title() ) )

# this to calculate the discount amount and substricted it from orifinal price
discountAmount = orignalPrice * discount / 100
salePrice = orignalPrice - discountAmount

# this line show the prince after the discount
print('\n\nthe sale price is $'.title() + str(salePrice) + '\n\n')

# to calculate the average of 4 class test

# Read the studen tinput and convert them into floating value 
classTest_1 = float( input('enter the score for the class test 1: '.title() ) )
classTest_2 = float( input('enter the score for the class text 2: '.title() ) )
classText_3 = float( input('enter the score for the class test 3: '.title() ) )
classTest_4 = float( input('enter the score for the class test 4: '.title() ) )

# claculating the average score
average = (classTest_1 + classTest_2 + classText_3 + classTest_4) / 4

# print the average score on the screan
print('\n\nthe average score is ' + str(average) + '\n\n')


# converting math formula into python statment 

future_value = float( input('enter the future value: $'.title() ) )
rate = float( input('enter the annual interst rate: '.title() ) )
years = float( input('enter the number of years: '.title() ) )
present_value = future_value / (1 + rate) ** years

print('\n\nyou need to deposit $'.title() + str(present_value) + 
     ' to get '.title() + '$' + str(future_value) + ' in ' + str(years) + 
     'from now'.title() ) 
print('\n\n')


the function of using end = ' ' ... when we do not want the print function to 
start a new line we used end = ' ' and the end of the statments. so the print 
will prit a space instate of print a new line.

print('One', end=' ')
print('Two', end=' ')
print('Three') # output One Two Three
