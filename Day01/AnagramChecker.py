# Anagram Checker

# function to calculate the length
def length(chars):
    i = 0
    
    for char in chars:
        i += 1
    return i


def AnagramChecker():
    
    a = input('Enter a word 1:').replace(" ","").lower()
    b = input('Enter a word 2:').replace(" ","").lower()
    
    count1 = {}
    count2 = {}
    
    # Rule 1 : checks for equal length
    if length(a) != length(b):
        return False
    
    #Rule 2: check for Char frequency
    for char in a:
        if char in count1:
            count1[char]+= 1 
        else:
            count1[char]= 1
    print(f"The char counts in word 1 {count1}")
    
    for char in b:
        if char in count2:
            count2[char]+=1 
        else:
            count2[char]=1
    print(f"The char counts in word 2 {count2}")
    
    # Rule 3: Checks for counts of each word
    if count2 == count1:
        print('Anagram')
    else:
        print('Not Anagram')

# Calling the method 
AnagramChecker()