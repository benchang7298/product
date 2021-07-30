product = []
while True:
    name = input('please enter the name of product: ')
    if name == 'q':
       break
    price = input('please enter the price of product: ')
    product.append([name, price])   
print(product)    
