def on_sale(price):
    """Returns discounted price based on original price"""
    if price >= 300:
        discount = price * 0.3
    elif 200 <= price < 300:
        discount = price * 0.2
    elif 100 <= price < 200:
        discount = price * 0.1
    elif 0 < price < 100:
        discount = price * 0.05
    elif price < 0:
        discount = 0
    price -= discount
    return price

price = int(input("Price: "))
result = on_sale(price)
print(f"${result:.2f}")
