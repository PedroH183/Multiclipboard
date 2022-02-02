#! python3
# Use o Mcb.bat <argumento > para copiar o conteudo do argumento indicado 
# Projeto feito para simular um multiclipboard, armazena, copia e cola o texto
# salvo nos argumentos 
# @ projeto do livro "Automatize tarefas maçantes com python"


import sys
import shelve as sh
import pyperclip as py

mcbShelf = sh.open('mcbKeys','a')
# Salvar o conteudo do clipboard 
try:
    #sys.argv[0] é o path do cód
    first_arg = sys.argv[1]
    second_arg = sys.argv[2]

except IndexError:
    print("""Passe dois argumento para iniciar o multicliboard
            Example : mcb.pyw save <name of variable>""")
    sys.exit()

if first_arg == 'save':
    text_in_clip = py.paste()
    lista_chaves = list(mcbShelf.key())
    lista_chaves.append(function)
    lista_chaves[function] = text_in_clip
    print('texto copiado')
    sys.exit()


elif first_arg == 'list':
    lista_chave = py.copy(list(mcbShelf.keys()))
    print('A lista de keys foi copiado para o clipboard aqui estão elas : %s' %(lista_chave) )



# listar palavras chaves e carrega conteudo 




mcbShelf.close()
