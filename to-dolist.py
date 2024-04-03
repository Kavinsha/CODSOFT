def display_list():
    if len(todo_list)==0:
        print("Your to-do list is empty")
    else:
        print("Your to-do list:")
        for index, item in enumerate(todo_list,1):
            print(f"{index}.{item}")

def add_item(item):
    todo_list.append(item)
    print(f"Added: {item}")

def remove_item(index):
    if 1 <= index <= len(todo_list):
        item = todo_list.pop(index - 1)
        print(f"Removed: {item}")
    else:
        print("Invalid index")

todo_list = []
while True:
    print("\nOptions:")
    print("1.Show tasks")
    print("2.Add task")
    print("3.Remove task")
    print("4.Exit")
    choice = input("Enter the code of your choice: ")
    if choice == "1":
        display_list()
    elif choice == "2":
        item = input("Enter the item to add: ")
        add_item(item)
    elif choice == "3":
        index = int(input("Enter the number of the task to be removed: "))
        remove_item(index)
    elif choice == "4":
        print("Exiting")
        break
    else:
        print("Invalid choice")
