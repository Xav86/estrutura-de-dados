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
        
minhaFila = Fila(5)

