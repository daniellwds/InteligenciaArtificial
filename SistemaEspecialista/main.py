from classDiagnostico import *
from classPerguntas import *

#Inferência
se = Diagnostico()
pergunta = Pergunta()

while se.probabilidade() not in [0, 100]:
	string = pergunta.texto()
	
	se.pergunta(string[0],string[1])
	
	print('Probabilidade: %d' %(se.probabilidade()))
	
	print('Possibilidades: ', [level.replace('_', ' ') for level in se.resultado ], '\n')
	
	if se.probabilidade() == 100:
		print('O diagnóstico é: ', se.resultado[0].replace('_', ' '))

	elif se.probabilidade() == 0:
		print('Não apresenta diagnóstico definido')