tasks = []

while True:
    print("\n----- TODO LIST MANAGER -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Add Task
    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    # View Tasks
    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks available!")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    # Remove Task
    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks to remove!")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            
            num = int(input("Enter task number to remove: "))
            
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)
                print(f"Task '{removed}' removed successfully!")
            else:
                print("Invalid task number!")

    # Exit
    elif choice == '4':
        print("Exiting Todo List Manager...")
        break

    else:
        print("Invalid choice! Please try again.")