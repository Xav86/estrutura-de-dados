
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
    def mostra_no(self):
        print(self.valor)


class ArvoreBinariaBusca:

    def __init__(self):
        self.raiz = None
        self.ligacoes = []

    def inserir(self, valor):
        novo = No(valor)

        #se a arvore estiver vazia

        if self.raiz == novo:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual

                #esquerda
                if valor < atual.valor:
                    atual = atual.esquerda
                    if atual == None:
                        pai.esquerda = novo
                        return
                    
                #direita
                else:
                    atual = atual.direita
                    if atual == None:
                        pai.direita = novo
                        return