from typing import List, Optional
class NoAVL:
    def __init__(self, valor: int):
        self.chave = valor  # Valor do nó
        self.repeticoes = 1  # Número de repetições
        self.tamanho = 1  # Total de nós sob este nó
        self.altura = 1  # Altura da subárvore
        self.esq: Optional['NoAVL'] = None  # Filho esquerdo
        self.dir: Optional['NoAVL'] = None  # Filho direito
class Solution:
    def countSmaller(self, numeros: List[int]) -> List[int]:
        resultado = [0] * len(numeros)  # Lista de contagens
        arvore = None  
        indice = len(numeros) - 1  
        while indice >= 0:  
            arvore, resultado[indice] = self.inserir(arvore, numeros[indice], 0)  
            indice -= 1  
        return resultado  # Retorna lista final
    def inserir(self, no: Optional[NoAVL], valor: int, contagem: int) -> (Optional[NoAVL], int):
        if not no: return NoAVL(valor), contagem  # Cria nó novo
        if valor == no.chave:  
            no.repeticoes += 1  # Incrementa repetição
            contagem += self.tamanho(no.esq)  # Soma elementos à esquerda
        elif valor < no.chave:  
            no.esq, contagem = self.inserir(no.esq, valor, contagem)  # Insere à esquerda
        else:  # valor maior
            contagem += self.tamanho(no.esq) + no.repeticoes  # Soma menores e iguais
            no.dir, contagem = self.inserir(no.dir, valor, contagem)  # Insere à direita
        self.atualizar(no)  
        no = self.balancear(no)  # Balanceia árvore
        return no, contagem  
    def tamanho(self, no: Optional[NoAVL]) -> int:
        return 0 if not no else no.tamanho  
    def altura(self, no: Optional[NoAVL]) -> int:
        return 0 if not no else no.altura  
    def atualizar(self, no: NoAVL) -> None:
        no.tamanho = no.repeticoes + self.tamanho(no.esq) + self.tamanho(no.dir)  # Recalcula tamanho
        no.altura = 1 + max(self.altura(no.esq), self.altura(no.dir))  # Recalcula altura
    def fator_balancea(self, no: Optional[NoAVL]) -> int:
        return 0 if not no else self.altura(no.esq) - self.altura(no.dir)  # Calcula fator de balanceamento
    def rotacao_direita(self, no: NoAVL) -> NoAVL:
        novo_topo = no.esq  
        temp = novo_topo.dir  # Subárvore temporária
        novo_topo.dir = no  
        no.esq = temp  # Ajuste de ponteiro
        for n in [no, novo_topo]: self.atualizar(n)  # Atualiza alturas
        return novo_topo  # Retorna nova raiz
    def rotacao_esquerda(self, no: NoAVL) -> NoAVL:
        novo_topo = no.dir  
        temp = novo_topo.esq  
        novo_topo.esq = no  
        no.dir = temp  
        for n in [no, novo_topo]: self.atualizar(n)  
        return novo_topo  
    def ajustar_lr(self, no: NoAVL) -> NoAVL:
        no.esq = self.rotacao_esquerda(no.esq)  # Rotação esquerda no filho
        return self.rotacao_direita(no)  # Depois direita no pai
    def ajustar_rl(self, no: NoAVL) -> NoAVL:
        no.dir = self.rotacao_direita(no.dir)  # Rotação direita no filho
        return self.rotacao_esquerda(no)  # Depois esquerda no pai
    def balancear(self, no: NoAVL) -> NoAVL:
        fator = self.fator_balancea(no)  # Obtém fator
        if fator > 1:  # Esquerda
            if self.fator_balancea(no.esq) < 0: no = self.ajustar_lr(no)  # Caso LR
            else: no = self.rotacao_direita(no)  # Caso LL
        elif fator < -1:  # Direita
            if self.fator_balancea(no.dir) > 0: no = self.ajustar_rl(no)  # Caso RL
            else: no = self.rotacao_esquerda(no)  # Caso RR
        return no  # Retorna nó balanceado
