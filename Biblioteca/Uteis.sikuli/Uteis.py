import os
import time
import datetime
from random import*
from sikuli import *

# Indica o tempo que levou para executar certa operacão.
def delta(dataInicio,dataFim):
    dataDelta = time.strftime("%M:%S",time.localtime(dataFim - dataInicio))
    return dataDelta

# A funcão "dropDown()" foi criada para a codificação ficar mais enxuta,
# é passado o número de vezes que o comando "type(Key.DOWN)" é chamado
# incluindo o tempo de espera entre um e outro.
def dropDown(qtdDropDown, tmpWait):
    cont = 0
    while (cont <= qtdDropDown):
        type(Key.DOWN)
        wait(tmpWait)
        cont = cont + 1

# A funcão "tabOrder()" foi criada para a codificação ficar mais enxuta,
# é passado o número de vezes que o comando "type(Key.TAB)" é chamado
# incluindo o tempo de espera entre um e outro.
def tabOrder(qtdTabOrder, tmpWait):
    cont = 1
    while (cont <= qtdTabOrder):
        type(Key.TAB)
        wait(tmpWait)
        cont = cont + 1
        
# Fecha qualquer tela do sistema.
def fechaTela():
    print "[LOG] fechaTela()"
    type(Key.F4, KeyModifier.ALT)
    wait(2)

# Fecha especificamente o sistema SCA 
# pois ele apresenta uma mensagem que deve ser validada.
def fechaSCA():
    print "[LOG] fechaSCA()"
    type(Key.F4, KeyModifier.ALT)
    wait(2)

    while not exists("telaSaidaSistema.png"):
        wait(1)

    type(Key.LEFT)
    type(Key.ENTER)
    wait(5)