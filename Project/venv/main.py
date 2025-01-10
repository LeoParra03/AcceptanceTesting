from todo_list import ToDoList

def main():
    todo_list = ToDoList()

    while True:
        print("To-Do List Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Clear All Tasks")
        print("5. Edit Task")
        print("6. Filter Tasks by Status")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            priority = input("Enter priority: ")
            todo_list.add_task(title, description, due_date, priority)

        elif choice == '2':
            tasks = todo_list.list_tasks()
            for task in tasks:
                print(task)

        elif choice == '3':
            title = input("Enter task title to mark as completed: ")
            todo_list.mark_task_as_completed(title)

        elif choice == '4':
            todo_list.clear_tasks()
            print("To-Do List cleared!")

        elif choice == '5':
            title = input("Enter task title to edit: ")
            new_title = input("Enter new title: ")
            new_description = input("Enter new description: ")
            new_due_date = input("Enter new due date: ")
            new_priority = input("Enter new priority: ")
            todo_list.edit_task(title, new_title, new_description, new_due_date, new_priority)

        elif choice == '6':
            status = input("Enter status to filter by (Pending/Completed): ")
            tasks = todo_list.filter_tasks_by_status(status)
            for task in tasks:
                print(task)

        elif choice == '7':
            break

        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()
