#Curso Técnico de Informática
#Autor: João Victor
#Data de início: 02/12/2021
#Término: 08/12/2021 - Sets
#Atividade009 - letra c

# Importando biblíoteca
import os


# Limpando terminal
os.system('cls')

# Título
print('-'*80)
print('Biblioteca de livros')
print('='*80)

# Livros na biblioteca
livros = {'O pequeno príncipe', 'Sherlok holmes', 'harry-poter'}

print(f'Os livros da biblioteca: {livros}')
print()

# Adicionando novos livros 
livros.add('O mágico de oz')

print(f'Biblioteca com livro novo: {livros}')
print('-'*80)

# Adicionando tempo para ler o livro
tempo1 = {'2 meses'}

for tempo in tempo1:
    print('tempo para ler o livro:')
    print(tempo, end=' ')
    print()
    print('-'*80)

# Dicas de livros 
tipoLivro = {'ação', 'Romance'}

# Saída
print(f'Com os estilos de livro anteriores: {tipoLivro}')
tipoLivro.update(['Aventura', 'Terror'])
print(f'Com os estilos de livros atualizados: {tipoLivro}')
print()
