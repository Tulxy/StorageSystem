import tkinter as tk
from tkinter import simpledialog, messagebox

products = [

]


def gui_menu():
    def refresh_display():
        display.delete("1.0", tk.END)
        if not products:
            display.insert(tk.END, "Sklad je prázdný\n")
            return
        for product in products:
            display.insert(tk.END, f"Název: {product['name']}, Cena: {product['price']}$, Množství: {product['amount']}, {product['availability']}\n")

    def gui_add_product():
        name = simpledialog.askstring("Přidání produktu", "Název produktu:")
        if name is None:
            return
        try:
            price = int(simpledialog.askstring("Přidání produktu", "Cena produktu:"))
            amount = int(simpledialog.askstring("Přidání produktu", "Množství:"))
        except (ValueError, TypeError):
            messagebox.showerror("Chyba", "Cena a množství musí být čísla.")
            return
        availability = "Skladem" if amount > 0 else "Není skladem"
        products.append({'name': name, 'price': price, 'amount': amount, 'availability': availability})
        refresh_display()

    def gui_remove_product():
        if not products:
            messagebox.showinfo("Info", "Sklad je prázdný")
            return
        choices = "\n".join([f"{i+1}. {p['name']}" for i, p in enumerate(products)])
        choice = simpledialog.askinteger("Odstranit produkt", f"Zadej číslo produktu:\n{choices}")
        if choice and 1 <= choice <= len(products):
            products.pop(choice - 1)
            refresh_display()
        else:
            messagebox.showerror("Chyba", "Neplatná volba")

    def gui_search_product():
        search = simpledialog.askstring("Hledání", "Zadej název produktu:")
        if search is None:
            return
        found = False
        display.delete("1.0", tk.END)
        for product in products:
            if search.lower() in product['name'].lower():
                display.insert(tk.END, "Nalezené položky\n")
                display.insert(tk.END, f"Název: {product['name']}, Cena: {product['price']}$, Množství: {product['amount']}, {product['availability']}\n")
                found = True
        if not found:
            display.insert(tk.END, "Produkt nebyl nalezen\n")

    root = tk.Tk()
    root.title("Správa skladu")

    display = tk.Text(root, height=15, width=50)
    display.pack()

    btn_frame = tk.Frame(root)
    btn_frame.pack()

    tk.Button(btn_frame, text="Přidat produkt", command=gui_add_product).grid(row=0, column=0)
    tk.Button(btn_frame, text="Odebrat produkt", command=gui_remove_product).grid(row=0, column=1)
    tk.Button(btn_frame, text="Hledat produkt", command=gui_search_product).grid(row=0, column=2)
    tk.Button(btn_frame, text="Obnovit výpis", command=refresh_display).grid(row=0, column=3)

    refresh_display()
    root.mainloop()

gui_menu()
