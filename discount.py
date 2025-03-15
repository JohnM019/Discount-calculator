def calculate_discount(price, discount_percent):
    if (discount_percent >= 20):
        return (20/100 * price)
    else:
        return price
    

price = int(input('Enter the price of the commodity: '))
disc = int(input('Enter the discount percentage: '))

if (disc < 20):
    print(f'Discount was not applied \nprice is {price}')
else:
    print(f'Discount applied \nThe price is {price - calculate_discount(price, disc)}')