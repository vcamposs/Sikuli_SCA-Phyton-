#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
from sikuli import *

# Monta relatório em HMTML usando o "Materialize CSS"
def montaRelatorio(dctTempoExecucao,strStatus):
    
    arquivoHTML = open('C:\\GitHub\\Sikuli_SCA\\Arquivos\\RelatorioSikuli\\index.html','w')
    
    conteudoHTML = (
    "<!DOCTYPE html>" + "\n" + 
    "<html>" + "\n" +
    "<head>" + "\n" +
    "<meta charset="'"utf-8"'" />" + "\n" +
    "<link href="'"http://fonts.googleapis.com/icon?family=Material+ "\n" +Icons"'" rel="'"stylesheet"'">" + "\n" +
    "<link type="'"text/css"'" rel="'"stylesheet"'" href="'"css/materialize.min.css"'" media="'"screen,projection"'" />" + "\n" +
    "<title>Testes Automatizados</title>" + "\n" +
    "<meta name="'"viewport"'" content="'"width=device-width, initial-scale=1.0"'" />" + "\n" +
    "</head>" + "\n" +
    "<body>" + "\n" +
    "<header>" + "\n" +
    "<nav>" + "\n" +
    "<div class="'"nav-wrapper"'"><a href="'"index.html"'" class="'"brand-logo"'">[+] Relatorio SIKULI</a></div>" + "\n" +
    "</nav>" + "\n" +
    "</header>" + "\n" +
    "<div class="'"container"'">" + "\n" +
    "<p class="'"z-depth-5"'">" + "\n" +
    "<div class="'"card"'">" + "\n" +
    "<div class="'"card-content black-text"'">" + "\n" +
    "<table>" + "\n" +
    "<thead>" + "\n" +
    "<tr>" + "\n" +
    "<th>Processo</th>" + "\n" +
    "<th>Tempo</th>" + "\n" +
    "</tr>" + "\n" +
    "</thead>" + "\n" +
    "<tbody>" + "\n" +
    "<tr>" + "\n" +
    "<td>" + "Login : " + "</td>" + "\n" +
    "<td>" + dctTempoExecucao['login'] + "</td>" + "\n" +
    "</tr>" + "\n" +
    "<tr>" + "\n" +
    "<td>" + "Cadastro Instrutor : " + "</td>" + "\n" +
    "<td>" + dctTempoExecucao['cadastroInstrutor'] + "</td>" + "\n" +
    "</tr>" + "\n" +
    "</tbody>" + "\n" +
    "</table>" + "\n" +
    "</p>" + "\n" +
    "</div>" + "\n" +
    "</div>" + "\n" +
    #Status é passado como ferencia para indicar se o processo ocorreu com SUCESSO ou ERRO        
    linhaStatus(strStatus) + "\n" +
    "</div>" + "\n" +
    "</body>" + "\n" +
    "</html>")
     
    arquivoHTML.write(conteudoHTML)
    arquivoHTML.close()

    wait(5)
    aberturaRelatorioChrome()

# Gerada a linha que indica no HTML se o processo ocorreu com SUCESSO ou ERRO
def linhaStatus(strStatus):
    if(strStatus=="SUCESSO"):   
        strLinhaStatus = "<span class="'"new badge green"'">Processo efetuado com SUCESSO | </span>"
    elif(strStatus=="ERRO"):
        strLinhaStatus = "<span class="'"new badge red"'">Processo efetuado com ERRO | </span>"
    return strLinhaStatus 

# Chrome é aberto para exibir o relatório HTML.
def aberturaRelatorioChrome():
    strChrome = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    strCaminhoRelatorio = "C:/GitHub/Sikuli_SCA/Arquivos/RelatorioSikuli/index.html"
    
    #Inicializa o Chrome. 
    myApp = App(strChrome)
    myApp.open()  
    wait(5)

    # Insere o caminho na barra de endereco.
    type("t", Key.CTRL)
    paste(strCaminhoRelatorio)
    type(Key.ENTER)

    # Maximiza a tela.
    type(Key.F11)
    wait(2)