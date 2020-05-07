# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:02:32 2020

@author: luano
"""

'''
DESCRITION

Jogo de Craps. Faça um programa de implemente um jogo de Craps. 
O jogador lança um par de dados, obtendo um valor entre 2 e 12. 
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. 
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". 
Seu objetivo agora é continuar jogando os dados até tirar este número novamente. 
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente

'''
# import library
import random
import os


def restart(): #restart condition
    rest = input("\n\nYES or NO\ndo you want to play again?: ")
    if rest == 'yes':
        main()
    else:
        return print("\n\nby by")

def won():  #check who won and print
    global veri1
    global veri2
    if veri1 == 1:
        print("\n%s won!!!" %player1)
        veri1 = 0   #false in variable
        restart()
        
    elif veri2 == 1:
        print("\n%s won!!!" %player2)
        veri2 = 0  #false in variable
        restart()
        
    else: print("fail!!")
    
    
    
def lost():  #check who lost and print
    global veri1
    global veri2
    if veri1 == 1:
        print("\n%s won!!!" %player1)
        veri1 = 0  #false in variable
        restart()
        
    elif veri2 == 1:
        print("\n%s won!!!" %player2)
        veri2 = 0  #false in variable
        restart()
        
    else: print("fail!!")



def score(result):  #accumulation of score with check who accumuled
    global veri1
    global veri2
    if veri1 == 1:
        score1.append(result)  #accumuted score in result list
        print("\nscore accumulated")
        print("\nscore of %s is %d\n\n\n" %(player1,sum(score1)))
        veri1 = 0  #false variable
        second()  #return second pleyes

    elif veri2 == 1:
        score2.append(result)  #accumuled score in result list
        print("\nscore accumulated")
        print("\nscore of %s is %d\n\n\n" %(player2,sum(score2)))
        veri2 = 0  #false varible
        first()  #return first player
    
    else: print("fail!!")
        
    
def first():  #sequence of player(first)
    global veri1
    if k == 0:
        print('\n%s plays' %player1)
        act = input('press enter to play')
        if act == "":  #press enter to start
            number = random.sample(range(1,7),2) #generate two random number
            result = sum(number) #sum of the two numbers
            print(result)
            if result == 7 or result == 11:  #if equal numbers
                veri1 = 1  #True variable
                won()
            elif result == 2 or result == 3 or result == 12: #if equal numbers
                veri1 = 1  #true variable
                lost()
            else:  #if not equal numbers, acuumuted
                veri1 = 1
                score(result)
            
        

def second(): #sequence of player(second) check descrition in def first()
    global veri2
    if i == 0:
        print('\n%s plays' %player2)
        act = input('press enter to play')
        if act == "":
            number = random.sample(range(1,7),2)
            result = sum(number)
            print(result)
            if result == 7 or result == 11:
                veri2 = 1
                won()
            elif result == 2 or result == 3 or result == 12:
                veri2 = 1
                lost()
            else:
                veri2 = 1
                score(result)

def main(): #start game
    global k  #define global variables
    global i
    global veri1
    global veri2
    global number
    global score1
    global score2
    global player1
    global player2
    print("*************** JOGO CRAPS ***********************")
    
    player1 = input("enter the name of the first player: ") #define name players
    player2 = input("enter the name of the second player: ")

    # starting variables
    k = 0  
    i = 0
    veri1 = 0
    veri2 = 0
    number = []
    score1 = []
    score2 = []
    first()

#start game
main()