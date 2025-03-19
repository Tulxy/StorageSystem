
products = [

]


def print_products():
    for product in products:
        print(f"Název produktu: {product['name']}\n cena: {product['price']}$\n množství: {product['amount']}\n")
    if not products:
        print("Sklad je prázdný")


def add_product():
    product_name = input("Název produktu:")
    product_price = input("Název cenu:")
    product_amount = input("Název množství:")
    product = {
        'name': product_name,
        'price': product_price,
        'amount': product_amount
    }

    products.append(product)

def remove_product():
    for index, product in enumerate(products):
        print(f"{index + 1}. {product['name']} - {product['price']}$ - {product['amount']} ks")

    remove_choice = int(input("Zadej číslo produktu, který chceš smazat: ")) - 1

    if 0 <= remove_choice < len(products):
        products.pop(remove_choice)
    else:
        print("Neplatná volba")

def search_product():
    search = input("Zadej název produktu: ")
    found = False

    for product in products:
        if search.lower() in product['name'].lower():
            print(f"Název produktu: {product['name']}\n cena: {product['price']}$\n množství: {product['amount']}")
            found = True
    if not found:
        print("Produkt nebyl nalezen")


def total_price():
    total = sum([product['price'] for product in products])
    print(f"Celková cena: {total}$")


def max_price():
    maximum_price = max([product['price'] for product in products])
    for product in products:
        if product['price'] == maximum_price:
            print(f"Nejvyšší cena: {product['name']} - {product['price']}$")


def min_price():
    minimum_price = min([product['price'] for product in products])
    for product in products:
        if product['price'] == minimum_price:
            print(f"Nejnižší cena: {product['name']} - {product['price']}$")


def max_amount():
    maximum_amount = max([product['amount'] for product in products])
    for product in products:
        if product['amount'] == maximum_amount:
            print(f"Nejvyšší množství: {product['name']} - {product['amount']} ks")


def average_price():
    average = sum([product['price'] for product in products]) / len(products)
    print(f"Průměrná cena: {average}$")


def edit_product():
    for index, product in enumerate(products):
        print(f"{index + 1}. {product['name']} - {product['price']}$ - {product['amount']} ks")

    edit_choice = int(input("Zadej číslo produktu, který chceš upravit: ")) - 1

    if 0 <= edit_choice < len(products):
        new_name = input("Zadej nový název produktu: ")
        new_price = int(input("Zadej novou cenu produktu: "))
        new_amount = int(input("Zadej nové množství produktu: "))

        products[edit_choice]['name'] = new_name
        products[edit_choice]['price'] = new_price
        products[edit_choice]['amount'] = new_amount
    else:
        print("Neplatná volba")


def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("0. Výpis položek")
    print("1. Přidání položky")
    print("2. Celková cena")
    print("3. Celková cena")
    print("4. Nejvyšší cena")
    print("5. Nejnižší cena")
    print("6. Průměrná cena")
    print("7. Upravit položku")
    print("8. Hledání položky")
    print("9. Nejvyšší množství")

    choice = int(input("Volba: \n"))

    match choice:
        case 0:
            print("### Vypsání položek #### ")
            print_products()
            print("")
            menu()
        case 1:
            print("### Přidání položky ###")
            add_product()
            print("")
            menu()
        case 2:
            remove_product()
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
        case 9:
            print("### Nejvyšší množství ###")
            max_amount()
            print("")
            menu()
        case _:
            print("Neplatná volba")
            print("")
            menu()

menu()
