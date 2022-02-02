#! python3
# Use o Mcb.bat <argumento > para copiar o conteudo do argumento indicado 
# Projeto feito para simular um multiclipboard, armazena, copia e cola o texto
# salvo nos argumentos 
# @ projeto do livro "Automatize tarefas maçantes com python"


import sys
import shelve as sh
import pyperclip as py

mcbShelf = sh.open('mcbKeys')
# Salvar o conteudo do clipboard 
try:
    #sys.argv[0] é o path do cód
    first_arg = sys.argv[1]
    second_arg = sys.argv[2]

except IndexError:
    print("""Passe dois argumento para iniciar o multicliboard
            Example : mcb.pyw save <name of variable>""")
    sys.exit()

first_options = ['save','list']
#Tratando 
if first_arg == first_options[0]:
    text_in_clip = py.paste()
    mcbShelf[str(second_arg)] = py.paste()
    print('texto copiado para a o argumento %s' %(second_arg))
    sys.exit()

# listar palavras chaves e carrega conteudo 
elif first_arg == first_options[1]:
    lista_chave = py.copy(list(mcbShelf.keys()))
    print('A lista de keys foi copiado para o clipboard aqui estão elas : %s' %(lista_chave) )

elif (first_arg not in first_options) or (first_arg in list(mcbShelf.keys())):
    py.copy = mcbShelf[first_arg]
    print('O texto salvo em %s foi copiado para o clipboard'% (mcbShelf[first_arg]))
    sys.exit()

else:
    print('algo deu errado pfv verificar')
    sys.exit()

mcbShelf.close()
