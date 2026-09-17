from datetime import datetime
import json
import os

file_name = "tasks.json"

choices = {
    "1": "Записать новую задачу",
    "2": "Вывести список задач",
    "3": "Удалить задачу из списка",
    "0": "Выйти из программы",
}

def load_tasks():
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        return []
    with open(file_name, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)
while True:
    tasks_list = load_tasks()

    print("\n--- ГЛАВНОЕ МЕНЮ ---")
    for key, value in choices.items():
        print(f"[{key}] - {value}")

    user_choice = input("\nВыберите действие: ").strip()
    print("\033[1A\033[2K", end="")
    
    if user_choice == "1":
        print("\n--- ДОБАВЛЕНИЕ ЗАДАЧИ ---")
        task_text = input("Введите свою задачу: ")

        next_task_number = len(tasks_list) + 1
        creation_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        new_task = {
            "number": next_task_number,
            "text": task_text,
            "date": creation_time,
        }

        tasks_list.append(new_task)
        save_tasks(tasks_list)
        print(f"Успешно добавлено! Задача №{next_task_number}")
    elif user_choice == "2":
        print("\n--- СПИСОК ЗАДАЧ ---")
        if not tasks_list:
            print("Список задач пуст.")
        else:
            for task in tasks_list:
                print(f"{task['number']}. {task['text']} [Создана: {task['date']}]")
    elif user_choice == "3":
        print("\n--- УДАЛЕНИЕ ЗАДАЧИ ---")
        if not tasks_list:
            print("Что мне удалять то, список задач пуст.")
        else:
            for task in tasks_list:
                print(f"{task['number']}. {task['text']}")
            try:
                to_delete = int(input("\nВведите номер задачи для удаления: "))

                task_to_remove = next((t for t in tasks_list if t["number"] == to_delete), None)

                if task_to_remove:
                    tasks_list.remove(task_to_remove)

                    for index, task in enumerate(tasks_list, start=1):
                        task["number"] = index

                    save_tasks(tasks_list)
                    print(f"Задача №{to_delete} успешно удалена!")
                else:
                    print("Задачи с таким номером не существует.")
            except ValueError:
                print("Ошибка, нужно ввести нормальное число.")
    elif user_choice == "0":
        print("\nПрограмма завершена. Пока!")
        break
    else:
        print("\nНеверный ввод. Пожалуйста, выберите пункт из меню.")