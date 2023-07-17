triangle_char = input('Enter a character:\n') # obtains input for character used in right triangle
triangle_height = int(input('Enter triangle height:\n')) # defines height from input
print('') # displays space

for i in range (1, triangle_height + 1): #begins for loop for triangle height ranges
    line = triangle_char + ' ' + (triangle_char + ' ') * (i - 1) # sets up line criteria 
    print (line) # displays output


