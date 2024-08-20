# Você precisa implementar três classes principais: Livro, Usuario, e Biblioteca. A classe Livro representa os livros da biblioteca, a classe Usuario representa as pessoas que pegam emprestado os livros, e a classe Biblioteca gerencia o processo de empréstimo de livros.

class Livro:
    def __init__(self, titulo, autor, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel
    
    def exibirDetalhes(self):
        print(f"Titulo: {self.titulo}, Autor: {self.autor}, Disponivel: {self.disponivel}")
        return
        
class Usuario:
    def __init__(self, nome, livrosEmprestados):
        self.nome = nome
        self.livrosEmprestados = livrosEmprestados
    
    def emprestarLivro(self):
        print('a')
        
    def devolverLivro(self):
        print('a')
        
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livro = []
        
    def adicionarLivro(self, livro):
        self.livro.append(livro)
        
    def exibirLivrosDisponiveis(self):
        for livro in self.livro:
            livro.exibirDetalhes()


biblioteca = Biblioteca("Biblioteca")

biblioteca.adicionarLivro(Livro('Livro legal', 'Gustavo', True))
biblioteca.adicionarLivro(Livro('Livro legal2', 'Gustavo2', False))
biblioteca.adicionarLivro(Livro('Livro legal3', 'Gustavo3', True))

biblioteca.exibirLivrosDisponiveis()