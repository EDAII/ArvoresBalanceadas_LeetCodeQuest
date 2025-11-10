class NoRubroNegro:
    def __init__(self, valor):
        self.valor = valor  # Valor armazenado
        self.esquerda = None  # Filho esquerdo
        self.direita = None  # Filho direito
        self.cor_vermelha = True  # Nova aresta nasce vermelha
        self.repeticoes = 1  # Quantas vezes o valor foi inserido
        self.tamanho_subarvore = 1  # Total (Incluindo repetições)
def tamanho(no):  # Retorna tamanho 
    return 0 if no is None else no.tamanho_subarvore  
class Solution:
    def __init__(self):
        self.raiz = None  # Raiz da árvore
    def eh_vermelho(self, no):  # Verifica cor do nó
        return no is not None and no.cor_vermelha  # True, se vermelho
    def rotacao_esquerda(self, no_raiz):  # Rotação à esquerda
        novo_topo = no_raiz.direita  # Define novo topo
        no_raiz.direita = novo_topo.esquerda  # Move subárvore
        novo_topo.esquerda = no_raiz  
        novo_topo.cor_vermelha = no_raiz.cor_vermelha  # Herda cor
        no_raiz.cor_vermelha = True  # Filho fica vermelho
        for atual in [no_raiz, novo_topo]:  # Atualiza tamanhos
            atual.tamanho_subarvore = atual.repeticoes + tamanho(atual.esquerda) + tamanho(atual.direita)
        return novo_topo  
    def rotacao_direita(self, no_raiz):  # Rotação à direita
        novo_topo = no_raiz.esquerda  
        no_raiz.esquerda = novo_topo.direita 
        novo_topo.direita = no_raiz  
        novo_topo.cor_vermelha = no_raiz.cor_vermelha 
        no_raiz.cor_vermelha = True  
        for atual in [no_raiz, novo_topo]:  
            atual.tamanho_subarvore = atual.repeticoes + tamanho(atual.esquerda) + tamanho(atual.direita)
        return novo_topo  
    def inverter_cores(self, no_raiz):  # Divide nó 4
        no_raiz.cor_vermelha = True  # Pai vira vermelho
        if no_raiz.esquerda: no_raiz.esquerda.cor_vermelha = False  # Filho esquerdo preto
        if no_raiz.direita: no_raiz.direita.cor_vermelha = False  # Filho direito preto
    def inserir_recursivo(self, no_raiz, valor):  # Insere mantendo balanceamento
        if no_raiz is None: return NoRubroNegro(valor)  # Novo nó vermelho
        if valor < no_raiz.valor:
            no_raiz.esquerda = self.inserir_recursivo(no_raiz.esquerda, valor)  # Insere à esquerda
        elif valor > no_raiz.valor:
            no_raiz.direita = self.inserir_recursivo(no_raiz.direita, valor)  # Insere à direita
        else:
            no_raiz.repeticoes += 1  # Valor repetido
        if self.eh_vermelho(no_raiz.direita) and not self.eh_vermelho(no_raiz.esquerda): no_raiz = self.rotacao_esquerda(no_raiz)  # Corrige inclinação direita
        if self.eh_vermelho(no_raiz.esquerda) and self.eh_vermelho(no_raiz.esquerda.esquerda): no_raiz = self.rotacao_direita(no_raiz)  # Corrige duplo vermelho
        if self.eh_vermelho(no_raiz.esquerda) and self.eh_vermelho(no_raiz.direita): self.inverter_cores(no_raiz)  
        no_raiz.tamanho_subarvore = no_raiz.repeticoes + tamanho(no_raiz.esquerda) + tamanho(no_raiz.direita)  
        return no_raiz  
    def inserir(self, valor):  
        self.raiz = self.inserir_recursivo(self.raiz, valor)  # Chama recursão
        self.raiz.cor_vermelha = False  # Raiz sempre preta
    def buscar_por_posicao(self, k):  # Busca o k-ésimo elemento
        no_atual = self.raiz  
        for _ in range(tamanho(self.raiz)):  
            tam_esq = tamanho(no_atual.esquerda)  
            if k <= tam_esq: no_atual = no_atual.esquerda  
            elif k > tam_esq + no_atual.repeticoes:
                k -= (tam_esq + no_atual.repeticoes)  
                no_atual = no_atual.direita  
            else: return no_atual.valor  
        raise IndexError("Posição fora dos limites")  # Erro seguro
    def tamanho_total(self):  # Total de elementos
        return tamanho(self.raiz)  # Acessa tamanho da raiz
class MedianFinder:
    def __init__(self):
        self.buscador = Solution()  
    def addNum(self, num: int) -> None:
        self.buscador.inserir(num)  # Insere número
    def findMedian(self) -> float:
        n = self.buscador.tamanho_total()  # Total de elementos
        if n == 0: return 0.0  # Caso vazio
        if n % 2 == 1: return float(self.buscador.buscar_por_posicao((n + 1) // 2))  
        menor = self.buscador.buscar_por_posicao(n // 2)  # Central esquerda
        maior = self.buscador.buscar_por_posicao(n // 2 + 1)  # Central direita
        return (menor + maior) / 2.0  # Média dos dois
