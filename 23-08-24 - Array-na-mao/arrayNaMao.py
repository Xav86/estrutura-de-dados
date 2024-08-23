class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = [''] * capacidade

    def inserir(self, valor):
        if self.ultimaPosicao == self.capacidade -1:
            print('Vetor Cheio')
        else:
            self.ultimaPosicao += 1
            self.valores[self.ultimaPosicao] = valor

    def imprimir(self):
        if (self.ultimaPosicao == -1):
            print('vetor vazio')
        else:
            for i in range(self.ultimaPosicao + 1):
                print(f'Posição {i} | Valor {self.valores[i]}')

    def pesquisar(self, valor):
        for i in range(self.ultimaPosicao +1):
            if (self.valores[i] == valor):
                return i
        return -1
    
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if (posicao == -1):
            return -1
        else:
            for i in range(posicao, self.ultimaPosicao):
                self.valores[i] = self.valores[i+1]
            self.ultimaPosicao -= 1


meuVetor = VetorNaoOrdenado(4)
meuVetor.imprimir()

meuVetor.inserir(2)
meuVetor.inserir(17)
meuVetor.inserir(7)
meuVetor.inserir(25)
meuVetor.inserir(666) #print Vetor cheio

meuVetor.imprimir()

print(meuVetor.pesquisar(17)) #1
print(meuVetor.pesquisar(35)) #-1
print(meuVetor.pesquisar(25)) #3

meuVetor.excluir(17)
meuVetor.imprimir()

meuVetor.excluir(55) #-1
