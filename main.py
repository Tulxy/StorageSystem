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
        print(f"Název produktu: {product['name']}, cena: {product['price']}$")


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


def max_price():
    maximum_price = max([product['price'] for product in products])
    print(f"Nejvyšší cena: {maximum_price}$")


def min_price():
    minimum_price = min([product['price'] for product in products])
    print(f"Nejnižší cena: {minimum_price}$")


def average_price():
    average = sum([product['price'] for product in products]) / len(products)
    print(f"Průměrná cena: {average}$")

def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis polože")
    print("2. Přidání položky")
    print("3. Celková cena")
    print("4. Nejvyšší cena")
    print("5. Nejnižší cena")
    print("6. Průměrná cena")

    choice = int(input("Volba: "))

    match choice:
        case 1:
            print("### Vypsání položek #### ")
            print_products()
        case 2:
            print("### Přidání položky ###")
            add_product()
        case 3:
            print("### Celková cena ###")
            total_price()
        case 4:
            print("### Nejvyšší cena ###")
            max_price()
        case 5:
            print("### Nejnižší cena ###")
            min_price()
        case 6:
            print("### Průměrná cena ###")
            average_price()
        case _:
            print("Neplatná volba")


menu()
