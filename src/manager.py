class Task:
    def __init__(self, task_id: int, title: str):
        self.id = task_id
        self.title = title
        self.completed = False  # Toda tarefa começa como pendente

    def mark_completed(self):
        """[MUDANÇA DE ESCOPO] Marca a tarefa como concluída."""
        self.completed = True


class TaskManager:
    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add_task(self, title: str) -> Task:
        """Adiciona uma nova tarefa."""
        if not title or not isinstance(title, str):
            raise ValueError("O título deve ser um texto válido.")
        
        task = Task(self._next_id, title)
        self.tasks.append(task)
        self._next_id += 1
        return task

    def get_tasks(self) -> list:
        """Retorna a lista de tarefas."""
        return self.tasks

    def delete_task(self, task_id: int) -> bool:
        """Exclui uma tarefa pelo ID."""
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False

    def complete_task(self, task_id: int) -> bool:
        """[MUDANÇA DE ESCOPO] Conclui uma tarefa pelo ID."""
        for task in self.tasks:
            if task.id == task_id:
                task.mark_completed()
                return True
        return False