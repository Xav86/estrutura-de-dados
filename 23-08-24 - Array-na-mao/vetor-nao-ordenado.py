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


meuVetor = VetorNaoOrdenado(7)
meuVetor.imprimir()

meuNome = 'Gustavo'

for i in meuNome:
    print('--- inserindo a letara: ', i)
    meuVetor.inserir(i)
    meuVetor.imprimir()

print('Vetor atual: ')
meuVetor.imprimir()

print(meuVetor.pesquisar('g'))
print(meuVetor.pesquisar('G'))
print(meuVetor.pesquisar('u'))
print(meuVetor.pesquisar('v'))

meuVetor.excluir('G')
meuVetor.excluir('t')
meuVetor.excluir('o')

meuVetor.imprimir()