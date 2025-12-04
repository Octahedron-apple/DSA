def print_dict(d):
    """Prints the dictionary in a formatted way."""
    print("\n--- Current Dictionary State ---")
    if not d:
        print("(Empty)")
    else:
        print("{")
        for k, v in d.items():
            type_name = type(v).__name__
            print(f"  '{k}': {v} ({type_name})")
        print("}")
    print("--------------------------------\n")



my_dict = {

}
while True:
    print_dict(my_dict)
    print("Select an operation:")
    print("1. Add or Update a Key-Value pair")
    print("2. Delete a Key")
    print("3. Check if a Key exists")
    print("4. Get a Value by Key")
    print("5. List all Keys")
    print("6. List all Values")
    print("7. Clear Dictionary")
    print("8. Exit")
    choice = input("\nEnter choice (1-8): ").strip()
    if choice == '1':
        key = input("Enter Key: ").strip()
        val_input = input("Enter Value: ").strip()
        
       
        if key in my_dict:
            print(f"Updated '{key}' from {my_dict[key]} to {val_input}.")
        else:
            print(f"Added new item: '{key}': {val_input}")
        
        my_dict[key] = val_input
    elif choice == '2':
        key = input("Enter Key to delete: ").strip()
        result = my_dict.pop(key, None)
        
        if result is not None:
            print(f"Successfully deleted key '{key}' (Value was: {result})")
        else:
            print(f"Error: Key '{key}' not found.")
    elif choice == '3':
        key = input("Enter Key to check: ").strip()
        if key in my_dict:
            print(f"Yes, '{key}' exists in the dictionary.")
        else:
            print(f"No, '{key}' is NOT in the dictionary.")
    elif choice == '4':
        key = input("Enter Key to retrieve: ").strip()
        
        val = my_dict.get(key)
        if val is not None:
            print(f"The value for '{key}' is: {val}")
        else:
            print(f"Key '{key}' not found.")
    elif choice == '5':
        print("Keys:", list(my_dict.keys()))
    elif choice == '6':
        print("Values:", list(my_dict.values()))
    elif choice == '7':
        confirm = input("Are you sure you want to delete everything? (y/n): ").lower()
        if confirm == 'y':
            my_dict.clear()
            print("Dictionary cleared.")
        else:
            print("Operation cancelled.")
    elif choice == '8':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid selection. Please try again.")
    input("\nPress Enter to continue...")
    print("\n" * 5) 
