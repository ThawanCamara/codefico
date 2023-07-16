def ex00():
	n = int(input("Digite um numero: "))
	if n % 2 == 0:
		print("Par!")
	else:
		print("Ímpar!")

def ex01():
	n1 = int(input("Digite o primeiro número: "))
	n2 = int(input("Digite o segundo número: "))
	if n1 == n2:
		print("Os números são iguais")
	elif n1 > n2:
		print(f"{n1} é maior que {n2}")
	else:
		print(f"{n2} é maior que {n1}")

def ex02():
	idade = int(input('Qual sua idade? '))
	min, max = 0, 1
	crianca = [0, 11]
	adolescente = [12, 17]
	adulto = [18, 59]
	idoso = [60, 2147483647]
	grupos = [crianca, adolescente, adulto, idoso]
	nome_do_grupo = ["Criança", "Adolescente", "Adulto", "Idoso"]
	for índice, grupo in enumerate(grupos):
		if idade in range(grupo[min],grupo[max]):
			print(nome_do_grupo[índice])

def ex03():
	import time

	print('Que bom ter você aqui!')
	print('Escrevendo...')
	time.sleep(4)
	NomeCliente = input('Qual seu nome? ')
	IdadeCliente = int(input('Qual sua idade? '))
	if (IdadeCliente < 20):
		print(f'Fala {NomeCliente}! Posso ajudar?')
	else:
		print(f'Olá {NomeCliente}, em que posso ser útil?')

def ex04():
	import time

	print('Que bom ter você aqui!')
	print('Escrevendo...')
	time.sleep(4)
	NomeCliente = input('Qual seu nome? ')
	print('Boa noite ' + NomeCliente + ', em que posso ser útil?')


RESET = "\033[0m"
RED = "\033[38;5;9m"
ORANGE = "\033[38;5;214m"
TEAL = "\033[38;5;14m"

max_amount = 5;
exs = [ex00, ex01, ex02, ex03, ex04]
print(f'{ORANGE}Pass 0 as argument to exit{RESET}')
while True:
	try:
		ex = int(input(f"{TEAL}Qual exercício? (1 - {max_amount})\n{RESET}"))
		if (ex == 0):
			print(f"{ORANGE}>>> Exiting <<<{RESET}")
			break
		elif 0 < ex < max_amount:
			exs[ex - 1]()
		else:
			print(f"{RED}Input must be within 1 and {max_amount}{RESET}")
	except ValueError:
		print(f"{RED}Invalid input. Please use just valid numbers{RESET}")
