# Palindrome No Checker
def reverse(num):
    revNum =    0
    
    while num > 0:
        a = num % 10
        revNum = revNum*10 + a
        
        num//=10
    return revNum;

print('Palindrome number Checker')

num = int(input('Enter a number :'))
if num ==  reverse(num):
    print('It is a Palindrome number')
else:
    print('Not a palindrome number')