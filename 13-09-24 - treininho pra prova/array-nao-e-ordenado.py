# pelo q o professor falo vamos ter o pseudocódigo e precisaremos fazer o resto, ent vou tenta refazer só com o pseudocódigo


### TENTATIVA TIRANDO TUDO DA MINHA CABEÇA (o excluir ali me matou, vou de uma vez pra tentativa olhando o pseudo-código)

# class VetorNaoOrdenado:
    
#     def __init__(self, capacidade):
#         self.capacidade = capacidade
#         self.ultimaPosicao = -1
#         self.valores = [''] * capacidade
        
#     def imprimir(self):
#         if (self.ultimaPosicao == -1):
#             print('Vetor Vazio')
#         else:
#             for i in range(self.ultimaPosicao):
#                 print(i, end=' ')
        
#     def inserir(self,valor):
#         if (self.ultimaPosicao == self.capacidade):
#             self.ultimaPosicao -= 1
#             print('Vetor Cheio!')
#         else:
#             self.valores[self.ultimaPosicao] = valor
#             self.ultimaPosicao += 1
        
#     def Pesquisar(self, valor):
#         if (self.ultimaPosicao == -1):
#             print('Vetor Vazio')
#         else:
#             for i in range(self.ultimaPosicao):
#                 if (self.valores[i] == valor):
#                     return i
#         return -1
        
#     def Excluir(self, valor):
#         if (self.ultimaPosicao == -1):
#             print('Vetor Vazio')
#         else:
#             posicao = self.Pesquisar(valor)
#             if (posicao == self.capacidade -1):
#                 self.ultimaPosicao -= 1
#             else:
#                 for i in range(posicao, self.ultimaPosicao):
#                     if (i != self.ultimaPosicao):
#                         self.valores[i] = self.valores[self.capacidade - i]
        
# meuVetor = VetorNaoOrdenado(4)

# meuVetor.inserir(1)
# meuVetor.inserir(2)
# meuVetor.inserir(3)
# meuVetor.inserir(4)
# meuVetor.inserir(5)

# meuVetor.imprimir()

# print('---')
# valor = meuVetor.Pesquisar(1)
# print(valor)

# meuVetor.Excluir(1)

class VetorNaoOrdenado:
    
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = [''] * capacidade
        
    def imprimir(self):
        if (self.ultimaPosicao == -1):
            print('Vetor Vazio!')
        else:
            for i in range(self.ultimaPosicao + 1):
                print(i, '-', self.valores[i])
        
    def inserir(self, valor):
        if (self.ultimaPosicao == self.capacidade - 1):
            print('Vetor Cheio!')
        else:
            self.ultimaPosicao += 1
            self.valores[self.ultimaPosicao] = valor
        
    def pesquisar(self, valor):
        if (self.ultimaPosicao == -1):
            print('Vetor Vazio!')
        else:
            for i in range(self.ultimaPosicao + 1):
                if (self.valores[i] == valor):
                    return i
            return -1
        
    def excluir(self, valor):
        if (self.ultimaPosicao == -1):
            print('Vetor Vazio!')
        else:
            posicao = self.pesquisar(valor)
            for i in range(posicao, self.ultimaPosicao):
                self.valores[i] = self.valores[i + 1]
            self.ultimaPosicao = self.ultimaPosicao -1
        

meuVetor = VetorNaoOrdenado(4)

meuVetor.inserir(1)
meuVetor.inserir(2)
meuVetor.inserir(3)
meuVetor.inserir(4)
meuVetor.inserir(5)

meuVetor.imprimir()

valor = meuVetor.pesquisar(2)
print(valor)

meuVetor.excluir(3)

meuVetor.imprimir()

### VETOR ORDENADO (esse vou direto seguindo pseudocódigo)

class VetorOrdenado:
    
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = [''] * capacidade
        
    def imprimir(self):
        if (self.ultimaPosicao == -1):
            print('Vetor Vazio!')
        else:
            for i in range(self.ultimaPosicao + 1):
                print(i, '-', self.valores[i])
        
    def inserir(self, valor):
        if (self.ultimaPosicao == self.capacidade - 1):
            print('Vetor Cheio!')
            return

        posicao = 0
        for i in range(self.ultimaPosicao + 1):
            posicao = i
            
            if (self.valores[i] > valor):
                break
            if (i == self.ultimaPosicao):
                posicao = i + 1
            
        j = self.ultimaPosicao
            
        while j >= posicao:
            self.valores[j + 1] = self.valores[j]
            j -= 1
        
        self.valores[posicao] = valor
        self.ultimaPosicao += 1
            
    def pesquisaLinear(self, valor):
        for i in range(self.ultimaPosicao + 1):
            if (self.valores[i] > valor):
                return -1

            if (self.valores[i] == valor):
                return i
            
            if (self.ultimaPosicao == i):
                return -1
        
    def pesquisaBinaria(self, valor):
        limiteInferior = 0
        limiteSuperior = self.ultimaPosicao
        
        while True:
            posicaoAtual = int((limiteInferior + limiteSuperior) / 2)
            
            #Achou
            if (self.valores[posicaoAtual] == valor):
                return posicaoAtual
            
            #N acho
            elif (limiteInferior > limiteSuperior):
                    return -1
            
            #divide os limites
            else:
                #limite inferior
                if self.valores[posicaoAtual] < valor:
                    limiteInferior = posicaoAtual + 1
                    
                #limite superior
                else:
                    limiteSuperior = posicaoAtual - 1
                
        
    def excluir(self, valor):
        posicao = self.pesquisaLinear(valor)
        if (posicao == -1):
            return -1
        else:
            for i in range(posicao, self.ultimaPosicao):
                self.valores[i] = self.valores[i + 1]
            self.ultimaPosicao -= 1
        
meuVetorOrdenado = VetorOrdenado(5)

print('----- Agora vetor ordenado ------')

meuVetorOrdenado.imprimir()

meuVetorOrdenado.inserir(1)
meuVetorOrdenado.inserir(2)
meuVetorOrdenado.inserir(5)
meuVetorOrdenado.inserir(706241345142)
meuVetorOrdenado.inserir(6)
meuVetorOrdenado.inserir(321)

meuVetorOrdenado.imprimir()

resultadoOrdenado = meuVetorOrdenado.pesquisaBinaria(706241345142)
print(resultadoOrdenado)

reusltadoNaoOrdenado = meuVetorOrdenado.pesquisaLinear(6)
print(reusltadoNaoOrdenado)

meuVetorOrdenado.excluir(6)

meuVetorOrdenado.imprimir()