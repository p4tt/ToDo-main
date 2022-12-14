HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать задачи на определенную дату.
showall - напечатать все добавленные задачи.
exit - завершить работу.
random - добавить случайную задачу на сегодня"""


random_task = "random"
tasks = {}

run = True

while run:
    command = input("Bведите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Bведите дату для отображения: ")
        if date in tasks:
            for task in tasks[date]:
                print("Задача - ", task)
        else:
          print("Нет задач на эту дату.")

    elif command == "showall":
        for key,value in tasks.items():
          print("Дата: ",key,"Задача: ",value)
          
    elif command == "add":
        date = input("Введите дату: ")
        task = input("Введите название задачи: ")
        if date in tasks:
            tasks[date].append(task)
        else:
            tasks[date] = []
            tasks[date] = [task]
        print("Задача", task, "добавлена на дату", date)
    elif command=="random":
        if "Сегодня" in tasks:
            tasks["Сегодня"].append(random_task)
        else:
            tasks["Сегодня"] = []
            tasks["Сегодня"].append(random_task)
            print("Добавлена случайная задача на сегодняшний день.")
    elif command == "exit":
        print("Shutdown.")
        break
    else:
        print("Неизвестная команда, для справки напишите help")