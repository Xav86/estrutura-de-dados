# triangulo

def triangulo(valor):
    
    if(valor == 0):
        return
    
    triangulo(valor - 1)
    
    print('*' * valor)
    
triangulo(5)