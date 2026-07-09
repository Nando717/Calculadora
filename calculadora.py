# -*- coding: utf-8 -*-







#Calculadora

#organizando o sistema para mudanças
#criando menu para calculadora

operacao = int(input('digite o numero da operaçao desejada: 1 adicao, 2 subtracao, 3 multipicacao, 4 divisao: '))



def adicao():
 num1 = float(input('digite o primeiro número: '))
 num2 = float(input('digite o segundo numero: '))
 return num1 + num2


def subtracao():
 num1 = float(input('digite seu primeiro número: '))
 num2 = float(input('digite seu segundo numero: ')) 
 return num1 - num2

def multiplicacao():
  num1 = float(input('digite seu primeiro número: '))
  num2 = float(input('digite seu segundo número: '))
  return num1 * num2

def divisao():
  num1 = float(input('digite seu primeiro número: '))
  num2 = float(input('digite seu segundo número: '))
  return num1 / num2

if operacao == 1:
  print(adicao())

if operacao == 2:
  print(subtracao())

if operacao == 3:
  print(multiplicacao())

if operacao == 4:
  print(divisao())
