laptops = [
    ['Apple', '1234$', '2567$', '2144$', '2567$'],
    ['Lg', '324$', '476$', '523$', '7657$'],
    ['Hp', '254$', '367$', '567$', '890$'],
    ['Honor', '299$', '345$', '587$', '6237$']
]


def show_price(laptops_price):
    print(laptops_price[0], laptops_price[1:])


for price in laptops:
    show_price(price)
