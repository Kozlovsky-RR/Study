"""Система для управления зарплат сотрудников компании."""


class Employee:
    """Класс для создания сотрудников."""
    def __init__(self, name: str, surname: str, post: str, salary: int) -> None:
        """Инициализация сотрудника. Проверка что зарплата является не отрицательным числом."""
        self.name = name
        self.surname = surname
        self.post = post
        if isinstance(salary, int) and salary >= 0:
            self.salary = salary
        else:
            raise TypeError("Зарплата должна быть положительным числом")

    def get_bonus(self) -> int:
        """Метод для вычисление бонуса."""
        return self.salary

    def __str__(self) -> str:
        """Неформальное представление сотрудника."""
        return f"{self.name}, {self.surname}, {self.post}, {self.salary}"


class Manager(Employee):
    """Класс менеджер."""
    def __init__(self, name: str, surname: str, post: str, salary: int) -> None:
        """Инициализация сотрудника. Проверка что зарплата является не отрицательным числом."""
        super().__init__(name, surname, post, salary)

    def get_bonus(self) -> int:
        """Метод для вычисление бонуса."""
        return super().get_bonus() * 4


class Developer(Employee):
    """Класс разработчик."""
    def __init__(self, name: str, surname: str, post: str, salary: int) -> None:
        """Инициализация сотрудника. Проверка что зарплата является не отрицательным числом."""
        super().__init__(name, surname, post, salary)

    def get_bonus(self) -> int:
        """Метод для вычисление бонуса."""
        return super().get_bonus() * 3


class Designer(Employee):
    """Класс дизайнер."""
    def __init__(self, name: str, surname: str, post: str, salary: int) -> None:
        """Инициализация сотрудника. Проверка что зарплата является не отрицательным числом."""
        super().__init__(name, surname, post, salary)

    def get_bonus(self) -> int:
        """Метод для вычисление бонуса."""
        return super().get_bonus() * 2


employees = [
    Manager("Иван", "Иванов", "Менеджер", 100000),
    Developer("Петр", "Петров", "Разработчик", 80000),
    Designer("Анна", "Смирнова", "Дизайнер", 70000)
]

for employee in employees:
    print(employee.get_bonus())