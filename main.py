
#New line code October 8th.

task_list = []



#Initial task manager showing


print()

loop = True

while loop == True:
        
    print("===== TASK MANAGER =====")


    print()

    print("1. Add task")
    print("2. View task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Quit")
    userChoice = input("Choose an output:")

    try:
        userChoice = int(userChoice)
    except ValueError:
        print("Invalid output! (Must be 1-5)")

    print("User picked: " + str(userChoice))
    print()

    if (userChoice == 1):
        task_list.append({"taskName": input("Enter task:"), "completed": False})
    elif(userChoice == 2):
        print("Your Tasks:")
        for x in range(len(task_list)):
            print(str(x + 1) + ": " + task_list[x]["taskName"] + "| Completed: " + str(task_list[x]["completed"]))

    elif(userChoice == 3):
        for x in range(len(task_list)):
            print(str(x + 1) + ": " + task_list[x]["taskName"] + "| Completed: " + str(task_list[x]["completed"]))
        userChoice = int(input("Choose task to complete(" + str(len(task_list)) + " tasks available):" ))
        
        task_list[userChoice - 1]["completed"] = True

    elif(userChoice == 4):
        for x in range(len(task_list)):
            print(str(x + 1) + ": " + task_list[x]["taskName"] + "| Completed: " + str(task_list[x]["completed"]))
        userChoice = int(input("Choose task to remove(" + str(len(task_list)) + " tasks available):" ))

        task_list.pop(userChoice - 1)

    elif(userChoice == 5):
        print("Thank you!")
        break



            
#elif(userChoice == 2):
#    print()
#elif(userChoice == 3):
#    print
#elif(userChoice == 4):
#   print
#elif(userChoice == 5):
#    print
#else
#    break;

