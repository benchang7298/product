product = []
#with open('product.csv', 'r') as f:
#    for line in f:
#        s = line.strip().split(',')
#        print(s)
while True:
    name = input('please enter the name of product: ')
    if name == 'q':
       break
    price = input('please enter the price of product: ')
    product.append([name, price])   
print(product)    

for p in product:
    print(p[0], 'price is', p[1])

with open('product.csv', 'w', encoding='utf-8') as f:
    f.write('PRODUCT,PRICE\n')
    for p in product:
        f.write(p[0] + ',' + str(p[1]) + '\n')
