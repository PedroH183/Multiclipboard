#! python3
# Use o Mcb.bat <argumento > para copiar o conteudo do argumento indicado 
# Projeto feito para simular um multiclipboard, armazena, copia e cola o texto
# salvo nos argumentos 
# @ projeto do livro "Automatize tarefas maçantes com python"


import sys
import shelve as sh
import pyperclip as py

mcbShelf = sh.open('mcb.pyw')
# Salvar o conteudo do clipboard 
try:
    argu = sys.argv[1]
except IndexError:
    print('Passe um argumento para iniciar o multicliboard')
    sys.exit()






# lista palavras chaves e carrega conteudo 




mcbShelf.close()
