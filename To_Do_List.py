class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            old_task = self.tasks[index]["task"]
            self.tasks[index]["task"] = new_task
            print(f"Task '{old_task}' updated to '{new_task}'.")
        else:
            print("Invalid task number.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"Task '{self.tasks[index]['task']}' marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks.pop(index)
            print(f"Task '{task['task']}' deleted.")
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        
        for i, task in enumerate(self.tasks, 1):
            status = "Completed" if task["completed"] else "Incomplete"
            print(f"{i}. {task['task']} - {status}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add task")
        print("2. Update task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. View tasks")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                task = input("Enter the task: ")
                todo_list.add_task(task)
            elif choice == 2:
                index = int(input("Enter the task number to update: ")) - 1
                new_task = input("Enter the new task: ")
                todo_list.update_task(index, new_task)
            elif choice == 3:
                index = int(input("Enter the task number to complete: ")) - 1
                todo_list.complete_task(index)
            elif choice == 4:
                index = int(input("Enter the task number to delete: ")) - 1
                todo_list.delete_task(index)
            elif choice == 5:
                todo_list.view_tasks()
            elif choice == 6:
                print("Exiting the To-Do List application.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
