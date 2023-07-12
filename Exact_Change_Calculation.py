total_change = int(input())

if total_change <= 0:
    print('No change')

dollar = 100
quarter = 25
dime = 10
nickel = 5
penny = 1

dollar_count = int(total_change / dollar)
if dollar_count > 1:
    print (str(dollar_count) + ' Dollars')
elif dollar_count == 1:
    print(str(dollar_count) + ' Dollar')


new_total = total_change - dollar * dollar_count

quarter_count = int(new_total / quarter)
if quarter_count > 1:
    print (str(quarter_count) + ' Quarters')
elif quarter_count == 1:
    print(str(quarter_count) + ' Quarter')


new_total = new_total - quarter * quarter_count
dime_count = int(new_total / dime)
if dime_count > 1:
    print (str(dime_count) + ' Dimes')
elif dime_count == 1:
    print(str(dime_count) + ' Dime')

new_total = new_total - dime * dime_count
nickel_count = int(new_total / nickel)
if nickel_count > 1:
    print (str(nickel_count) + ' Nickels')
elif nickel_count == 1:
    print(str(nickel_count) + ' Nickel')

new_total = new_total - nickel * nickel_count
penny_count = int(new_total / penny)
if penny_count > 1:
    print (str(penny_count) + ' Pennies')
elif penny_count == 1:
    print(str(penny_count) + ' Penny')