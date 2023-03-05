print("WELCOME to ToDo App!")

to_do_list = []
tasks_done = []
keep_going = True


def print_to_do_list():
    for index in range(0, len(to_do_list)):
        print(f"{index + 1}. {to_do_list[index]}")


def print_tasks_done():
    for task_done in tasks_done:
        print(f"*  {task_done}")


while keep_going:
    print("Add your ToDo task\nOR press a number of existing task to mark it complete\n"
          "or press 'q' to Quit!")
    print("-" * 50)

    print_to_do_list()

    print("-" * 50)

    action = input(">>>   ")

    if action.isnumeric():
        if len(to_do_list) > 0 and 0 <= (int(action)-1) < len(to_do_list):
            tasks_done.append(to_do_list.pop(int(action)-1))
        else:
            print("There is no such task number! Enter again!")
    elif action == "q" or action == "Q":
        print("Goodbye!")
        print("So far You have completed the following tasks:")
        print_tasks_done()
        break
    else:
        to_do_list.append(action)

