

'''def division(x,y):
    divide=float(x)/float(y)
    return divide
print division(7,2)

length=len("I have a car, a bike, a guitar, and a stereo")
print length'''

'''x=2848484
print str(x)
z=2.345
print str(z)'''

'''y=float(40)/float(3)
print y

yint=int(y)
print yint

print round(y)
print int(round(y))'''
'''from math import sqrt, exp
print sqrt(16)
print exp(2)'''
'''import math
print math.degrees(90)'''
'''from random import randint
def multiplyby5(x):
    return x*5
def add5(x):
    return x+5
def randomAdd(x):
    y=randin(0,10)
    return x+y'''

'''import smallMathsModule
#print smallMathsModule.multiplyby5(3)

 #print smallMathsModule.add5(10)
print smallMathsModule.randomAdd(50)'''
epic_programmer_dictionary={'tim berners lee':['tbl@gmail.com',111],'Guido Van Rosson':['gvr@gmail.com',222],'Linus Torvald':['lt@gmail.com',333],'larry page':['lp@gmail.com',444],'sergey brin':['sg@gmail.com',555]}
#print epic_programmer_dictionary
'''programmer=epic_programmer_dictionary['tim berners lee']
print programmer'''
personsName=raw_input("Please enter a name: ")
print personsName

#password=raw_input("Please enter your password")
#print password
try:
    personsInfo=epic_programmer_dictionary[personsName]
    print personsName
    
except:
    print 'No information for that name'
