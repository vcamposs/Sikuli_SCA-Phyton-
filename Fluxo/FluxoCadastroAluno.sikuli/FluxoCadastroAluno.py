import time
import datetime
import os, sys
from sikuli import *

myPath = os.path.dirname(getBundlePath())
myPath = myPath.replace("Fluxo/FluxoCadastroAluno.sikuli", "")
myPath = myPath + "Biblioteca/"

importPathLib = myPath.replace("/", "\\\\")
if not importPathLib in sys.path:
    sys.path.append(importPathLib)

# Import bibliotecas
import Login 
reload(Login)
import Uteis
reload(Uteis)
import CadastroInstrutor 
reload(CadastroInstrutor)
import Relatorio 
reload(Relatorio)

try:
    dctTempoExecucao = {}
    dctTempoExecucao['login']  = Login.userioLogin() 
    dctTempoExecucao['cadastroInstrutor'] = CadastroInstrutor.inclusao()
    Uteis.fechaSCA()
    # Chamada do relatório HTML
    Relatorio.montaRelatorio(dctTempoExecucao,"SUCESSO")
    print "[Log] Processo executado com SUCESSO."
except:
    dctTempoExecucao['login']  = "--" 
    dctTempoExecucao['cadastroInstrutor'] = "--"
    # Chamada do relatório HTML
    Relatorio.montaRelatorio(dctTempoExecucao,"ERRO")
    print "[Log] Processo executado com ERRO."