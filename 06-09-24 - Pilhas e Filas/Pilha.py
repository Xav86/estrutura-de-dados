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
                print(self.valores[i], end=" ")
            print()
        
    def pilhaCheia(self):
        return self.topo == self.capacidade -1
        
    def pilhaVazia(self):
        return self.topo == -1
        
    def empilhar(self, valor):
        if self.pilhaCheia():
            print('Pilha cheia!')
        else:
            self.topo += 1
            self.valores[self.topo] = valor
        
    def desempilhar(self):
        if self.pilhaVazia():
            print('Pilha vazia')
        else:
            self.topo -= 1
        
    def verTopo(self):
        if self.topo == -1:
            return -1
        else:
            return self.valores[self.topo]
        
# minhaPilha = Pilha(4)

# resultado = minhaPilha.pilhaCheia()
# print(resultado)

# print('1---')

# minhaPilha.empilhar(3)
# minhaPilha.empilhar(2)
# minhaPilha.empilhar(5)
# minhaPilha.empilhar(123)

# print('2---')

# minhaPilha.imprimir()

# print('3---')

# minhaPilha.empilhar(666) # não vai entra

# print('4---')

# minhaPilha.imprimir()

# print('5---')

# topo = minhaPilha.verTopo()
# print(topo)

# print('6---')

# minhaPilha.desempilhar()

# print('7---')

# minhaPilha.imprimir()

# LISTA DE ATIVIDADES PARTE PILHA

minhaPilha = Pilha(7)

# NUMERO 7
# A
minhaPilha.desempilhar()

# B
meuNome = 'Gustavo'
for i in meuNome:
    minhaPilha.empilhar(i)
    minhaPilha.imprimir()

# C
minhaPilha.empilhar('coisa')

# D
topo = minhaPilha.verTopo()
print('Topo da fila: ', topo)

# E
for i in range(3):
    minhaPilha.desempilhar()
    
print('---')
topo = minhaPilha.verTopo()
print('Topo da fila: ', topo)


# NUMERO 8
# "S"

# NUMERO 9
# ficar vendo a posição do topo para determinar as ações (sinceramente n sei qual é o problema, falei algo q acho meio chatinho mesmo)

# NUMERO 10
# Se o topo for igual a -1

# NUMERO 11
# se a posição do topo for igual ao tamanho da pila (capacidade -1)