import time
import datetime
import os, sys
from sikuli import *
from random import*

import Uteis
reload(Uteis)

import Gerador
reload(Gerador)

def inclusao():
    # Guarda a hora que a funcão foi iniciada, 
    # posteriormente será usado para calcular o tempo que o processo levou.
    dataInicio = time.time()

    # Abertura de tela foi isolada em uma funcão, 
    # posteriormente pode ser usada em outros processos.
    aberturaTelaDeCadastroInstrutor()

    # Atribuido a variavel "strNomeIntrutor" pois será usada como base para montar o endereco de email.
    strNomeIntrutor = Gerador.nome()

    paste(strNomeIntrutor)
    Uteis.tabOrder(2,2)

    paste(str(randint(100000, 999999)))
    Uteis.tabOrder(1,2)

    # A funcão "dropDown()" foi criada para a codificação ficar mais enxuta,
    # é passado o número de vezes que o comando "type(Key.DOWN)" é chamado
    # incluindo o tempo de espera entre um e outro.
    # É feita uma escolha randomica entre [1]C | [2]D | [3]E
    Uteis.dropDown(choice([1,2,3]),2)
    Uteis.tabOrder(1,2)
    
    #[1]"JM ASL" | [2]"JM ASL/AFF" | [3]"I ASL" | [4]"I ASL/AFF"
    Uteis.dropDown(choice([1,2,3,4]),2)
    Uteis.tabOrder(1,5)

    paste(Gerador.telefoneFixo())
    Uteis.tabOrder(1,5)

    paste(Gerador.celular())
    Uteis.tabOrder(1,5)

    # Gera o endereço de email com base no nome cadastrado.
    paste(Gerador.email(strNomeIntrutor))
    Uteis.tabOrder(1,5)

    paste("Nota cadastro instrutores")
    wait(2)

    # Fecha tela de cadastro de instrutor.
    type('f', KeyModifier.CTRL)
    wait(2)

    while exists("barraSuperiorCadastroInstrutores.png"):
        print "[LOG] Aguardando abertura da tela ..."
        wait(1)
    
    type(Key.F3)
    Uteis.fechaTela()
    wait(5)
    
    return Uteis.delta(dataInicio, time.time())

def aberturaTelaDeCadastroInstrutor():
    click(Pattern("botaoCadastroInstrutor.png").similar(0.90))
    wait(3)

    while not exists("barraSuperiorSelecaoInstrutores.png"):
        print "[LOG] Aguardando abertura da tela ..."
        wait(1)
    
    type('n', KeyModifier.CTRL)

    while not exists("barraSuperiorCadastroInstrutores.png"):
        print "[LOG] Aguardando abertura da tela ..."
        wait(1)    