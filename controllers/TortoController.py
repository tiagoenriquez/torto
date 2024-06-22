from math import ceil
from daos.TortoDao import TortoDao
from modelos.Torto import Torto
from views.Frame import Frame


class TortoController:

    def checar(self, frame: Frame, torto: Torto) -> None:
        from views.JogoFrame import JogoFrame
        JogoFrame(frame, torto)

    def editar(self, frame: Frame, torto: Torto) -> None:
        from views.EdicaoFrame import EdicaoFrame
        EdicaoFrame(frame, torto)
    
    def inserir_palavra(self, frame: Frame, torto: Torto) -> None:
        torto = self._salvar(torto)
        self.editar(frame, torto)
    
    def jogar(self, frame: Frame) -> None:
        from views.JogoFrame import JogoFrame
        try:
            JogoFrame(frame, Torto(TortoDao().sortear()))
        except Exception:
            self.editar(frame, Torto())
    
    def listar(self, frame: Frame, page: int) -> None:
        from views.ListaFrame import ListaFrame
        lista_de_letras = TortoDao().listar()
        n_paginas = ceil(len(lista_de_letras) / 10)
        inicio = (page - 1) * 10
        fim = page * 10 if page < len(lista_de_letras) / 10 else len(lista_de_letras)
        tortos: list[Torto] = []
        for i in range(inicio, fim):
            tortos.append(Torto(lista_de_letras[i]))
        ListaFrame(frame, tortos, n_paginas)

    def _salvar(self, torto: Torto) -> Torto:
        if len(torto.palavras) == 30:
            torto.salvar()
            torto = Torto()
        return torto