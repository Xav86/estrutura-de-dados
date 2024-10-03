# recebe numero e fala quantos tem

def contagem(numero):
    
    print(numero)
    if (numero == 0):
        return 0
    else:
        return 1 + contagem(numero // 10)
        
    
digitos = contagem(54321)
print(digitos)