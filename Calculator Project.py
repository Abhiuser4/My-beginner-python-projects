# Calculator Project

First_number=int(input('Enter first number:'))
second_number=int(input('Enter second number:'))
Operator=input('enter a operator (+, - ,* , /)')

if Operator =='+':
    sum=First_number + second_number
    print(sum)
elif Operator =='-':
    sum=First_number - second_number
    print(sum)
elif Operator =='*':
    sum=First_number * second_number
    print(sum)
elif Operator =='/':
    if second_number !=0:
        sum=First_number /second_number 
        print(sum)
    else:
        print('Not divisible by 0')

else:
    print('Invaild operator ')