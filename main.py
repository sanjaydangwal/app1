# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")
while True:
    user_action = input("Type add, show, edit, complete and exit : ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos("todos.txt")

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}--{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            index = int(user_action[5:]) - 1
            new_todo = input("Enter new todo : ")

            todos = functions.get_todos()

            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            index = int(user_action[9:]) - 1
            todos = functions.get_todos()
            removed_todo = todos.pop(index)
            functions.write_todos(todos)
            print(f"Todo '{removed_todo.strip('\n')}' has been removed.")
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print('Bye.')
