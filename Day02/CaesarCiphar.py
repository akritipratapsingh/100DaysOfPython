def CaesarCipher(word,shift):
    
    word = word.lower();
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    
    lookup = {char: idx for idx, char in enumerate(alpha)}
    
    for char in word:
        if char in lookup:
            idx = lookup[char]
            newIdx = (idx+shift)%26
            result += alpha[newIdx]
            
        else:
            result += char
    
    print(f"Encrypted code : {result}")
    

print("-----------Caesar Cipher-------------")
word = input("Enter a word: ")
shift = int(input("Enter the shift key : "))
CaesarCipher(word, shift)


