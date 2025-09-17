import string

def WordFrequencyCounter():
    
    statement = input("Enter a statement: ").lower()
    
    # Removing Punctuation
    for p in string.punctuation:
        statement = statement.replace(p,"")
    
    # Tokenization
    statement = statement.split()
    
    Counter = {}
    
    for word in statement:
        if word in Counter:
            Counter[word] += 1 
        else:
            Counter[word] = 1 
            
    print(f"The Word Frequency in the provide statement: {Counter}")

    
WordFrequencyCounter()