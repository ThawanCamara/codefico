RESET = "\033[0m"
RED = "\033[38;5;9m"
PINK = "\033[38;5;13m"
ORANGE = "\033[38;5;214m"
TEAL = "\033[38;5;14m"

# Preencha um vetor X de 10 elementos inteiros e positivos. Criar um vetor Y da seguinte forma:
# Os elementos de Y com índice par receberão os respectivos elementos de X divididos por 2;
# Os elementos de Y com índice ímpar receberão os respectivos elementos de X multiplicados por 3.
# No final, imprima o vetor X e o vetor Y.
def ex00():
	print(f'{PINK}Preencha um vetor X de 10 elementos inteiros e positivos. Criar um vetor Y da seguinte forma:\nOs elementos de Y com índice par receberão os respectivos elementos de X divididos por 2;\nOs elementos de Y com índice ímpar receberão os respectivos elementos de X multiplicados por 3.\nNo final, imprima o vetor X e o vetor Y.{RESET}')
	import random
	X = []
	Y = []
	amount = int(input("Informe o tamanho do vetor: "))
	for i in range(0, amount):
		X.append(random.randint(0, 100))
	size = len(X)
	for i in range(0, size):
		if i % 2 == 0:
			Y.append(int(X[i] / 2))
		else:
			Y.append(X[i] * 3)
	print(f'Vetor X: {X}\nVetor Y: {Y}')

# Digite 10 números em um vetor e no final imprima a média, o maior e o menor número.
def ex01():
	print(f'{PINK}Digite 10 números em um vetor e no final imprima a média, o maior e o menor número.{RESET}')
	import random
	X = []
	amount = int(input("Informe o tamanho do vetor: "))
	for i in range(0, amount):
		X.append(random.randint(0, 100))
	print(f'Vetor: {X}')
	print(f'Media: {sum(X)/len(X)}\nMaior: {max(X)}\nMenor: {min(X)}')

# Criar um programa que solicita uma string e verifica se ela é um palíndromo ou não. Um palíndromo é uma string que, quando invertida, se mantém igual a original. Por exemplo: arara.
def ex02():
	print(f'{PINK}Criar um programa que solicita uma string e verifica se ela é um palíndromo ou não. Um palíndromo é uma string que, quando invertida, se mantém igual a original. Por exemplo: arara.{RESET}')
	res = ["", "não "]
	s = input("Digite uma palavra: ")
	print(f'{res[s != s[::-1]]}é um palíndromo')

# Crie um programa que armazena diversos inteiros em uma lista e depois os imprime em ordem de tamanho.
def ex03():
	print(f'{PINK}Crie um programa que armazena diversos inteiros em uma lista e depois os imprime em ordem de tamanho.{RESET}')
	import random
	X = []
	amount = int(input("Informe o tamanho do vetor: "))
	for i in range(0, amount):
		X.append(random.randint(0, 100))
	X.sort()
	print(f'Vetor: {X}')

max_amount = 4
exs = [ex00, ex01, ex02, ex03]
print(f'{ORANGE}Pass 0 as argument to exit{RESET}')
while True:
	try:
		ex = int(input(f"\n{TEAL}Qual exercício? (1 - {max_amount})\n{RESET}"))
		if (ex == 0):
			print(f"{ORANGE}>>> Exiting <<<{RESET}")
			break
		elif 0 < ex <= max_amount:
			exs[ex - 1]()
		else:
			print(f"{RED}Input must be within 1 and {max_amount}{RESET}")
	except ValueError:
		print(f"{RED}Invalid input. Please use just valid numbers{RESET}")
