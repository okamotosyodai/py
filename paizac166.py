x = int(input())
total = 0
rm_amount = x
for coin in [500,100,50,10,5,1]:
    warukazu = rm_amount // coin
    total +=  warukazu
    rm_amount -= coin*warukazu
print(total)
