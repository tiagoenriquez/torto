from functools import partial
import tkinter as tk
from typing import Callable

from modelos.Torto import Torto


class TortoComponent:

    def __init__(self, parentFrame: tk.Frame, linhas: int, torto: Torto, action: Callable[[int, int], None]) -> None:
        self.frame = tk.Frame(parentFrame)

        for linha in range(linhas):
            celulas = torto.celulas_da_linha(linha + 1)
            for coluna in range(len(celulas)):
                celula_button = tk.Button(
                    self.frame,
                    text=celulas[coluna].letra,
                    command=partial(action, linha + 1, coluna + 1))
                celula_button.grid(row=linha, column=coluna)