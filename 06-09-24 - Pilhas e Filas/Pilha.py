class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = [''] * capacidade
        
    def imprimir(self):
        if self.topo == -1:
            print('Pilha vazia')
        else:
            for i in range(self.topo + 1):
                print(self.valores[i])
        
    def pilhaCheia(self):
        return self.topo == self.capacidade -1
        
    def pilhaVazia(self):
        print('a')
        
    def empilhar(self, valor):
        if self.pilhaCheia():
            print('Pilha cheia!')
        else:
            self.topo += 1
            self.valores[self.topo] = valor
        
    def desempilhar(self, valor):
        print('a')
        
    def verTopo(self):
        print('a')
        
minhaPilha = Pilha(4)

resultado = minhaPilha.pilhaCheia()
print(resultado)

minhaPilha.empilhar(3)
minhaPilha.empilhar(2)
minhaPilha.empilhar(5)
minhaPilha.empilhar(123)

minhaPilha.imprimir()

minhaPilha.empilhar(666) # não vai entra

minhaPilha.imprimir()