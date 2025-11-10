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
    def em_ordem(self, no, lista):  # Percorre árvore em ordem
        if no is None: return  
        self.em_ordem(no.esquerda, lista)  # Visita esquerda
        for _ in range(no.repeticoes): lista.append(no.valor)  # Adiciona valor
        self.em_ordem(no.direita, lista)  # Visita direita
class SummaryRanges:
    def __init__(self):
        self.arvore = Solution()  
    def addNum(self, valor: int) -> None:
        self.arvore.inserir(valor)  # Insere valor no fluxo
    def getIntervals(self) -> List[List[int]]:
        valores = []  
        self.arvore.em_ordem(self.arvore.raiz, valores)  
        valores_unicos = sorted(set(valores)) 
        intervalos = []  
        if len(valores_unicos) > 0: # Verifica se há elementos  
            indice = 0  
            inicio = valores_unicos[indice] # Define início do intervalo  
            fim = inicio # Define fim inicial  
            while indice < len(valores_unicos) - 1: # Percorre a lista ordenada  
                proximo_valor = valores_unicos[indice + 1]  
                if proximo_valor == fim + 1:  
                    fim = proximo_valor # Atualiza o fim  
                else: # Caso contrário, quebra o intervalo  
                    intervalo_atual = [inicio, fim]  
                    intervalos.append(intervalo_atual) # Adiciona  
                    inicio = fim = proximo_valor # Reinicia novo intervalo  
                indice += 1 # Avança o índice  
            intervalos.append([inicio, fim]) # Adiciona último intervalo  
        else:  
            return []  
        return intervalos # Retorna lista final de intervalos  
