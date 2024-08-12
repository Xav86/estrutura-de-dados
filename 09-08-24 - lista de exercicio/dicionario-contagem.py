# uma função que recebe uma string e retorna dicionário com a contagem de cada caractere

def contarCracteres(texto):
    contagem = {}
    for caractere in texto:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1
    return contagem

texto_qualquer = "letra o 2 vezes o"
resultado = contarCracteres(texto_qualquer)
print(resultado)
