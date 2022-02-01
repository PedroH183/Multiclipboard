#! python3
# Use o Mcb.bat <argumento > para copiar o conteudo do argumento indicado 
# Projeto feito para simular um multiclipboard, armazena, copia e cola o texto
# salvo nos argumentos 


import sys
import shelve as sh
import pyperclip as py

myfile = sh.open('mcb.pyw')

