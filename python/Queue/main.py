queue = []
while True:
    
    if not queue:
        print("\n[  (Empty)  ]")
    else:
        
        print(f"\nFRONT -> {queue} <- REAR")
    print("-" * 35)
    print("1. Enqueue (Add to Rear)")
    print("2. Dequeue (Remove from Front)")
    print("3. Peek    (See who is next)")
    print("4. Size    (Count elements)")
    print("5. Exit")
    print("-" * 35)
    choice = input("Enter choice: ")
    if choice == '1': 
        val = input("Enter item to add: ")
        
        queue.append(val)
        print(f"Enqueued '{val}'.")
    elif choice == '2':
        if len(queue) > 0:
            
            removed = queue.pop(0)
            print(f"Dequeued '{removed}'.")
        else:
            print("Error: Queue Underflow (The queue is empty).")
    elif choice == '3':
        if len(queue) > 0:
            
            print(f"Next in line: '{queue[0]}'")
        else:
            print("The queue is empty.")
            
        print(f"Queue size: {len(queue)}")
    elif choice == '5': 
        print("Exiting.")
        break
    else:
        print("Invalid choice.")

