import tkinter as tk
from typing import Callable


class PalavraComponent():

    def __init__(self, parent_frame: tk.Frame, action: Callable) -> None:
        self.frame = tk.Frame(parent_frame)

        palavra_label = tk.Label(self.frame, text="Digite uma palavra")
        palavra_label.grid(row=0, column=0)

        self.palavra_entry = tk.Entry(self.frame)
        self.palavra_entry.grid(row=0, column=1)
        self.palavra_entry.bind("<Return>", action)

        palavra_button = tk.Button(self.frame, text="Adicionar Palavra", command=action)
        palavra_button.grid(row=0, column=2)