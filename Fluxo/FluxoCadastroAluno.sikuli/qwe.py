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

# Chamada fluxo
dctTempoExecucao = {}
dctTempoExecucao['login']  = Login.userioLogin() 
dctTempoExecucao['cadastroInstrutor'] = CadastroInstrutor.inclusao()
Uteis.fechaSCA()

print "-- Tempo Execução --"
print "Login : " + dctTempoExecucao['login']
print "Cadastro Instrutor : " + dctTempoExecucao['cadastroInstrutor'] 

#[2do]