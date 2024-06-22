from math import ceil
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from controllers.TortoController import TortoController
from modelos.Torto import Torto
from views.Frame import Frame as MyFrame
from views.components.TortoComponent import TortoComponent


class ListaFrame:

    def __init__(self, frame: MyFrame, tortos: list[Torto], n_paginas) -> None:
        self._my_frame = frame
        self._n_paginas = n_paginas
        self._my_frame.limpar()
        self._window = frame.window
        self._LINHAS_DO_TORTO = 6
        self._COLUNAS_DO_FRAME = 5

        self._frame = tk.Frame(self._window)
        self._frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self._paginas_frame = tk.Frame(self._frame)
        self._paginas_frame.grid(row=0, column=0)
        
        self._paginas_combobox = ttk.Combobox(self._paginas_frame, values=self._paginas())
        self._paginas_combobox.grid(row=0, column=0)
        self._paginas_combobox.bind("<<ComboboxSelected>>", lambda event: self._escolher_outra_pagina())

        self._tortos = tk.Frame(self._frame)
        self._tortos.grid(row=1, column=0)

        for i, torto in enumerate(tortos):
            torto_frame = TortoComponent(self._tortos, self._LINHAS_DO_TORTO, torto, self._fazer_nada)
            torto_frame.frame.grid(row=i // self._COLUNAS_DO_FRAME, column=i % self._COLUNAS_DO_FRAME, pady=16, padx=16)
        
        self._my_frame.manter_aberto()
    
    def _escolher_outra_pagina(self):
        TortoController().listar(self._my_frame, int(self._paginas_combobox.get()))
    
    def _fazer_nada(self, linha: int, coluna: int) -> None:
        messagebox.showerror("Erro", "Escolha de célula não habilitado para a tela em exibição")

    def _paginas(self) -> list[int]:
        paginas: list[int] = []
        for i in range(self._n_paginas):
            paginas.append(i + 1)
        return paginas