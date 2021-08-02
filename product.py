import os

# Read the file
def read_file(filename):
    product = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if 'PRODUCT,PRICE' in line:
                continue
            name, price = line.strip().split(',') #先把空格拿掉，再用取逗號換行
            product.append([name, price])   
        return product

# Let user enter the data
def user_enter(product):
    while True:
        name = input('please enter the name of product: ')
        if name == 'q':
           break
        price = input('please enter the price of product: ')
        product.append([name, price])   
    print(product)    
    return product

# List are products and price what they buy
def print_P(product):
    for p in product:
        print(p[0], 'price is', p[1])

# Save to excel
def save_file(filename, product):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('PRODUCT,PRICE\n')
        for p in product:
            f.write(p[0] + ',' + str(p[1]) + '\n')


def main():
    filename = 'product.csv'
    if os.path.isfile(filename): #check if the file is exist
        print('You Got it the file is exist')
        product = read_file(filename)
    else:    
        print('There is not......')    

    product = user_enter(product)
    print_P(product)
    save_file('product.csv', product)

main()