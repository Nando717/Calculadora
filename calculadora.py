# -*- coding: utf-8 -*-







#Calculadora

#organizando o sistema para mudanças
#criando menu para calculadora

from funcoes import adicao,subtracao,multiplicacao,divisa








operacao = int(input('digite o numero da operaçao desejada: 1 adicao, 2 subtracao, 3 multipicacao, 4 divisao: '))


if operacao == 1:
  print(adicao())

if operacao == 2:
  print(subtracao())

if operacao == 3:
  print(multiplicacao())

if operacao == 4:
  print(divisao())
