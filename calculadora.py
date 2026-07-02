# -*- coding: utf-8 -*-
"""Calculadora.ipynb





#Calculadora

def somar():
num1 = input('digite o primeiro número: ')
num2 = input('digite o segundo número: ')

return num1 + num2


print(somar())






#def adicao(num1, num2):
#def multiplicar(num1, num2):
#def divisao(num1,num2):


operacao = int(input('Olá, qual operação você deseja realizar hoje? digite o número do tipo da operação ex: 1 = adição, 2 = subtração, 3 = multiplicação ou 4 divisão: '))
numero1 = int(input('Digite seu primeiro número: '))
numero2 = int(input('Digite seu segundo número: '))

if operacao == 1:
  resultado = numero1 + numero2
  print(resultado)
elif operacao == 2:
  resultado = numero1 - numero2
  print(resultado)
elif operacao == 3:
  resultado = numero1 * numero2
  print(resultado)
elif operacao == 4:
  resultado = numero1 / numero2
  print(resultado)
