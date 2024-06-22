from os import path
from random import randrange


class TortoDao:

    def __init__(self) -> None:
        script_dir = path.dirname(path.abspath(__file__))
        self._file = path.join(script_dir, "../datas", ".tortos.txt")
    
    def listar(self) -> list[str]:
        with open(self._file, 'r') as file:
            return file.readlines()[1:]

    def salvar(self, letras: str) -> None:
        modo = 'a' if path.exists(self._file) else 'w'
        with open(self._file, modo) as file:
            file.write(f"\n{letras}")
    
    def sortear(self) -> str:
        lines: list[str] = []
        with open(self._file, 'r') as file:
            lines = file.readlines()[1:]
        return lines[randrange(0, len(lines) - 1)]