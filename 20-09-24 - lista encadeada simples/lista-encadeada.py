class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostrarNo(self):
        print(self.valor)

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def inserirInicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        if (self.primeiro == None):
            print('Lista Vazia')
            return None

        atual = self.primeiro
        while atual != None:
            atual.mostrarNo()
            atual = atual.proximo

    def pesquisar(self, valor):
        if (self.primeiro == None):
            print('Lista Vazia')
            return None
        
        atual = self.primeiro

        while atual.valor != valor:
            if( atual.proximo == None ):
                return None
            else:
                atual = atual.proximo

        return atual

    def excluirInicio(self):
        if (self.primeiro == None):
            print('Lista vazia')
            return None
        
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo

        return temp

    def excluirPosicao(self, valor):
        if (self.primeiro == None):
            print('Lista vazia')
            return None
        
        atual = self.primeiro
        anterior = self.primeiro

        while atual.valor != valor:
            if(atual.proximo == None):
                return None
            else:
                anterior = atual
                atual = atual.proximo

        if(atual == self.primeiro):
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo
        
        return atual


minhaLista = ListaEncadeada()


# for i in range(10):
#     minhaLista.inserirInicio(i)

# minhaLista.mostrar()

# minhaLista.excluirInicio()

# print('-----')

# minhaLista.mostrar()

# print('-----')

# minhaLista.excluirPosicao(6)

# minhaLista.mostrar()

# print('-----')

# noEncontrado = minhaLista.pesquisar(24324)
# if (noEncontrado == None):
#     print('nada aqui')
# else:
#     print(noEncontrado.valor)

# NUMERO 1

# A
meuNome = 'Gustavo' 

for i in meuNome:
    minhaLista.inserirInicio(i)
    minhaLista.mostrar()

print('---')

# B
minhaLista.mostrar()

# C
# minhaLista.excluirInicio()

print('---')

# D
minhaLista.mostrar()

# E
noEncontrado = minhaLista.pesquisar('o')
if (noEncontrado == None):
    print('nada aqui')
else:
    print(noEncontrado.valor)

# F
minhaLista.excluirPosicao(4)

print('---')

minhaLista.mostrar()

# NUMERO 2
#docs

# NUMERO 3
#docs
 
# NUMERO 4
# no método inserirInicio

# NUMERO 5
# nó?

# NUMERO 6
# se o primeiro elemento for = None

# NUMERO 7
# se o proximo valor for igual a None 
