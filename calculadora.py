# -*- coding: utf-8 -*-
"""Calculadora.ipynb





#Calculadora

def adicao():
num1 = float(input('digite o primeiro número: '))
num2 = float(input('digite o segundo número: '))

return num1 + num2


print(adicao())


def subtracao():
num1 = float(input('digite seu primeiro número: ')
num2 = float(input('digite seu segundo número: ')

return num1 - num2

print(subtracao())





def multiplicar():
num1 = float(input('digite seu primeiro número: '))
num2 = float(input('digite seu segundo número: 0'))

return num1 * num2

print(multiplicar())



def divisao():
num1 = float(input('digite seu primeiro número'))
num2 = float(input('digite seu sgundo número'))

return num1 / num2

print(divisao())


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
