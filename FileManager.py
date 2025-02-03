"""Контекстный менеджр для работы с файлами."""
import os


class FileManager:
    """Класс Файловый менеджер."""
    def __init__(self, filename: str, mode: str = 'r') -> None:
        """Инициализация файла, и проверка режима доступа."""
        self.filename = filename
        if mode in ('r', 'w', 'x', 'a', 'b', 't'):
            self.mode = mode
        else:
            raise ValueError('Режим не допустим')

    def __enter__(self):
        """Открытие файла, и проверка на его существование."""
        if self.mode != 'r' and os.path.isfile(self.filename):
            self.file = open(self.filename, self.mode)
            return self.file
        else:
            raise FileNotFoundError("Файла не существует")

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """Закрытие файла, и вывод ошибки при ее наличии."""
        if self.file:
            self.file.close()
        if exc_val:
            raise exc_val(f'ошибка: {exc_val}')
        else:
            return True


with FileManager("example.txt", "w") as file:
    file.write("Hello, world!")
