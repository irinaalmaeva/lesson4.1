# Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи,
# срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач
# и вывода списка текущих (не выполненных) задач


class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_as_done(self, task_index):
        if task_index < len(self.tasks):
            self.tasks[task_index].status = True

    def display_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.status]
        if current_tasks:
            for index, task in enumerate(current_tasks):
                print(f"Task {index + 1}: {task.description} | Срок выполнения: {task.deadline}")
        else:
            print("Нет текущих задач.")

    def get_task_status(self, task_index):
        if task_index < len(self.tasks):
            return self.tasks[task_index].status
        else:
            return None


task1 = Task("Выполнить домашнее задание", "2024-06-05")
task2 = Task("Убраться в комнате", "2024-06-07")
task3 = Task("Лечь спать во время", "2024-06-07")

task_manager = TaskManager()
task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)

print("Текущие задачи:")
task_manager.display_current_tasks()

task_manager.mark_task_as_done(0)

print("Эти задачи предстоит еще выполнить:")
task_manager.display_current_tasks()

print("Статус задач после выполнения:")

for i in range(len(task_manager.tasks)):
    print(f"Task {i + 1}: Выполнена" if task_manager.get_task_status(i) else f"Task {i + 1}: Не выполнена")