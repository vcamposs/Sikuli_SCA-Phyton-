import time
import datetime
import os, sys
from sikuli import *
from random import*

import Uteis
reload(Uteis)

def inclusao():
    today = datetime.datetime.today()
    dataHoje = today.strftime("%d/%m/20%y")
    numeroAleatorio    = str(randint(1, 500))
    
    registro           = numeroAleatorio
    dataFiliacao       = dataHoje 
    nome               = "Nom Teste " + numeroAleatorio 
    Lic                = "123"
    dataNasc           = "01/01/1990"
    sexo               = "Masculino"
    nacionalidade      = "Brasileiro"
    naturalidade       = "Campinas"
    uf                 = "SSP"
    registroGeral      = "00.000.00-0"
    orgaoExp           = "SSP"
    cic                = "111.111.111-11"
    escolaridade       = "Superior"
    profissao          = "Analista"
    pai                = "TESTE PAI " + numeroAleatorio
    mae                = "TESTE MAE " + numeroAleatorio
    cep                = "11111-111"
    endereco           = "RUA TESTE"
    numero             = "111"
    complemento        = "TESTE COMPLEMENTO"
    bairro             = "BAIRRO TESTE"
    cidade             = "CAMPINAS" 
    uf                 = "SP"
    telefone           = "11111111111"
    celular            = "11111111111"
    email              = "TESTE@TESTE.COM" 
    anuidadePagaEm     = dataHoje 
    dadosAtualizadosEm = dataHoje   

    while not exists ("1508109556432.png"):
        wait(1)
        
    click("1508109556432.png")

    while not exists("1508109607430.png"):
        wait(1)

    type("n", Key.CTRL) ## atalho para a abertura de tela

    while not exists("1508109948890.png"):
        wait(1)

    wait(3)
    
    #paste(registro)
    Uteis.TabOrder(1,3)
     
    paste(dataFiliacao)
    Uteis.TabOrder(1,3)
    
    paste(nome)
    Uteis.TabOrder(2,3)
    
    paste(Lic)
    Uteis.TabOrder(1,3) 
    
    paste(dataNasc)
    Uteis.TabOrder(3,3)
    
    #paste(sexo)
    #paste(nacionalidade)
    
    paste(naturalidade)
    Uteis.TabOrder(2,3)
    
    #paste(uf)
    
    paste(registroGeral)
    Uteis.TabOrder(1,3)
    
    paste(orgaoExp)
    Uteis.TabOrder(1,3)
    
    paste(cic)
    Uteis.TabOrder(1,3)
    
    Uteis.DropDown(1,3) #paste(escolaridade)
    Uteis.TabOrder(1,3)
    
    Uteis.DropDown(1,3) #paste(profissao)
    Uteis.TabOrder(1,3)
    
    paste(pai)
    Uteis.TabOrder(1,3)
    
    paste(mae)
    Uteis.TabOrder(1,3)
    
    paste(cep)
    Uteis.TabOrder(1,3)
    
    paste(endereco)
    Uteis.TabOrder(1,3)
    
    paste(numero)
    Uteis.TabOrder(1,3)
    
    paste(complemento)
    Uteis.TabOrder(1,3)
    
    paste(bairro)
    Uteis.TabOrder(1,1)
    
    paste(cidade)
    Uteis.TabOrder(1,3)
    
    Uteis.DropDown(1,3) #paste(uf)
    Uteis.TabOrder(1,3)
    
    paste(telefone)
    Uteis.TabOrder(1,3)
    
    paste(celular)
    Uteis.TabOrder(1,3)
    
    paste(email)
    Uteis.TabOrder(1,5)
    
    #paste(anuidadePagaEm)
    #Uteis.TabOrder(1,5)
    
    #paste(dadosAtualizadosEm)
    #Uteis.TabOrder(1,5)

    type("f", Key.CTRL) ## salvar e fechar
    wait(3)
    type(Key.F4, KeyModifier.ALT)  
    