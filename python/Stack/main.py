#THere is no need to have a seperate obj.py defining the structure as Lists in python already act like Stacks


my_list = []
while True:
 
    print(f"\nCURRENT LIST: {my_list}")
    
   
    print("-" * 30)
    print("1. Append (Add item to end)")
    print("2. Insert (Add item at specific index)")
    print("3. Remove (Delete specific item by name)")
    print("4. Pop    (Delete item at specific index)")
    print("5. Sort   (Order the list)")
    print("6. Reverse (Flip order)")
    print("7. Clear  (Delete everything)")
    print("8. Exit")
    print("-" * 30)
    
    choice = input("Enter your choice (1-8): ")
   
    if choice == '1': 
        val = input("Enter item to add: ")
        my_list.append(val)
        print(f"Added '{val}'.")
    elif choice == '2':
        try:
            idx = int(input("Enter index position: "))
            val = input("Enter item to add: ")
            my_list.insert(idx, val)
            print(f"Inserted '{val}' at index {idx}.")
        except ValueError:
            print("Error: Index must be a number.")
    elif choice == '3': 
        val = input("Enter item to remove: ")
        if val in my_list:
            my_list.remove(val)
            print(f"Removed '{val}'.")
        else:
            print(f"Error: '{val}' not found in list.")
    elif choice == '4': 
        try:
            idx_input = input("Enter index to pop (press Enter to pop last item): ")
            if idx_input == "":
                popped = my_list.pop() 
            else:
                popped = my_list.pop(int(idx_input))
            print(f"Popped item: '{popped}'")
        except IndexError:
            print("Error: Index out of range.")
        except ValueError:
            print("Error: Index must be a number.")
    elif choice == '5':
        
        try:
            my_list.sort() 
            print("List sorted.")
        except TypeError:
            print("Error: Cannot sort a list with mixed data types (e.g., numbers and strings).")
    elif choice == '6': 
        my_list.reverse()
        print("List reversed.")
    elif choice == '7': 
        confirm = input("Are you sure? (y/n): ")
        if confirm.lower() == 'y':
            my_list.clear()
            print("List cleared.")
    elif choice == '8': 
        print("Exiting program.")
        break 
    else:
        print("Invalid selection. Please choose 1-8.")

