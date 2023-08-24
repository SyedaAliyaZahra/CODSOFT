class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
        else:
            print("Invalid index")

    def show_tasks(self):
        print("To-Do List:")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Show Tasks")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
            print("Task added successfully.")

        elif choice == '2':
            index = int(input("Enter task index to update: ")) - 1
            new_task = input("Enter new task: ")
            todo_list.update_task(index, new_task)
            print("Task updated successfully.")

        elif choice == '3':
            todo_list.show_tasks()

        elif choice == '4':
            print("Exiting....\n Thank you!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
