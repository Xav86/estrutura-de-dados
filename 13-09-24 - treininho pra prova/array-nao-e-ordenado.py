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

