# Você precisa implementar três classes principais: Livro, Usuario, e Biblioteca. A classe Livro representa os livros da biblioteca, a classe Usuario representa as pessoas que pegam emprestado os livros, e a classe Biblioteca gerencia o processo de empréstimo de livros.

class Livro:
    def __init__(self, titulo, autor, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel
    
    def exibirDetalhes(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Disponível: {self.disponivel}")
        
class Usuario:
    def __init__(self, nome, livrosEmprestados):
        self.nome = nome
        self.livrosEmprestados = livrosEmprestados
    
    def emprestarLivro(self):
        print('a')
        
    def devolverLivro(self):
        print('a')
        
class Biblioteca:
    def __init__(self, nome, livro: Livro):
        self.nome = nome
        self.livro = livro
        
    def adicionarLivro(self, livro):
        print('a')
        
    def exibirLivrosDisponiveis():
        print('a')
        

livrosLista = []

livrosLista.append(Livro('Livro legal', 'Gustavo', True))
livrosLista.append(Livro('Livro legal2', 'Gustavo2', False))
livrosLista.append(Livro('Livro legal3', 'Gustavo3', True))

for livro in livrosLista:
    livro.exibirDetalhes()