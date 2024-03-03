todo = ["Science", "Math", "History", "Com-sci"]


def listtask():
    print("\n")
    print("-----------------------------")
    for i, task in enumerate(todo):
        print(f"Task #{i + 1}: {task}")


if __name__ == '__main__':
    print("Welcome to Tri Nguyen's to-do list")
    while True:
        print("\n")
        print("-----------------------------")
        print("1. Add a task")
        print("2. Mark as done")
        print("3. Delete a task")
        print("4. Quit")

        choice = input("Choose a task: ")
        if choice == "1":
            listtask()
            add = int(input("Add a task: "))

            if 0 <= add < (len(todo)+1):
                add = add -1
                description = input("Add task description: ")
                deadline = input("Add a deadline: ")
                todo[add] += f": {description}"
                todo[add] += f" (Deadline: {deadline})"
                listtask()
            else:
                print("Task is not available")

        elif choice == "2":
            listtask()
            done = int(input("Mark as done: "))
            if (0 <= done < (len(todo)+1)):
                done = done -1
                todo[done] += " (done)"
                listtask()
            else:
                print("Task is not available")

        elif choice == "3":
            listtask()
            delete = int(input("Remove a task: "))
            if 0 <= delete < (len(todo)+1):
                delete = delete -1
                del todo[delete]
                listtask()
            else:
                print("Please enter a valid number")



        elif choice == "4":
            exit()

        else:
            print("Please enter a valid number")
