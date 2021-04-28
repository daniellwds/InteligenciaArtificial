from random import *
class Pergunta:
	def __init__(self):
		self.level = [
                  ['Apresenta enxaqueca?', 'enxaqueca'],
                  ['Apresenta perda de olfato?', 'perda_de_olfato'],
                  ['Apresenta dor muscular?', 'dor_muscular'],
                  ['Apresenta tosse?', 'tosse'],
                  ['Apresenta dor de garganta?', 'dor_de_garganta'],
                  ['Apresenta dor no peito?', 'dor_no_peito'],
                  ['Apresenta sem febre?', 'sem_febre'],
                  ['Apresenta rouquidão?', 'rouquidao'],
                  ['Apresenta febre?', 'febre'],
                  ['Apresenta perda de apetite?', 'perda_de_apetite'],
                  ['Apresenta diarréia?', 'diarreia'],
                  ['Apresenta sem tosse?', 'sem_tosse'],
                  ['Apresenta fadiga?', 'fadiga'],
                  ['Apresenta confusão?', 'confusao'],
                  ['Apresenta dificuldade respiratória?', 'dificuldade_respiratoria'],
                  ['Apresenta dor abdominal?', 'dor_abdominal'],
		]

	def texto(self):
		string = self.level[0]
		del self.level[0]
		return string