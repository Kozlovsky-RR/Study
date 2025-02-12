"""Система для управления зарплат сотрудников компании."""


MULTIPLIER_BONUS_DESIGNER = 2
MULTIPLIER_BONUS_DEVELOPER = 3
MULTIPLIER_BONUS_MANAGER = 4


class Employee:
    """Класс для создания сотрудников."""
    def __init__(self, name: str, surname: str, post: str, salary: int) -> None:
        """Инициализация сотрудника. Проверка что зарплата является не отрицательным числом."""
        self.name: str = name
        self.surname: str = surname
        self.post: str = post
        if isinstance(salary, int) and salary >= 0:
            self.salary: int = salary
        else:
            raise TypeError("Зарплата должна быть положительным числом")

    def get_bonus(self) -> int:
        """Метод для вычисления бонуса."""
        return self.salary

    def __str__(self) -> str:
        """Неформальное представление сотрудника."""
        return f"{self.name}, {self.surname}, {self.post}, {self.salary}"


class Manager(Employee):
    """Класс менеджер."""

    def get_bonus(self) -> int:
        """Метод для вычисления бонуса."""
        return super().get_bonus() * MULTIPLIER_BONUS_MANAGER


class Developer(Employee):
    """Класс разработчик."""

    def get_bonus(self) -> int:
        """Метод для вычисления бонуса."""
        return super().get_bonus() * MULTIPLIER_BONUS_DEVELOPER


class Designer(Employee):
    """Класс дизайнер."""

    def get_bonus(self) -> int:
        """Метод для вычисления бонуса."""
        return super().get_bonus() * MULTIPLIER_BONUS_DESIGNER


employees: list[Employee] = [
    Manager("Иван", "Иванов", "Менеджер", 100000),
    Developer("Петр", "Петров", "Разработчик", 80000),
    Designer("Анна", "Смирнова", "Дизайнер", 70000)
]

for employee in employees:
    print(employee.get_bonus())
