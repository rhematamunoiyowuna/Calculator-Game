print("Let's Make your Shopping List\n")

shopping_list = [] 

while True:
    item = input("Enter an item (or type 'done' to finish): ")

    if item.lower() == "done":
        print("\nYour shopping list is ready!")
        print("Items in your list:")
        for i, list_item in enumerate(shopping_list, start=1):
            print(f"{i}. {list_item}")
        print(f"\nTotal items: {len(shopping_list)}")
        break
    else:
        shopping_list.append(item)
        print("Item added. Add more or type 'done' to finish.\n")
