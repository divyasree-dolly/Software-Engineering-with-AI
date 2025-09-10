class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not isinstance(task, str) or not task.strip():
            return "Invalid task. Please provide a non-empty string."
        if task in self.tasks:
            return f"Task '{task}' already exists."
        if task == "":
            return "Invalid task. Please provide a non-empty string."
        self.tasks.append(task)
        return f"Task '{task}' added."

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return f"Task '{task}' removed."
        else:
            return "Task not found."

    def list_tasks(self):
        return self.tasks

# Example usage
if __name__ == "__main__":
    manager = TaskManager()
    print(manager.add_task("Buy groceries"))
    print(manager.add_task("Read a book"))
    print(manager.add_task("Buy groceries"))  # Duplicate
    print(manager.add_task(""))               # Invalid
    print(manager.list_tasks())
    print(manager.remove_task("Read a book"))
    print(manager.list_tasks())