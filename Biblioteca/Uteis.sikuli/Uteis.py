import os
import time
import datetime
from random import*
from sikuli import *

def delta(dataInicio,dataFim):
    dataDelta = time.strftime("%M:%S",time.localtime(dataFim - dataInicio))
    return dataDelta

def dropDown(qtdDropDown, tmpWait):
    cont = 0
    while (cont <= qtdDropDown):
        type(Key.DOWN)
        wait(tmpWait)
        cont = cont + 1

def tabOrder(qtdTabOrder, tmpWait):
    cont = 1
    while (cont <= qtdTabOrder):
        type(Key.TAB)
        wait(tmpWait)
        cont = cont + 1

def fechaTela():
    print "[LOG] fechaTela()"
    type(Key.F4, KeyModifier.ALT)
    wait(2)
    
def fechaSCA():
    print "[LOG] fechaSCA()"
    type(Key.F4, KeyModifier.ALT)
    wait(2)

    while not exists("telaSaidaSistema.png"):
        wait(1)

    type(Key.LEFT)
    type(Key.ENTER)
    wait(5)