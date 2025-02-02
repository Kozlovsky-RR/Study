"""Контекстный менеджр для работы с файлами."""
import os


class FileManager:
    def __init__(self, filename: str, mode: str = 'r') -> None:
        self.filename = filename
        if mode in ('r', 'w', 'x', 'a', 'b', 't'):
            self.mode = mode
        else:
            raise ValueError('Режим не допустим')

    def __enter__(self):
        if self.mode != 'r' and os.path.isfile(self.filename):
            self.file = open(self.filename, self.mode)
            return self.file
        else:
            raise FileNotFoundError("Файла не существует")

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if self.file:
            self.file.close()
        if exc_val:
            raise exc_val(f'ошибка: {exc_val}')
        else:
            return True


with FileManager("example.txt", "w") as file:
    file.write("Hello, world!")
