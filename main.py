products = [
    {
        "name": "Audi",
        "price": 50
    },
    {
        "price": 30,
        "name": "BMW",
    }
]


def print_products():
    for product in products:
        print(f"Název produktu2: {product['name']}, cena: {product['price']}$")


def add_product():
    product_name = input("Název produktu:")
    product_price = input("Název cenu:")
    product2 = {
        'name': product_name,
        'price': product_price
    }

    products.append(product2)


def total_price():
    total = sum([product['price'] for product in products])
    print(f"Celková cena: {total}$")


def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis polože")
    print("2. Přidání položky")
    print("3. Celková cena")

    choice = int(input("Volba: "))

    match choice:
        case 1:
            print_products()
        case 2:
            add_product()
        case 3:
            total_price()
        case _:
            print("Neplatná volba")


menu()
