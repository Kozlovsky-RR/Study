class FileManager:
    def __init__(self, filename: str, mode: str = 'r') -> None:
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if self.file:
            self.file.close()
        if exc_val:
            print(f"Возбуждена ошибка {exc_val}")
            return True


with FileManager("example.txt", "w") as file:
    file.write("Hello, world!")
