#! python3
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
            Example : mcb.pyw <argument> <argument optional>
            <arguments> = save,list or paste
            <argument optional> = name of variable for save
            save - two arguments 
            paste - two arguments
            list - one argument""")
    sys.exit()

def one_arguments(argv1):
    if argv1 == 'list':
        chaves = mcbShelf.keys()
        chaves = str(list(chaves))
        py.copy(chaves)
        print('A lista de keys foi copiado para o clipboard aqui estão elas : %s' %(chaves) )
    else:
        erro()
    
    return 


def two_arguments(argv1,argv2):
    if argv1 == 'save':
        text_in_clip = py.paste()
        mcbShelf[argv2] = text_in_clip
        print('texto salvo para a o argumento %s' %(argv2))

    elif argv1 == 'paste':
        py.copy(mcbShelf[argv2])
        print('O texto referente a key %s foi copiado para o clipboard' %(argv1))
    else:
        erro()

    return

first_argv = sys.argv[1]
list_of_options = ['save','list','paste']

if first_argv in list_of_options:
    pass
else:
    erro()

try:
    #tentando rodar com dois argumentos
    second_argv = sys.argv[2] # nome da variavel 
    two_arguments(first_argv,second_argv)

except IndexError:
    ##só foi detectado um argumento rodando como consulta!!
    # programa rodando com apenas um argumento
    one_arguments(first_argv)


mcbShelf.close()
sys.exit()