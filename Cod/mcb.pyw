#! python3
# Projeto feito para simular um multiclipboard, armazena, copia e cola 
# o texto salvo nos argumentos 
# Use py.exe mcb.pyw <argumento 1 > <argumento 2>
# argumentos 1 valido == save, paste e list, 
# caso o argumento seja list não é necessário um outro argumento



import sys
import shelve as sh
import pyperclip as py

mcbShelf = sh.open('mcbKeys')

def erro():
    print(
        f"""Digite um argumento válido na entrada do programa
        
            Example: mcb.pyw <argument> <argument optional>
                     save <key>- two arguments 
                     paste <key>- two arguments
                     list - one argument
                     remove <key>- two arguments""")
    sys.exit()

def one_arguments(argv1):
    if argv1 == 'list':
        chaves = mcbShelf.keys()
        chaves = str(list(chaves))
        if len(chaves)<1:
            print('não há keys armazenadas')
        else:
            py.copy(chaves)
            print('A lista de keys foi copiado para o clipboard aqui estão elas : %s' %(chaves) )
    else:
        erro()
    # return é necessário para fechar o shelf 
    return 


def two_arguments(argv1,argv2):
    if argv1 == 'save':
        text_in_clip = py.paste()
        mcbShelf[argv2] = text_in_clip
        print('texto salvo para a o argumento %s' %(argv2))

    elif argv1 == 'paste':
        py.copy(mcbShelf[argv2])
        print('O texto referente a key %s foi copiado para o clipboard' % (argv1) )

    elif argv1 == 'rm':
        del mcbShelf[argv2]
        print('o texto salvo em %s foi apagado junto de sua key'% (argv2) )

    else:
        erro()
    # return é necessário para fechar o shelf 
    return

first_argv = sys.argv[1]
#argumentos validos
list_of_options = ['save','list','paste','rm']

# Testando a entrada de valores
if first_argv in list_of_options:
    pass
else:
    erro()
#tentando rodar com dois argumentos
try:
    second_argv = sys.argv[2] # nome da variavel 
    if second_argv in list_of_options:
        pass
    else:
        erro()
    two_arguments(first_argv,second_argv)

# programa rodando com apenas um argumento
except IndexError:
    one_arguments(first_argv)


mcbShelf.close()
sys.exit()