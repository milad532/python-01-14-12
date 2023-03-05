from operator import mod

number1=input("Enter a 3 digit number\n")
number1=int(number1)
number2=int(0)
if number1>=100 and number1<1000 : # for abc we have a=abc/100 b=(abc-a*100)/10 c=abc%10
    number2=int(number1/100) #  a ---> c
    number2+=int((number1%100-number1%10)) # b --->b*10
    number2+=int((number1%10)*100) # c --->c*100-->a
    print (2*number2)
else :
    print("number isn't 3digit number\n")