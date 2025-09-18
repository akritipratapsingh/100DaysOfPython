def PrimeNumberDetector(num):
    numSqrt = int(num**0.5)
    
    if num <= 1:
        print('Not Prime')
    elif num == 2:
        print('Prime')
    
    for i in range(2,numSqrt+1):
        if num%i == 0:
            a = "Not Prime"
            print(a)
            break
        
        
    
    

print("--------------Prime Number Detector--------------")
num = int(input('Enter a number :'))
PrimeNumberDetector(num)
