a = '4,018'
# a = "1.4 million"
# a = "20 million"
price = a.replace(',', '').split()
print(price)
try:
    if price[1] == 'million':
        price = float(price[0]) * 10 ** 6
    elif price[1] == 'priceillion':
        price = float(price[0]) * 10 ** 9
    elif price[1] == 'tillion':
        price = float(price[0]) * 10 ** 12
finally:
    price = int(price)

print(price)
