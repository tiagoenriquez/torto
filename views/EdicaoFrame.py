import tkinter as tk
from tkinter import messagebox
from controllers.TortoController import TortoController
from modelos.Celula import Celula
from modelos.Torto import Torto
from views.Frame import Frame as MyFrame
from views.components.PalavraComponent import PalavraComponent
from views.components.PalavrasComponent import PalavrasComponent
from views.components.TortoComponent import TortoComponent


class EdicaoFrame:

    def __init__(self, frame: MyFrame, torto: Torto) -> None:
        self._my_frame = frame
        self._torto = torto
        self._my_frame.limpar()
        self._window = frame.window
        self._LINHAS_DO_TORTO = 6
        self._celulas_escolhidas: list[Celula] = []

        self._frame = tk.Frame(self._window)
        self._frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self._cima_frame = tk.Frame(self._frame)
        self._cima_frame.grid(row=0, column=0)

        self._torto_frame = TortoComponent(self._cima_frame, self._LINHAS_DO_TORTO, self._torto, self._escolher_celula)
        self._torto_frame.frame.grid(row=0, column=0)

        self._palavras_frame = PalavrasComponent(self._cima_frame, self._torto)
        self._palavras_frame.frame.grid(row=0, column=1)

        self._palavra_frame = PalavraComponent(self._frame, self._inserir_palavra)
        self._palavra_frame.frame.grid(row=1, column=0)

        self._desistir_button = tk.Button(self._frame, text="Desistir", command=self._desistir)
        self._desistir_button.grid(row=1, column=1)
        
        self._my_frame.manter_aberto()
    
    def _desistir(self) -> None:
        TortoController().editar(self._my_frame, Torto())

    def _escolher_celula(self, linha: int, coluna: int) -> None:
        self._celulas_escolhidas.append(Celula(linha, coluna))
    
    def _inserir_palavra(self, event = None) -> None:
        try:
            palavra = self._palavra_frame.palavra_entry.get()
            self._torto.submeter_palavra(palavra, self._celulas_escolhidas, 'insercao')
            TortoController().inserir_palavra(self._my_frame, self._torto)
        except Exception as exception:
            messagebox.showerror("Erro", exception.args[0])
            self._celulas_escolhidas = []