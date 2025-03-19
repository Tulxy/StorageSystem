from pyautogui import doubleClick

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


def search_product():
    search = input("Zadej název produktu: ")
    found = False

    for product in products:
        if search.lower() in product['name'].lower():
            print(f"Název produktu: {product['name']}, cena: {product['price']}$")
            found = True
    if not found:
        print("Produkt nebyl nalezen")


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


def edit_product():
    for index, product in enumerate(products):
        print(f"{index + 1}. {product['name']} - {product['price']}$")

    edit_choice = int(input("Zadej číslo produktu, který chceš upravit: ")) - 1

    if 0 <= edit_choice < len(products):
        new_name = input("Zadej nový název produktu: ")
        new_price = int(input("Zadej novou cenu produktu: "))

        products[edit_choice]['name'] = new_name
        products[edit_choice]['price'] = new_price
    else:
        print("Neplatná volba")


def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis položek")
    print("2. Přidání položky")
    print("3. Celková cena")
    print("4. Nejvyšší cena")
    print("5. Nejnižší cena")
    print("6. Průměrná cena")
    print("7. Upravit položku")
    print("8. Hledání položky")

    choice = int(input("Volba: \n"))

    match choice:
        case 1:
            print("### Vypsání položek #### ")
            print_products()
            print("")
            menu()
        case 2:
            print("### Přidání položky ###")
            add_product()
            print("")
            menu()
        case 3:
            print("### Celková cena ###")
            total_price()
            print("")
            menu()
        case 4:
            print("### Nejvyšší cena ###")
            max_price()
            print("")
            menu()
        case 5:
            print("### Nejnižší cena ###")
            min_price()
            print("")
            menu()
        case 6:
            print("### Průměrná cena ###")
            average_price()
            print("")
            menu()
        case 7:
            print("### Upravit položku ###")
            edit_product()
            print("")
            menu()
        case 8:
            print("### Hledání položky ###")
            search_product()
            print("")
            menu()
        case _:
            print("Neplatná volba")
            print("")
            menu()

menu()
