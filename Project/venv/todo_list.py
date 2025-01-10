class Task:
    def __init__(self, title, description, due_date, priority, status="Pending"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"{self.title} - {self.status}"

    def mark_as_completed(self):
        self.status = "Completed"

    def edit(self, title=None, description=None, due_date=None, priority=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if due_date:
            self.due_date = due_date
        if priority:
            self.priority = priority


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date, priority, status="Pending"):
        task = Task(title, description, due_date, priority, status)
        self.tasks.append(task)

    def list_tasks(self):
        return [
            {
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date,
                "priority": task.priority,
                "status": task.status,
            }
            for task in self.tasks
        ]

    def mark_task_as_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_as_completed()

    def clear_tasks(self):
        self.tasks.clear()

    def edit_task(self, title, new_title=None, new_description=None, new_due_date=None, new_priority=None):
        for task in self.tasks:
            if task.title == title:
                task.edit(new_title, new_description, new_due_date, new_priority)

    def filter_tasks_by_status(self, status):
        return [
            {
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date,
                "priority": task.priority,
                "status": task.status,
            }
            for task in self.tasks
            if task.status == status
        ]
