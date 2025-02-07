"""Контекстный менеджр для работы с файлами."""


import os
from typing import TextIO


class FileManager:
    """Класс Файловый менеджер."""
    def __init__(self, filename: str, mode: str = 'r') -> None:
        """Инициализация файла, и проверка режима доступа."""
        self.filename = filename
        if mode[0] in 'rwxat' and all(c in 'bt' for c in mode[1:]):
            self.mode = mode
        else:
            raise ValueError('Режим не допустим')
        self.file = None

    def __enter__(self) -> TextIO:
        """Открытие файла, и проверка на его существование."""
        if 'r' in self.mode and not os.path.isfile(self.filename):
            raise FileNotFoundError("Файл не существует")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """Закрытие файла, и вывод ошибки при ее наличии."""
        if self.file:
            self.file.close()
        if exc_val:
            raise Exception(f'ошибка: {exc_val}')
        else:
            return True


with FileManager("example.txt", "w") as file:
    file.write("Hello, world!")
