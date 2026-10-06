# Part B — Shopping List Manager

shopping_list = []

while True:
    choice = input("Choose: add / remove / show / done:")
    if choice == "add":
        item = input("Enter item: ")
        shopping_list.append(item)
        print("Item added. ")
    elif choice == "remove":
        item = input ("Enter item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print("Item remove.")
        else:
            print("That item is not on your list.")





