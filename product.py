import os

product = []
# Read the file
if os.path.isfile('product.csv'): #check if the file is exist
    print('You Got it the file is exist')
    with open('product.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if 'PRODUCT,PRICE' in line:
                continue
        name, price = line.strip().split(',') #先把空格拿掉，再用取逗號換行
        product.append([name, price])   
    print(product)
else:
    price('There is not......')    

# Let user enter the data
while True:
    name = input('please enter the name of product: ')
    if name == 'q':
       break
    price = input('please enter the price of product: ')
    product.append([name, price])   
print(product)    

# List are products and price what they buy
for p in product:
    print(p[0], 'price is', p[1])

# Save to excel
with open('product.csv', 'w', encoding='utf-8') as f:
    f.write('PRODUCT,PRICE\n')
    for p in product:
        f.write(p[0] + ',' + str(p[1]) + '\n')
