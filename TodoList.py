todo = ["Science", "Math", "History", "Com-sci"]


def listtask():
    for i, task in enumerate(todo):
        print(f"Task #{i + 1}: {task}")


if __name__ == '__main__':
    print("Welcome to Tri Nguyen's to-do list")
    while True:
        print("\n")
        print("1. Add a task")
        print("2. Mark as done")
        print("3. Delete a task")
        print("4. Add a Deadline")
        print("5. Quit")

        choice = input("Choose a task: ")
        if choice == "1":
            listtask()
            add = int(input("Add a task: "))

            if 0 <= add < len(todo):
                description = input("Add task description: ")
                todo[add] += f": {description}"
                print(*todo, sep=', ')
            else:
                print("Task is not available")

        elif choice == "2":
            print(*todo, sep=', ')
            done = int(input("Mark as done: "))
            if 0 <= done < len(todo):
                todo[done] += " (done)"
                print(*todo, sep=', ')
            else:
                print("Task is not available")

        elif choice == "3":
            print(*todo, sep=', ')
            delete = int(input("Remove a task: "))
            if 0 <= delete < len(todo):
                del todo[delete]
                print(*todo, sep=', ')
            else:
                print("Please enter a valid number")

        elif choice == "4":
            print(*todo, sep=', ')
            time = int(input("Add a deadline to which task? "))
            if 0 <= time < len(todo):
                deadline = input("Add a deadline: ")
                todo[time] += f" (Deadline: {deadline})"
                print(*todo, sep=', ')
            else:
                print("Task is not available")

        elif choice == "5":
            exit()

        else:
            print("Please enter a valid number")
