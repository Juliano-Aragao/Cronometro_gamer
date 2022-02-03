# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 09:37:08 2022

@author: Juliano
"""
from time import sleep
import os
import winsound

   
def menu1():#  tela inicial de entrada
    os.system('cls')
    print('*'*52)
    print('*'*52)
    print('*'*10," "*30,"*"*10)
    print('*'*10," "*30,"*"*10)
    print('*'*10,"          Cronometro          ","*"*10)
    print('*'*10,"             Gamer            ","*"*10)
    print('*'*10," "*30,"*"*10)
    print('*'*10," "*30,"*"*10)
    print('*'*52)
    print('*'*10,'     Digite 1 para iniciar.   ','*'*10) 
    print('*'*52)  
    

def menu2 ():  # tela de escolha de tempo
    os.system("cls")
    print('*'*52)
    print('*'*52)
    print('*'*10," "*30,"*"*10)
    print('*'*10,"       Escolha a opção        ","*"*10)
    print('*'*10," "*30,"*"*10)
    print('*'*10,"   1 ->  30 segundo           ","*"*10)
    print('*'*10,"   2 -> 180 segundo           ","*"*10)
    print('*'*10,"   3 -> Para escolher o tempo ","*"*10)
    print('*'*10," "*30,"*"*10)
    print('*'*10," "*30,"*"*10)
    print('*'*52)
    print('*'*52)    

def menu3(): # tela encerramento da contagem
    print('*'*52)
    print('*'*52)
    print('*'*10," "*30,"*"*10)
    print('*'*10," "*30,"*"*10)
    print('*'*10,"          TIME OUT            ","*"*10)
    print('*'*10,"                              ","*"*10)
    print('*'*10,"        Aperte  Enter         ","*"*10)
    print('*'*10," "*30,"*"*10)
    print('*'*52)
    print('*'*52) 
    winsound.Beep(2100,50)    
    winsound.Beep(2300,50) 
    winsound.Beep(2700,50)    
    winsound.Beep(3300,50) 
    winsound.Beep(4700,50)    
    winsound.Beep(5300,50) 
    winsound.Beep(6700,50)    
    winsound.PlaySound("chimes.wav",winsound.SND_FILENAME) 
    input()  
          
    

def time1():  # contagem de 30 segundo
    for cont in range(10,-1,-1):
        os.system("cls") 
        print(cont,' segundos')
        sleep(1)
    os.system("cls")    
    menu3()
    
                
def time2():  # contagem de 180 segundos
    for cont in range(180,-1,-1):
        os.system("cls") 
        print(cont,' segundos')
        sleep(1) 
    os.system("cls")     
    menu3()
    
        
def time3():  # escolha da contagem      
    op = int(input('Digite o tempo desejado: '))        
    for cont in range(op,-1,-1):
        os.system("cls") 
        print(cont, " segundos")
        sleep(1)
    os.system("cls") 
    menu3()
    
    
    
            
    #inicio do programa  
inicio =True
n2 = 0
while True:
    menu1()
    n1 = int(input('  Entrar -> :'  )) 
    if n1 == 1:
        inico=False
        menu2()
        n2 = int(input('digite sua escolha:-> '))
        if n2 == 1:
            time1()
        elif n2 ==2:
            time2()    
        elif n2 ==3:
            time3()    
        elif n2 > 3:
            print( 'Digito errado')
            sleep(2)
        
   

 
   

        




       

 