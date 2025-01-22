class Employee:
    def __init__(self, name: str, surname: str, post: str, salary: int) -> None:
        self.name = name
        self.surname = surname
        self.post = post
        self.salary = salary

    def get_bonus(self) -> int:
        return self.salary

    def __str__(self) -> str:
        return f"{self.name}, {self.surname}, {self.post}, {self.salary}"


class Manager(Employee):
    def __init__(self, name: str, surname: str, post: str, salary: int) -> None:
        super().__init__(name, surname, post, salary)

    def get_bonus(self) -> int:
        return super().get_bonus() * 4


class Developer(Employee):
    def __init__(self, name: str, surname: str, post: str, salary: int) -> None:
        super().__init__(name, surname, post, salary)

    def get_bonus(self) -> int:
        return super().get_bonus() * 3


class Designer(Employee):
    def __init__(self, name: str, surname: str, post: str, salary: int) -> None:
        super().__init__(name, surname, post, salary)

    def get_bonus(self) -> int:
        return super().get_bonus() * 2


employees = [
    Manager("Иван", "Иванов", "Менеджер", 100000),
    Developer("Петр", "Петров", "Разработчик", 80000),
    Designer("Анна", "Смирнова", "Дизайнер", 70000)
]

for employee in employees:
    print(employee.get_bonus())
