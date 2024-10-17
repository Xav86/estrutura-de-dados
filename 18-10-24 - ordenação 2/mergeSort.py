import random

def mergeSort(lista):
    #divisão do array
    if len(lista) > 1:
        meio = len(lista) // 2

        esquerda = lista[:meio]
        direita = lista[meio:]

        mergeSort(esquerda)
        mergeSort(direita)

        i = j = k = 0

        # Ordena esquerda e direita
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            
            k += 1

        # Ordenação final
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

    return lista

random_numbers = [random.randint(0, 10000) for _ in range(1000)]

print(random_numbers)

listaReOrdenada = mergeSort(random_numbers)

print(listaReOrdenada)

names = [
    "Alice Silva", "Bruno Oliveira", "Carla Santos", "Daniel Costa", "Elisa Fernandes", "Fabio Souza", "Gabriela Lima",
    "Henrique Almeida", "Isabel Ribeiro", "João Pereira", "Karla Nogueira", "Leonardo Mendes", "Mariana Castro",
    "Nina Cardoso", "Otávio Rocha", "Patrícia Barros", "Quintino Guedes", "Rafael Martins", "Sofia Neves", "Tiago Alves",
    "Ursula Morais", "Victor Correia", "Wagner Braga", "Xavier Mendes", "Yasmin Vieira", "Zélia Figueiredo",
    "Adriana Ramos", "Bernardo Lopes", "Cecília Freitas", "Davi Borges", "Eduarda Farias", "Felipe Moreira",
    "Giovanna Carvalho", "Heitor Medeiros", "Inês Duarte", "Jorge Sales", "Kauã Pinheiro", "Larissa Santana",
    "Miguel Dias", "Natália Cruz", "Otto Camargo", "Pedro Gouveia", "Quirino Andrade", "Renata Paiva", "Samuel Araújo",
    "Tereza Maia", "Ulisses Monteiro", "Vanessa Rocha", "Willian Ribeiro", "Ximena Cardoso", "Yuri Magalhães",
    "Amanda Souza", "Bruna Ferreira", "Camila Duarte", "Diego Barbosa", "Eduardo Lima", "Fernanda Machado",
    "Giovani Costa", "Helena Silva", "Ian Farias", "Jessica Teixeira", "Kaique Araújo", "Laura Gomes", "Marcelo Vieira",
    "Nicolas Souza", "Olga Albuquerque", "Paulo Reis", "Quintino Martins", "Rodrigo Costa", "Sara Fonseca",
    "Tatiane Andrade", "Ubirajara Santos", "Vicente Tavares", "Wesley Lopes", "Xande Cruz", "Yara Morais",
    "Ágata Santos", "Breno Albuquerque", "César Teixeira", "Douglas Lima", "Emanuel Almeida", "Flávia Pinto",
    "Gustavo Cunha", "Helder Martins", "Igor Ribeiro", "Juliana Alves", "Karen Silva", "Leandro Azevedo",
    "Maitê Cardoso", "Nilson Pereira", "Oscar Ribeiro", "Patrícia Gomes", "Quintino Ferreira", "Rita Araújo",
    "Simone Costa", "Tomás Almeida", "Ursula Monteiro", "Vitor Gomes", "Wellington Alves", "Xena Ramos", "Yuri Reis",
    "Anita Silva", "Bianca Barros", "Carlos Teixeira", "Diana Costa", "Elias Martins", "Fabiana Freitas",
    "Gabriel Almeida", "Heloisa Ribeiro", "Igor Lima", "Joana Pereira", "Kléber Cardoso", "Lucas Nogueira",
    "Mara Souza", "Nelson Cunha", "Otávio Barros", "Priscila Alves", "Quirino Duarte", "Ricardo Gomes",
    "Sabrina Oliveira", "Thales Martins", "Ubiratan Vieira", "Valentina Ferreira", "Wanderley Mendes", "Xênia Lopes",
    "Yasmin Azevedo", "Aline Ramos", "Beatriz Silva", "Cristiano Cardoso", "Daniela Barros", "Eduardo Santos",
    "Fábio Freitas", "Giovana Costa", "Heitor Reis", "Isabela Lima", "Júlio Vieira", "Karina Oliveira", "Luan Ribeiro",
    "Marcela Souza", "Natasha Pereira", "Orlando Almeida", "Paola Santos", "Quirino Martins", "Roberta Mendes",
    "Sérgio Cardoso", "Tatiana Ramos", "Ulisses Martins", "Vanessa Souza", "William Ferreira", "Ximena Alves",
    "Yago Cruz", "André Almeida", "Bruno Santos", "Carla Reis", "Diego Costa", "Eduarda Souza", "Felipe Oliveira",
    "Gustavo Lima", "Helena Mendes", "Igor Cardoso", "Julia Freitas", "Karla Martins", "Leonardo Costa", "Mariana Lopes",
    "Nicolas Mendes", "Olga Souza", "Paulo Cardoso", "Quirino Barros", "Rafael Andrade", "Silvia Mendes", "Thiago Neves",
    "Ursula Teixeira", "Vitor Cardoso", "William Ribeiro", "Xênia Andrade", "Yara Costa", "Álvaro Martins", "Bárbara Souza",
    "Alexandre Braga", "Benedito Lopes", "Caio Neves", "Dalila Souza", "Emerson Oliveira", "Fernanda Barros",
    "Guilherme Teixeira", "Hugo Rocha", "Ingrid Ramos", "João Victor", "Kevin Santos", "Lívia Costa", "Marcos Freitas",
    "Neusa Alves", "Olavo Rocha", "Paulo Henrique", "Querubina Souza", "Ronaldo Nogueira", "Simone Teixeira",
    "Tales Barros", "Uliana Santos", "Vinícius Ramos"
]

print(names)

listaReOrdenadaNomes = mergeSort(names)

print(listaReOrdenadaNomes)