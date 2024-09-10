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
                i = (i + 1) % self.capacidade  # Avança circularmente
                elementos_impressos += 1
            print()  # Quebra de linha após impressão
        

# Exemplo de uso:
minhaFila = Fila(5)

minhaFila.enfileirar(10)
minhaFila.enfileirar(20)
minhaFila.enfileirar(30)
minhaFila.imprimir()  # Saída esperada: 10 20 30

minhaFila.desenfileirar()
minhaFila.imprimir()  # Saída esperada: 20 30

minhaFila.enfileirar(40)
minhaFila.enfileirar(50)
minhaFila.imprimir()  # Saída esperada: 20 30 40 50
