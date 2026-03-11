import sys


def main() -> None:

    print("=== Inventory System Analysis ===")

    inventory = dict()

    for arg in sys.argv[1:]:
        try:
            name, qty = arg.split(":")
            inventory.update({name: int(qty)})
        except ValueError:
            continue

    total_items = 0
    for v in inventory.values():
        total_items += v

    print("Total items in inventory:", total_items)
    print("Unique item types:", len(inventory))

    print("\n=== Current Inventory ===")

    temp = dict()
    temp.update(inventory)
    count = 0
    while count < len(inventory):
        max_item = None
        max_qty = -1
        for item, qty in temp.items():
            if qty > max_qty:
                max_qty = qty
                max_item = item
        percent = (max_qty / total_items) * 100
        if max_qty == 1:
            print(f"{max_item}: {max_qty} unit ({percent:.1f}%)")
        else:
            print(f"{max_item}: {max_qty} units ({percent:.1f}%)")
        temp.update({max_item: -1})
        count += 1

    most_item = None
    most_qty = -1

    least_item = None
    least_qty = None

    for item, qty in inventory.items():

        if qty > most_qty:
            most_qty = qty
            most_item = item

        if least_qty is None or qty < least_qty:
            least_qty = qty
            least_item = item

    print("\n=== Inventory Statistics ===")
    if most_qty == 1:
        print("Most abundant:", most_item, "(" + str(most_qty) + " unit)")
    else:
        print("Most abundant:", most_item, "(" + str(most_qty) + " units)")

    if least_qty == 1:
        print("Least abundant:", least_item, "(" + str(least_qty) + " unit)")
    else:
        print("Least abundant:", least_item, "(" + str(least_qty) + " units)")

    moderate = dict()
    scarce = dict()

    for item, qty in inventory.items():

        if qty >= 4:
            moderate.update({item: qty})
        else:
            scarce.update({item: qty})

    print("\n=== Item Categories ===")
    print("Moderate:", moderate)
    print("Scarce:", scarce)

    print("\n=== Management Suggestions ===")

    restock = ""

    for item, qty in inventory.items():
        if qty <= 1:
            if restock == "":
                restock = item
            else:
                restock = restock + ", " + item

    if restock != "":
        print("Restock needed:", restock)

    print("\n=== Dictionary Properties Demo ===")

    keys_str = ""
    for k in inventory.keys():
        if keys_str == "":
            keys_str = k
        else:
            keys_str = keys_str + ", " + k

    print("Dictionary keys:", keys_str)

    values_str = ""
    for v in inventory.values():
        if values_str == "":
            values_str = str(v)
        else:
            values_str = values_str + ", " + str(v)

    print("Dictionary values:", values_str)
    print("Sample lookup - 'sword' in inventory:", "sword" in inventory)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
