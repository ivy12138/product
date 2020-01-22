product=[]
while True:
    name=input('enter the name:')
    if name=='q':
        break
    p=[]
    price=input('enter the price:')
    p.append(name)
    p.append(price)
    product.append(p)
print(product)
