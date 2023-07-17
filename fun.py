word = input()
password = ''

replacements = {'i': '!', 'a': '@', 'm': 'M', 'B': '8', 'o': '.'}

for char in word:
    if char in replacements:
        char = replacements[char]  
        
    password += char
    
password += 'q*s'
    
print (password)
