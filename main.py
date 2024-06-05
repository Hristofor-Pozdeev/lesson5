class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = "не выполнено"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        new_task = Task(description, deadline)
        self.tasks.append(new_task)

    def mark_task_as_done(self, description):
        for task in self.tasks:
            if task.description == description:
                task.status = "выполнено"

    def get_current_tasks(self):
        current_tasks = [task for task in self.tasks if task.status == "не выполнено"]
        return current_tasks

# Пример использования
task_manager = TaskManager()

task_manager.add_task("Сдать д.з.", "01.06.2024")
task_manager.add_task("Сходить в магазин", "03.06.2024")

print("Текущие задачи:")
for task in task_manager.get_current_tasks():
    print(task.description, task.deadline, task.status)

task_manager.mark_task_as_done("Сдать д.з.")

print("\nПосле отметки задачи как выполненной:")
for task in task_manager.get_current_tasks():
    print(task.description, task.deadline, task.status)