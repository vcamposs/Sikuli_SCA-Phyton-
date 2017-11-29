import time
import datetime
import os, sys
from sikuli import *

import Uteis
reload(Uteis)

def userioLogin():
    # Guarda a hora que a funcão foi iniciada, 
    # posteriormente será usado para calcular o tempo que o processo levou.
    dataInicio = time.time()

    # Algumas constantes insoladas para facilitar o processo.
    strlogin = "SCA" 
    strsenha = "SCA" 
    strExecutaveSCA = "C:\Program Files (x86)\Para-quedismo\Sca\Sca.exe"

    # Inicializa a aplicacão.
    myApp = App(strExecutaveSCA)
    myApp.open()

    # Enquando não existir a imagem "telaLogin.png" aguarda 1 segundo.
    while not exists("telaLogin.png"):
        print "[LOG] Aguardando a abertura da tela de login." 
        wait(1)
        
    print "[LOG] Tela de login aberta com sucesso."

    # Inclusão de login e senha.
    paste(strlogin)
    Uteis.tabOrder(1, 0.5) # A funcão "tabOrder()" foi criada para a codificação ficar mais enxuta.
    paste(strsenha)
    Uteis.tabOrder(2, 0.5)
    type(Key.ENTER)
    
    # Após indicar o usuário e senha aguardar a abertura do sistema para prosseguir com o fluxo
    while not exists ("barraSuperiorTelaInicial.png"):
        print "[LOG] Aguardando a abertura da tela inicial do SCA." 
        wait(1)
    print "[LOG] SCA aberto com sucesso."

    # Retornado o tempo que o processo levou para ser executado, 
    # será utilizado posteriormente na classe "Relatorio.py" 
    return Uteis.delta(dataInicio, time.time())