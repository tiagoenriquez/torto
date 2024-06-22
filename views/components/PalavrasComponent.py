import tkinter as tk

from modelos.Torto import Torto


class PalavrasComponent(tk.Frame):

    def __init__(self, parent_frame: tk.Frame, torto: Torto) -> None:
        LINHAS = 10
        self.frame = tk.Frame(parent_frame)

        for i, palavra in enumerate(torto.palavras):
            palavras_label = tk.Label(self.frame, text=f"{i + 1}: {palavra}")
            palavras_label.grid(row=i % LINHAS, column=i // LINHAS)