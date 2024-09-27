class No:
    
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def mostrarNo(self):
        
        print(self.valor)

class ListaEncadeada:
    
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        
    def listaVazia(self):
        
        return self.primeiro == None

    def inserirInicio(self, valor):
        
        novo = No(valor)
        if (self.listaVazia()):
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo
            novo.proximo = self.primeiro
            self.primeiro = novo
        
    def inserirFinal(self, valor):
        
        novo = No(valor)
        if (self.listaVazia()):
            self.primeiro = novo
        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo
            
        self.ultimo = novo

    def mostrarInicio(self):
        
        atual = self.primeiro
        
        while atual != None:
            atual.mostrarNo()
            atual = atual.proximo
            
    def mostrarFinal(self):
        
        atual = self.ultimo
        
        while atual != None:
            atual.mostrarNo()
            atual = atual.anterior

    def pesquisar(self, valor):
        
        if (self.listaVazia()):
            print('Lista vazia')
            return None
        
        atual = self.primeiro

        while atual.valor != valor:
            if( atual.proximo == None ):
                return None
            else:
                atual = atual.proximo

        return atual

    def excluirInicio(self):
               
        temp = self.primeiro
        if (self.primeiro.proximo == None):
            self.ultimo = None
        else:
            self.primeiro.proximo.anterior = None # ta certo isso????
        
        self.primeiro = self.primeiro.proximo

        return temp
    
    def excluirFinal(self):
        
        temp = self.ultimo
        if (self.primeiro.proximo == None):
            self.primeiro = None
        else:
            self.ultimo.anterior.proximo = None # ta certo isso aqui tmb????
        
        self.ultimo = self.ultimo.anterior

        return temp

    def excluirPosicao(self, valor):
        
        atual = self.primeiro
        
        while atual.valor != valor:
            atual = atual.proximo
            
            if (atual == None):
                return None
        
        if (atual == self.primeiro):
            self.primeiro = atual.proximo
        else:
            atual.anterior.proximo = atual.proximo # e esse aqui ta certo tmb?
        
        if (atual == self.ultimo):
            self.ultimo = atual.anterior
        else:
            atual.proximo.anterior = atual.anterior
            
        return atual
            

minhaLista = ListaEncadeada()

for i in range(5):
    minhaLista.inserirInicio(i)
    
for i in range(5):
    minhaLista.inserirFinal(i)

minhaLista.mostrarInicio()
minhaLista.mostrarFinal()

minhaLista.excluirInicio()
minhaLista.excluirFinal()

print('-----')

minhaLista.mostrarInicio()

print('-----')

minhaLista.excluirPosicao(6)

minhaLista.mostrarFinal()

print('-----')

noEncontrado = minhaLista.pesquisar(7)
if (noEncontrado == None):
    print('nada aqui')
else:
    print(noEncontrado.valor)