import os

tasks = ["wash the dishes", "kick Teddy", "pet Teddy"]

def viewList():
    if len(tasks)==0:
        print("There are no tasks")
    else:
        for i in range(len (tasks)):
            print(str (i+1) + ": " + tasks[i])
os.system("cls")

def tasksZero():
    if len(tasks) == 0:
        os.system("cls")
        print("There are no tasks.")
        return True
    return False

def tasksOver():
    os.system("cls")
    print ("Not a valid index")

while True:
    print("Hello, welcome to Kian Wu's task list program")
    
    print()
    print("Here are your tasks: ")
    viewList()
    print()

    print("What would you like to do?")
    print("A: add a task")
    print("R: remove a task")
    print("E: edit a task")
    print("O: reorder a task")
    letter = input("Please select a letter: ").upper()
    letter = letter[0]
    print("")


    # if num == "1":
    #     # for i in range(len (tasks)):
    #     #     print(tasks[i])
    #     viewList()
    #     print("")
    if letter == "A":
        newTask = input("Add your new task: ")
        tasks.append(newTask)
        print("")
        viewList()
        print("")
    elif letter == "R":
        if tasksZero():
            print("")
            continue
        viewList()
        print("")
        taskRemove = input("Select which task you would like to remove by typing its number: ")
        taskRemove = int(taskRemove) -1 #Now we're back in programmer counting as an integer
        if taskRemove >= len(tasks) or taskRemove < 0:
            tasksOver()
            print()
            continue
        tasks.pop(taskRemove)
        print("")
    elif letter == "E":
        

        if tasksZero():
                continue
        taskEdit = input("Select which task you would like to edit by typing its number: ")
        if int(taskEdit) > len(tasks):
            tasksOver()
            continue
        
        taskEdit = int(taskEdit) -1
        changedTask = input("Now, write the revised task here: ")
        tasks[taskEdit] = changedTask
    elif letter == "O":
        indexToMove = input("Select which task you would like to move by typing its number: ")
        indexToMove = int(indexToMove) -1
        if tasksZero():
            continue
        if int(indexToMove) > len(tasks):
            tasksOver()
            continue
        indexToPlace = input("Where would you like to move the task to: ")
        indexToPlace = int(indexToPlace) -1
        if indexToPlace >= len(tasks) or indexToPlace < 0:
            tasksOver()
            continue
        int(indexToMove)
        if indexToPlace < indexToMove:
            tasks.insert(indexToPlace, tasks[indexToMove])
            tasks.pop(indexToMove +1)
        else:
            tasks.insert(indexToPlace +1, tasks[indexToMove])
            tasks.pop(indexToMove)
    os.system("cls")
    print("")


    #On lines 13-14 and 19-20 we have the same code. 
    # Take that code outt and turn it into a function 
    # tthat is called
    #Also, finsish the command to remove items

    #New HW
    #Add new command which allows you to edit a task's name

    #New, New HW 7-26-25
    #turn parameters into functions (if list is 0 elements or if index is out of bounds)