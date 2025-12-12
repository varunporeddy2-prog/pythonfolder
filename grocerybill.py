items = {}
while True:
    name = input("Item name (or 'done'): ")
    if name == "done":
        break
    price = float(input("Price: "))
    items[name] = price

total = sum(items.values())
print("Total bill:", total)
