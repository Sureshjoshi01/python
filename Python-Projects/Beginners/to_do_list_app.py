# Write a program to create a simple To-Do List application. The program allows
# users to add tasks, view the current list of tasks, and remove tasks once they are
# completed.


# Optional Enhancements
# • Add an option in the menu that allows users to mark tasks as completed
# instead of removing them. Completed tasks can be displayed separately or
# removed from the list.
# • Implement functionality that saves the list to a file and loads it when the
# program starts. This way, users can maintain their to-do list across different
# sessions.
# •Allow users to categorize tasks (e.g., Work, Personal) and filter the list based
# on these categories. This adds an organizational element to the to-do list.

def todo_list_menu():
    print("Todo List Menu:")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def view_task(tasks):
    for i in range(len(tasks)): 
        print(f"{i+1}. {tasks[i]}")

def add_task(tasks):
    print("Enter a new task : ",end="")
    new_task = input()
    if new_task in tasks:
        print("Task already exists in the Todo List")
    elif new_task.strip() == "":
        print("Task cannot be empty")
    elif new_task.strip() != "":
        tasks.append(new_task)
        save_tasks(tasks)

def completed_tasks(tasks):
    print("Enter task number to mark as completed: ", end="")
    completed_task = int(input())
    if 1 <= completed_task <= len(tasks):
        tasks[completed_task - 1] = f"{tasks[completed_task - 1]} (Completed)"
        print("Task marked as completed")
        save_tasks(tasks)
    else:
        print("Task not found.")

def task_to_remove(tasks):
    print("Enter task number to be deleted : ",end="")
    rmv_task = int(input())
    if 1 <= rmv_task <= len(tasks):
        tasks.pop(rmv_task - 1)
        print("Task removed successfully")
        save_tasks(tasks)
    else:
        print("Task not found.")

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")



def load_tasks(filename="tasks.txt"):
    tasks = []
    try:
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        pass
    return tasks

def main():
    tasks = load_tasks()
    todo_list_menu()
    while True:

        print("Enter your choice: ", end="")
        try:
            choice = int(input())
        except ValueError:
            print("Please enter numbers only.")
            continue
        if choice not in [1,2,3,4,5]:
            print("Invalid Selection, Please select from below options ")
            todo_list_menu()
        elif choice == 1:
            if len(tasks) == 0:
                print("No Tasks in the Todo List")
            else:
                view_task(tasks)
                todo_list_menu()
        elif choice == 2:
            add_task(tasks)
            todo_list_menu()
        elif choice == 3:
            task_to_remove(tasks) 
            todo_list_menu()        
        elif choice == 4:
            completed_tasks(tasks)
            todo_list_menu()
        elif choice == 5:
            save_tasks(tasks)
            print("GoodBye")
            break
            
main()
       
