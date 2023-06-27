tasks = []

while True:
 print("\nTodo App")
 print("1. Add Task")
 print("2. View Task")
 print("3. Exit")
 choice = input("Choose an option: ")

 if choice == '1':
  task = input("Enter na task: ")
  tasks.append(task)
  print("Task added.")
 elif choice == '2':
  print("\nTasks:")
  for i, task in enumerate(tasks):
   print("Exiting...")
   break
 else:
  print("Invalid choice, try again.")