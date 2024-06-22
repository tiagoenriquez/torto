import tkinter as tk

from modelos.Torto import Torto


class Frame:

    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.update_idletasks()

        largura_da_tela = self.window.winfo_screenwidth()
        altura_da_tela = self.window.winfo_screenheight()
        x = (largura_da_tela - 800) // 2
        y = (altura_da_tela - 800) // 2
        self.window.geometry(f"800x600+{x}+{y}")
        self.window.title("Torto")

        self._menu = tk.Menu(self.window)
        self.window.config(menu=self._menu)
        self._menu.add_command(label='Jogar', command=self._abrir_jogo)
        self._menu.add_command(label='Editar', command=self._abrir_edicao)
        self._menu.add_command(label='Lista', command=self._abrir_lista)

    def limpar(self):
        for widget in self.window.winfo_children():
            if (str(type(widget)) != "<class 'tkinter.Menu'>"):
                widget.destroy()
    
    def manter_aberto(self):
        self.window.mainloop()
    
    def _abrir_edicao(self) -> None:
        from controllers.TortoController import TortoController
        TortoController().editar(self, Torto())
    
    def _abrir_jogo(self) -> None:
        from controllers.TortoController import TortoController
        TortoController().jogar(self)
    
    def _abrir_lista(self) -> None:
        from controllers.TortoController import TortoController
        TortoController().listar(self, 1)