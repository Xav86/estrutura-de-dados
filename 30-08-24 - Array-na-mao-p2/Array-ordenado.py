import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def inserir(self, valor):
        if self.ultimaPosicao == self.capacidade -1:
            print('Vetor Cheio')
            return
        
        # inserição ordenada
        # achar onde inserir
        posicao = 0
        for i in range(self.ultimaPosicao + 1):
            posicao = i

            #achou o local para inserir
            if (self.valores[i] > valor):
                break

            # é para inseir no final
            if (i == self.ultimaPosicao):
                posicao = i + 1
            
        # inserção
        j = self.ultimaPosicao
        while(j >= posicao):
            self.valores[j + 1] = self.valores[j]
            j -= 1
        
        self.valores[posicao] = valor
        self.ultimaPosicao += 1

    def imprimir(self):
        if (self.ultimaPosicao == -1):
            print('vetor vazio')
        else:
            for i in range(self.ultimaPosicao + 1):
                print(f'Posição {i} | Valor {self.valores[i]}')

    def pesquisaBinaria(self, valor):
        limiteInf = 0
        limiteSup = self.ultimaPosicao

        while True:
            posicaoAtual = int((limiteInf + limiteSup) / 2)

            # achou
            if (self.valores[posicaoAtual] == valor):
                return posicaoAtual

            #não achou
            elif (limiteInf > limiteSup):
                return -1
            
            # escolhe um lado e vai!
            else:

                # direita se é maior
                if (self.valores[posicaoAtual] < valor):
                    limiteInf = posicaoAtual + 1
                # esquerda se é menor
                else:
                    limiteSup = posicaoAtual - 1
                
    def pesquisar(self, valor):
        for i in range(self.ultimaPosicao +1):

            # achou maior q ele

            if (self.valores[i] > valor):
                return -1

            if (self.valores[i] == valor):
                return i
        # F
        return -1
    
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if (posicao == -1):
            return -1
        else:
            for i in range(posicao, self.ultimaPosicao):
                self.valores[i] = self.valores[i+1]
            self.ultimaPosicao -= 1


meuVetor = VetorNaoOrdenado(7)
meuVetor.imprimir()

meuVetor.inserir(2)
meuVetor.inserir(666)
meuVetor.inserir(7)
meuVetor.inserir(25)
meuVetor.inserir(17)

meuVetor.imprimir()

print(meuVetor.pesquisar(17))
print(meuVetor.pesquisar(35)) #-1
print(meuVetor.pesquisar(25))

meuVetor.excluir(17)
meuVetor.imprimir()

meuVetor.excluir(55) #-1
