todo = ["Science", "Math", "History", "Com-sci"]


if __name__ == '__main__':
    print("Welcome to Tri Nguyen's to-do list")
    while True:
        print("\n")
        print("1. Add a task")
        print("2. Mark as done")
        print("3. Delete a work")
        print("4. List task")
        print("5. Quit")

        choice = input("choose a task: ")
        if (choice == "1"):
            print(*todo, sep=', ')
            add = int(input("add a description to task: "))


            if (0<=add<(len(todo)+1)):
                add = add-1
                description= input("Add task description: ")
                todo[add] = todo[add] + ": " + description
                print (*todo, sep = ', ')
            else:
                print("task is not available")


        elif (choice =="2"):
            print(*todo, sep = ', ')
            done = int(input("Mark as done: "))
            if (todo):
                if(0<=done<(len(todo)+1)):
                    done = done - 1
                    todo[done] = todo[done] + " (done)"
                    print(*todo, sep = ', ')
                else:
                    print("task is not available")
            else:
                print("to-do list is empty")


        elif (choice == "3"):
            print(*todo, sep = ', ')
            delete = int(input("remove a task: "))
            if (todo):
                if (0 <= delete < (len(todo)+1)):
                    delete = delete - 1
                    del todo[delete]
                    print(*todo, sep = ', ')
                else:
                    print("please enter a valid number:")
            else:
                print("the todo list is empty")

        elif (choice == "4"):
            print (*todo, sep = ', ')

        elif(choice == "5"):
            exit()

        else:
            print("please enter a valid number")