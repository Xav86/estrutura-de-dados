# Você precisa implementar três classes principais: Livro, Usuario, e Biblioteca. A classe Livro representa os livros da biblioteca, a classe Usuario representa as pessoas que pegam emprestado os livros, e a classe Biblioteca gerencia o processo de empréstimo de livros.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
    
    def exibirDetalhes(self):
        print(f"Titulo: {self.titulo}, Autor: {self.autor}, Disponivel: {self.disponivel}")
        
class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livrosEmprestados = []
    
    def emprestarLivro(self, livro):
        if (livro.disponivel):
            self.livrosEmprestados.append(livro)
            livro.disponivel = False
        else:
            print(f'O livro {livro.titulo} não esta disponivel')
        
    def devolverLivro(self, livro):
        if (livro.disponivel == False):
            self.livrosEmprestados.remove(livro)
            livro.disponivel = True
        
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
        
    def adicionarLivro(self, livro):
        self.livros.append(livro)
        
    def exibirLivrosDisponiveis(self):
        for livro in self.livros:
            if (livro.disponivel):
                livro.exibirDetalhes()



l1 = Livro('Livro legal', 'Gustavo')
l2 = Livro('Livro legal2', 'Gustavo2')
l3 = Livro('Livro legal3', 'Gustavo3')

biblioteca = Biblioteca("Biblioteca")

biblioteca.exibirLivrosDisponiveis()

biblioteca.adicionarLivro(l1)
biblioteca.adicionarLivro(l2)
biblioteca.adicionarLivro(l3)

u1 = Usuario("coisa")
u1.emprestarLivro(l1)
u1.emprestarLivro(l1)

biblioteca.exibirLivrosDisponiveis()