


task_lists = []

print("===== TASK MANAGER =====")


print()

print("1. Add task")
print("2. View task")
print("3. Complete Task")
print("4. Delete Task")
print("5. Quit")

print()

userChoice = int(input("Choose an output:"))


print("User picked: " + str(userChoice))

if (userChoice == 1):
    task_lists.append(input("Enter task:"))
    
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

