import pytest
from src.manager import TaskManager

def test_add_task():
    """Garante que adicionar uma tarefa funciona no sistema."""
    manager = TaskManager()
    task = manager.add_task("Configurar ambiente TechFlow")
    assert len(manager.get_tasks()) == 1
    assert task.title == "Configurar ambiente TechFlow"
    assert task.completed is False

def test_add_invalid_task():
    """Garante que o sistema não aceita tarefas com título inválido."""
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.add_task("")

def test_delete_task():
    """Garante que deletar uma tarefa funciona."""
    manager = TaskManager()
    task = manager.add_task("Tarefa para deletar")
    assert manager.delete_task(task.id) is True
    assert len(manager.get_tasks()) == 0

def test_complete_task_change_scope():
    """[MUDANÇA DE ESCOPO] Garante que marcar como concluída funciona."""
    manager = TaskManager()
    task = manager.add_task("Tarefa para concluir")
    assert manager.complete_task(task.id) is True
    assert task.completed is True