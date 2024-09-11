class Fila:
    def __init__(self, capacidade):
        self.inicio = 0
        self.final = -1
        self.elementos = 0
        self.capacidade = capacidade
        self.valores = [''] * capacidade
        
    def filaCheia(self):
        return self.elementos == self.capacidade
        
    def filaVazia(self):
        return self.elementos == 0
        
    def enfileirar(self, valor):
        if (self.filaCheia()):
            print('Filha cheia!')
            return

        if (self.final == self.capacidade - 1):
            self.final = -1
            
        self.final += 1
        
        self.valores[self.final] = valor
        self.elementos += 1
        
    def desenfileirar(self):
        if (self.filaVazia()):
            print('Fila vazia!')
            return
        
        temp = self.valores[self.inicio]
        self.inicio += 1
        
        if (self.inicio == self.capacidade):
            self.inicio = 0
            
        self.elementos -= 1
        
        return temp
        
    def verPrimeiro(self):
        if (self.filaVazia()):
            return -1
        
        return self.valores[self.inicio]
    
    def imprimir(self):
        if self.filaVazia():
            print("Fila vazia!")
        else:
            i = self.inicio
            elementos_impressos = 0
            while elementos_impressos < self.elementos:
                print(self.valores[i], end=" ")
                i = (i + 1) % self.capacidade
                elementos_impressos += 1
            print()
        

# minhaFila = Fila(5)

# minhaFila.enfileirar(10)
# minhaFila.enfileirar(20)
# minhaFila.enfileirar(30)

# minhaFila.imprimir()

# minhaFila.desenfileirar()

# minhaFila.imprimir() 

# minhaFila.enfileirar(40)
# minhaFila.enfileirar(50)

# minhaFila.imprimir()

# NUMERO 1

minhaFila = Fila(7)

# A
minhaFila.desenfileirar()

# B
meuNome = 'Gustavo'
for i in meuNome:
    minhaFila.enfileirar(i)
    minhaFila.imprimir()
    
# C
minhaFila.enfileirar('qualquerCoisa')

# D
primeiroElemento = minhaFila.verPrimeiro()
print('primeiro elemento', primeiroElemento)

# E
for i in range(3):
    minhaFila.desenfileirar()

primeiroElemento = minhaFila.verPrimeiro()
print('primeiro elemento agora', primeiroElemento)

minhaFila.imprimir()

# NUMERO 2
# Envolve primeiro saber se a pilha esta cheia, se não estiver tem que saber qual a ultima posição de self.final, pra não passar da capacidade da fila, voltando ela pro inicio da fila
# aquele negócio de ser circular

# NUMERO 3
# Mais ou menos como enfileirar, se que aqui temover que ver se a fila esta vazia, senão estiver temos que saber qual o primeiro elemento para removelo e isso levando em conta que não passou
# do tamanho da fila que é a capacidade manteindo o negócio circular

# NUMERO 4
# Se o numero de elementos na fila for 0

# NUMERO 5
# se o numero de elementos é igual a capacidade maxima

# NUMERO 6
# vai ta no word q vou envia junto