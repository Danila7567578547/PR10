from datetime import datetime
from typing import List, Optional
from flask import Flask
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Task:
    """
    Класс для представления задачи в системе управления задачами.
    
    Attributes:
        id (int): Уникальный идентификатор задачи
        title (str): Заголовок задачи
        description (str): Подробное описание задачи
        status (str): Текущий статус задачи
        priority (int): Приоритет задачи (1-5)
        due_date (datetime): Срок выполнения задачи
        assigned_to (int): ID пользователя, которому назначена задача
    """
    
    def __init__(self, title: str, description: str, priority: int = 3):
        """
        Инициализация новой задачи.
        
        Args:
            title: Заголовок задачи
            description: Описание задачи
            priority: Приоритет задачи (по умолчанию 3)
        
        Raises:
            ValueError: Если приоритет вне диапазона 1-5
        """
        if not 1 <= priority <= 5:
            raise ValueError("Приоритет должен быть от 1 до 5")
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "новая"
        self.created_at = datetime.now()

class TaskManager:
    """
    Класс для управления задачами в системе.
    
    Предоставляет методы для создания, обновления, удаления и поиска задач.
    """
    
    def create_task(self, title: str, description: str, priority: int = 3) -> Task:
        """
        Создает новую задачу в системе.
        
        Args:
            title: Заголовок задачи
            description: Описание задачи
            priority: Приоритет задачи
            
        Returns:
            Task: Созданная задача
            
        Example:
            >>> manager = TaskManager()
            >>> task = manager.create_task("Разработка API", "Создать REST API", 4)
        """
        return Task(title, description, priority)
    
    def get_tasks_by_status(self, status: str) -> List[Task]:
        """
        Получает список задач с указанным статусом.
        
        Args:
            status: Статус для фильтрации задач
            
        Returns:
            List[Task]: Список задач с указанным статусом
        """
        pass

    def assign_task(self, task_id: int, user_id: int) -> bool:
        """
        Назначает задачу конкретному пользователю.
        
        Args:
            task_id: ID задачи
            user_id: ID пользователя
            
        Returns:
            bool: True если назначение прошло успешно, False в противном случае
        """
        pass

class User:
    """
    Класс для представления пользователя в системе.
    
    Attributes:
        id (int): Уникальный идентификатор пользователя
        username (str): Имя пользователя
        role (str): Роль пользователя в системе
        email (str): Email пользователя
    """
    
    def __init__(self, username: str, email: str, role: str = "исполнитель"):
        """
        Инициализация нового пользователя.
        
        Args:
            username: Имя пользователя
            email: Email пользователя
            role: Роль пользователя (по умолчанию "исполнитель")
        """
        self.username = username
        self.email = email
        self.role = role

def setup_app() -> Flask:
    """
    Настраивает и возвращает экземпляр Flask-приложения.
    
    Returns:
        Flask: Настроенное Flask-приложение
        
    Example:
        >>> app = setup_app()
        >>> app.run(debug=True)
    """
    app = Flask(__name__)
    return app

if __name__ == "__main__":
    app = setup_app()
    app.run(debug=True) 