product = []
while True:
    name = input('please enter the name of product: ')
    if name == 'q':
       break
    price = input('please enter the price of product: ')
    product.append([name, price])   
print(product)    

for p in product:
    print(p[0], 'price is', p[1])
