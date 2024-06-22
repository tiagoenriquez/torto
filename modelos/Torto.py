from daos.TortoDao import TortoDao
from modelos.Celula import Celula
from utils.remover_caracteres_especiais import remover_caracteres_especiais


class Torto:

    def __init__(self, letras: str = '') -> None:
        self._init_celulas(letras)
        self._palavras: list[str] = []
    
    @property
    def celulas(self) -> list[Celula]:
        return self._celulas
    
    @property
    def palavras(self) -> list[str]:
        self._palavras.sort()
        return self._palavras
    
    def celulas_da_linha(self, linha: int) -> list[Celula]:
        celulas_da_linha: list[Celula] = []
        for celula in self._celulas:
            if celula.linha == linha:
                celulas_da_linha.append(celula)
        return celulas_da_linha
    
    def submeter_palavra(self, palavra: str, celulas: list[Celula], fim: str = 'checagem') -> None:
        self._validar_tamanho(palavra, celulas)
        self._checar_palavra_repetida(palavra)
        self._validar_celulas(celulas)
        self._validar_caminho(palavra, celulas)
        if fim == 'insercao':
            for i in range(len(celulas)):
                for j in range(len(self._celulas)):
                    if celulas[i].linha == self._celulas[j].linha and celulas[i].coluna == self._celulas[j].coluna:
                        self._celulas[j].letra = palavra[i]
        self._palavras.append(palavra)
    
    def salvar(self) -> None:
        letras = ''
        for celula in self._celulas:
            letras += celula.letra
        TortoDao().salvar(letras)
    
    def _checar_celulas_repetidas(self, celulas: list[Celula]) -> None:
        for i in range(len(celulas) - 1):
            for j in range(i + 1, len(celulas)):
                if celulas[i].linha == celulas[j].linha and celulas[i].coluna == celulas[j].coluna:
                    raise Exception("Células repetidas")
    
    def _checar_celulas_vizinhas(self, celulas: list[Celula]) -> None:
        for i in range(len(celulas) - 1):
            if abs(celulas[i].linha - celulas[i + 1].linha) > 1 or abs(celulas[i].coluna - celulas[i + 1].coluna) > 1:
                mensagem = "Há células não vizinhas no caminho passado: "
                mensagem += f"({celulas[i].linha}, {celulas[i].coluna}), "
                mensagem += f"({celulas[i + 1].linha}, {celulas[i + 1].coluna})"
                raise Exception(mensagem)

    
    def _checar_palavra_repetida(self, palavra_nova: str) -> None:
        for palavra_salva in self._palavras:
            if remover_caracteres_especiais(palavra_salva) == remover_caracteres_especiais(palavra_nova):
                raise Exception(f"A palavra '{palavra_nova}' já foi inserida.")

    def _init_celulas(self, letras: str) -> None:
        self._celulas: list[Celula] = []
        for i in range(6):
            linha = i + 1
            for j in range(3):
                letra = letras[i * 3 + j] if letras != '' else ' '
                coluna = j + 1
                self._celulas.append(Celula(linha, coluna, letra))
    
    def _validar_celulas(self, celulas: list[Celula]) -> None:
        for celula in celulas:
            if celula.linha < 1 or celula.linha > 6 or celula.coluna < 1 or celula.coluna > 3:
                raise Exception("Célula inválida")
    
    def _validar_tamanho(self, palavra: str, celulas: list[Celula]) -> None:
        if len(palavra) != len(celulas):
            raise Exception("Palavra e caminho incompatíveis")
    def _checar_caminho_divergente(self, palavra: str, celulas: list[Celula]) -> None:
        palavra = remover_caracteres_especiais(palavra)
        for i in range(len(celulas)):
            for j in range(len(self._celulas)):
                if celulas[i].linha == self._celulas[j].linha and celulas[i].coluna == self._celulas[j].coluna:
                    if self._celulas[j].letra != palavra[i] and self._celulas[j].letra != ' ':
                        raise Exception("Sobreescrita indevida de letra")
    
    def _validar_caminho(self, palavra: str, celulas: list[Celula]) -> bool:
        self._checar_celulas_repetidas(celulas)
        self._checar_celulas_vizinhas(celulas)
        self._checar_caminho_divergente(palavra, celulas)