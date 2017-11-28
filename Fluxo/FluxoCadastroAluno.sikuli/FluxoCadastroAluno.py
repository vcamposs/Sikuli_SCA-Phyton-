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

import Login
reload(Login)

import Uteis
reload(Uteis)

import CadastroInstrutor
reload(CadastroInstrutor)

dicionarioTempoExecucao = {}
dicionarioTempoExecucao['login'] = Login.userioLogin() 
dicionarioTempoExecucao['cadastroInstrutor'] = CadastroInstrutor.inclusao()
Uteis.fechaSCA()

print dicionarioTempoExecucao