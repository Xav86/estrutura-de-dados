# criar uma função onde recebe um dicionario com chaver sendo o nome e um array com as notas, a função vai calcular a média e retornar um dicionario com nome e média

def calcularMedia(alunos):
    medias = {}
    for aluno in alunos:
        notas = alunos[aluno]
        
        media = sum(notas) / len(notas)
        medias[aluno] = media
    return medias
    

dicionarioAlunos = {"Gustavo": [10, 3, 8], "Caetano": [5, 6, 2], "Calebe": [10, 9, 7]}
mediaAlunos = calcularMedia(dicionarioAlunos)
print(mediaAlunos)