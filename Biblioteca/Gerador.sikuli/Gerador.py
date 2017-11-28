import time
from datetime import datetime, timedelta
import os, sys
from sikuli import *
from random import*

def nome():  
    
    listaNomesMasculinos = ["Diogo","Enzo","Guilherme","Kauan","Luiz",
                            "Martim","Murilo","Rodrigo","Samuel","Victor"]
          
    listaNomesFemininos  = ["Agatha","Aline","Anna","Julia","Paula",
                            "Raisa","Mariana", "Marina","Claudia","Neusa"]
    
    listaSobrenomes      = ["Alves","Carvalho","Cunha","Pereira","Costa",
                            "Dias","Azevedo","Araujo","Ribeiro","Cardoso",
                            "Oliveira","Cavalcanti","Tula","Ferreira ","Rodrigues",
                            "Goncalves","Dias","Oliveira","Alves","Araujo",
                            "Azevedo","Barbosa","Cardoso ","Carvalho","Costa",
                            "Cunha","Dias","Goncalves","Oliveira","Pereira",
                            "Ribeiro","Rodrigues","Tula","Pecci","Nupe"] 

    tipoGenero = choice(["MASCULINO","FEMININO"])
            
    if (tipoGenero == "MASCULINO") :
        listaNomes = listaNomesMasculinos 
    elif (tipoGenero == "FEMININO"):
        listaNomes = listaNomesFemininos    
    
    strNome         = choice(listaNomes)
    strSobrenome_01 = choice(listaSobrenomes)
    strSobrenome_02 = choice(listaSobrenomes)

    strNomeSobrenome = strNome + " " + strSobrenome_01 + " " + strSobrenome_02

    return strNomeSobrenome

def data(qtdDias):
    dataHoje       = datetime.today()
    dataSolicitada = datetime.fromordinal(dataHoje.toordinal() + qtdDias)
    strData        = dataSolicitada.strftime("%d/%m/%Y")

    return strData

def telefoneFixo():
    strNumeroTelefoneFixo = "(019)32" + str(randint(10,99)) + "-" + str(randint(1000,9999))
    return strNumeroTelefoneFixo

def celular():
    strNumeroCelular = "(019)99" + str(randint(10,99)) + "-" + str(randint(1000,9999))
    return strNumeroCelular

def email(strNome):
    strEmail = strNome.replace(" ",".") + "@" + choice(["gmail","hotmail","academia123"]) + ".com"
    return strEmail