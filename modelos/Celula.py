from utils.remover_caracteres_especiais import remover_caracteres_especiais


class Celula:

    def __init__(self, linha: int, coluna: int, letra: str = '') -> None:
        self._linha = linha
        self._coluna = coluna
        self._letra = letra
    
    @property
    def linha(self) -> int:
        return self._linha
    
    @property
    def coluna(self) -> int:
        return self._coluna
    
    @property
    def letra(self) -> str:
        return self._letra
    
    @letra.setter
    def letra(self, letra: str) -> None:
        self._letra = remover_caracteres_especiais(letra)