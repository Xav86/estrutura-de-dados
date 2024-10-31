
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
                    
    def pesquisar(self, valor):
        atual = self.raiz
        while atual.valor != valor:
            if valor < atual.esquerda:
                atual = atual.esquerda
            else:
                atual = atual.direita
            
            if atual == None:
                return None
            
        return atual
    

    #raiz, esquerda, direita
    def preOrdem(self, no):
        if no != None:
            print(no.valor)
            self.preOrdem(no.esquerda)
            self.preOrdem(no.direita)

    #esquerda, raiz, direita
    def emOrdem(self, no):
        if no != None:
            self.emOrdem(no.esquerda)
            print(no.valor)
            self.emOrdem(no.direita)

    def posOrdem(self, no):
        if no != None:
            self.posOrdem(no.esquerda)
            self.posOrdem(no.direita)
            print(no.valor)
    
    def excluir(self, valor):
        if self.raiz == None:
            print('A arvore esta vazia')
            return

        #encontrar o nó
        atual = self.raiz
        pai = self.raiz
        e_esquerda = True

        while atual.valor != valor:
            pai = atual
            
            #esquerda
            if valor < atual.valor:
                e_esquerda = True
                atual = atual.esquerda
            #direita
            else:
                e_esquerda = False
                atual = atual.direita
            
            if atual == None:
                return False
            
        #o nó a ser apagado é uma folha
        if (atual.esquerda) == None and atual.direita == None:
            if atual == self.raiz:
                self.raiz = None
            elif e_esquerda == True:
                pai.esquerda = None
            else:
                pai.direita = None
            
        #o nó a ser apagado não possui filho a direta
        elif atual.direta == None:
            if atual == self.raiz:
                self.raiz = atual.esuqerda
            elif e_esquerda == True:
                pai.esquerda = atual.esquerda
            else:
                pai.direita = atual.esquerda
            
        #o nó a ser apagado não possui filho a esquerda
        elif atual.esquerda == None:
            if atual == self.raiz:
                self.raiz = atual.direita
            elif e_esquerda == True:
                pai.esquerda = atual.direita
            else:
                pai.direita = atual.direita
        
        #o nó possui dois filhos :O
        else:
            sucessor = self.getSucessor(atual)
            if atual == self.raiz:
                self.raiz = sucessor
            elif e_esquerda == True:
                pai.esquerda = sucessor
            else:
                pai.direita = sucessor
            
            sucessor.esquerda = atual.esquerda
            
        return True

    def getSucessor(self, no):
        paiSucessor = no
        sucessor = no
        atual = no.direita

        while atual != None:
            paiSucessor = sucessor
            sucessor = atual
            atual = atual.esquerda
        
        if sucessor != no.direita:
            paiSucessor.esquerda = sucessor.direita
            sucessor.direita = no.direita
        
        return sucessor
        
