products = [

]


def print_products():
    for product in products:
        print(f"Název produktu: {product['name']}\n cena: {product['price']}$\n množství: {product['amount']}\n {product['availability']}")
    if not products:
        print("Sklad je prázdný")


def add_product():
    product_name = input("Název produktu:")
    try:
        product_price = int(input("Cena produktu:"))
    except ValueError:
        product_price = 0

    try:
        product_amount = int(input("Množství:"))
    except ValueError:
        product_amount = 0

    product_availability = ""
    product = {
        'name': product_name,
        'price': product_price,
        'amount': product_amount,
        'availability': product_availability
    }

    if product_amount == 0:
        product['availability'] = "Není skladem"
    else:
        product['availability'] = "Skladem"

    products.append(product)


def remove_product():
    remove_all = int(input("Chcete odstranit všechny produkty? 1 - ano, 2 - ne: "))
    if remove_all == 1:
        products.clear()
        print_products()
        return
    else:
        for index, product in enumerate(products):
            print(f"{index + 1}. {product['name']} - {product['price']}$ - {product['amount']} ks")

        remove_choice = int(input("Zadej číslo produktu, který chceš smazat: ")) - 1

        if 0 <= remove_choice < len(products):
            products.pop(remove_choice)
        else:
            print("Neplatná volba")


def search_product():
    available = input("Chceš zobrazit pouze produkty, které jsou skladem? 1 - ano, 2 - ne: ")
    search = input("Zadej název produktu: ")
    found = False

    for product in products:
        name_match = search.lower() in product['name'].lower()
        in_stock = product['availability'] == "Skladem"

        if available == "1":
            if name_match and in_stock:
                print(f"Název produktu: {product['name']}\n cena: {product['price']}$\n množství: {product['amount']}")
                found = True
        else:
            if name_match:
                print(
                    f"Název produktu: {product['name']}\n cena: {product['price']}$\n množství: {product['amount']}\n {product['availability']}")
                found = True

    if not found:
        print("Produkt nebyl nalezen")


def total_price():
    if not products:
        print("Sklad je prázdný")
        return

    total = sum([product['price'] * product['amount'] for product in products])
    print(f"Celková cena: {total}$")


def max_price():
    if not products:
        print("Sklad je prázdný")
        return

    maximum_price = max([product['price'] for product in products])
    for product in products:
        if product['price'] == maximum_price:
            print(f"Nejvyšší cena: {product['name']} - {product['price']}$")


def min_price():
    if not products:
        print("Sklad je prázdný")
        return

    minimum_price = min([product['price'] for product in products])
    for product in products:
        if product['price'] == minimum_price:
            print(f"Nejnižší cena: {product['name']} - {product['price']}$")


def max_amount():
    if not products:
        print("Sklad je prázdný")
        return

    maximum_amount = max([product['amount'] for product in products])
    for product in products:
        if product['amount'] == maximum_amount:
            print(f"Nejvyšší množství: {product['name']} - {product['amount']} ks")


def average_price():
    if not products:
        print("Sklad je prázdný")
        return
    average = sum([product['price'] for product in products]) / len(products)
    print(f"Průměrná cena: {average}$")


def edit_product():
    for index, product in enumerate(products):
        print(f"{index + 1}. {product['name']} - {product['price']}$ - {product['amount']} ks")

    edit_choice = int(input("Zadej číslo produktu, který chceš upravit: ")) - 1

    if 0 <= edit_choice < len(products):
        new_name = input("Zadej nový název produktu: ")
        try:
            new_price = int(input("Zadej novou cenu produktu: "))
        except ValueError:
            new_price = 0

        try:
            new_amount = int(input("Zadej nové množství produktu: "))
        except ValueError:
            new_amount = 0

        products[edit_choice]['name'] = new_name
        products[edit_choice]['price'] = new_price
        products[edit_choice]['amount'] = new_amount
        if new_amount == 0:
            products[edit_choice]['availability'] = "Není skladem"
        else:
            products[edit_choice]['availability'] = "Skladem"
    else:
        print("Neplatná volba")


def menu():
    while True:
        print("Vítej ve skladu")
        print("###############\n")
        print("0. Výpis položek")
        print("1. Přidání položky")
        print("2. Odstranění položky")
        print("3. Celková cena")
        print("4. Nejvyšší cena")
        print("5. Nejnižší cena")
        print("6. Průměrná cena")
        print("7. Upravit položku")
        print("8. Hledání položky")
        print("9. Nejvyšší množství")
        print("10. Konec")

        try:
            choice = int(input("Volba: \n"))
        except ValueError:
            print("Neplatná volba")
            continue

        match choice:
            case 0:
                print("### Vypsání položek #### ")
                print_products()
                print("")
            case 1:
                print("### Přidání položky ###")
                add_product()
                print("")
            case 2:
                remove_product()
                print("")
            case 3:
                print("### Celková cena ###")
                total_price()
                print("")
            case 4:
                print("### Nejvyšší cena ###")
                max_price()
                print("")
            case 5:
                print("### Nejnižší cena ###")
                min_price()
                print("")
            case 6:
                print("### Průměrná cena ###")
                average_price()
                print("")
            case 7:
                print("### Upravit položku ###")
                edit_product()
                print("")
            case 8:
                print("### Hledání položky ###")
                search_product()
                print("")
            case 9:
                print("### Nejvyšší množství ###")
                max_amount()
                print("")
            case 10:
                print("Ukončuji program.")
                break
            case _:
                print("Neplatná volba")
                print("")


if __name__ == "__main__":
    menu()
