#! python3
# Use o Mcb.bat <argumento > para copiar o conteudo do argumento indicado 
# Projeto feito para simular um multiclipboard, armazena, copia e cola o texto
# salvo nos argumentos 
# @ projeto do livro "Automatize tarefas maçantes com python"


import sys
import shelve as sh
import pyperclip as py

mcbShelf = sh.open('mcbKeys')
#Tratando entrada de argumentos 

def erro():
    print(
        f"""Digite um argumento válido na entrada do programa
            Example : mcb.pyw <argument> <argument optional>""")
    sys.exit()

def one_arguments(argv1,options):
    if argv1 == options[1]:
        lista_chave = py.copy(list(mcbShelf.keys()))
        print('A lista de keys foi copiado para o clipboard aqui estão elas : %s' %(lista_chave) )

    elif argv1 == options[2]:
        py.copy(mcbShelf[argv1])
        print('O texto referente a key %s foi copiado para o clipboard' %(argv1))
    
    else:
        erro()
    
    return 


def two_arguments(argv1,argv2, options):
    if argv1 == options[1]:
        text_in_clip = py.paste()
        mcbShelf[str(argv2)] = text_in_clip
        print('texto salvo para a o argumento %s' %(argv2))
        

    elif argv1 == options[2]:
        lista_chave = py.copy(list(mcbShelf.keys()))
        print('A lista de keys foi copiado para o clipboard aqui estão elas : %s' %(lista_chave) )

    else:
        erro()
        
    return

first_argv = sys.argv[1]
try:
    #tentando rodar com dois argumentos
    list_of_options = ['save','list']
    second_argv = sys.argv[2]
    two_arguments(first_argv,second_argv, list_of_options)


except IndexError:
    ##só foi detectado um argumento rodando como consulta!!
    # programa rodando com apenas um argumento
    list_of_options = ['list','consulta'] 
    one_arguments(first_argv, list_of_options)


mcbShelf.close()
sys.exit()