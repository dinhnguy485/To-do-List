todo = []

if __name__ == '__main__':
    print("Welcome to Tri Nguyen's to-do list")
    while True:
        print("\n")
        print("1. Add a work")
        print("2. Mark as done")
        print("3. Delete a work")
        print("4. List task")
        print("5. Quit")

        choice = input("choose a task: ")

        if (choice == "1"):
            add = input("add a task: ")
            todo.append (add)
            print(add, "was added to the to do list")


        elif (choice =="2"):
            print(todo)
            done = int(input("Mark as done: "))
            if (todo):
                if(0<=done<(len(todo)+1)):
                    done = done - 1
                    todo[done] = todo[done] + " (done)"
                    print(todo)
                else:
                    print("task is not available")
            else:
                print("to-do list is empty")


        elif (choice == "3"):
            print(todo)
            delete = int(input("remove a task: "))
            if (todo):
                if (0 <= delete < (len(todo)+1)):
                    delete = delete - 1
                    del todo[delete]
                    print(todo)
                else:
                    print("please enter a valid number:")
            else:
                print("the todo list is empty")



        elif (choice == "4"):
            print (todo)

        elif(choice == "5"):
            exit()

        else:
            print("please enter a valid number")