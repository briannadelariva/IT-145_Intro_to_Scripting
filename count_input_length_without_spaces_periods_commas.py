user_text = input() # Asks user for input
count = 0 #sets count of characters to zero

for char in user_text: #creates for loop
    if char != ' ' and char != '.' and char != ',': #alerts to ignore spaces, periods, and commas in count
        count = count + 1 #adds to count itself plus one for each chacter not a space, period,  or comma
print (count) #displays the final count