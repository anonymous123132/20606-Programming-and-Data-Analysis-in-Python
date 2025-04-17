def full_inventory(inventory):
    st = ""
    for book in inventory:
        st += "Title: " + book[0] + ", Author: " + book[1] + ", Price: " + str(book[2]) +", Quantity: " + str(book[3]) + "\n"
    return st

def total_inventory_value(inventory):
    total = 0
    for book in inventory:
        total += book[2] * book[3]
    return total

def filter_books_by_price(inventory, price):
    res = []
    for book in inventory:
        if book[2] < price:
            res.append(book)
    return res

def check_availability(inventory, book_name):
    for book in inventory:
        if book[0] == book_name and book[3] > 0:
            return True
    return False