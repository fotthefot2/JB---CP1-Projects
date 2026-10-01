# Judah Beagley, period 1, shopping list manager
instructions = print("this is a shopping list. you can add any items here out of the list provided")
shopping_list = []
while True:
    
    user_output = input("HERE ARE ALL COMMANDS: viewlist, additem, removeitem, checkout. ENTER YOUR COMMAND: ")
    if user_output == "viewlist":
        print(*shopping_list)
    elif user_output == "additem":
        item = input("what item: ")
        shopping_list.append(item)
        print(f"added {item}")
    elif user_output == "removeitem":
        remove = input("what do you want to remove: ")
        if remove in shopping_list:
            shopping_list.remove(remove)
        else:
            print("ITEM NOT IN LIST")
    elif user_output == "checkout":
        print("here is your shopping list:") 
        print(*shopping_list)
        break
    else:
        print("INVALID")