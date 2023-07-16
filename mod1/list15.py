RESET = "\033[0m"
RED = "\033[38;5;9m"
PINK = "\033[38;5;13m"
ORANGE = "\033[38;5;214m"
TEAL = "\033[38;5;14m"

# Faça um programa que mostre a tabuada(de 1 a 10) de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
# O programa deve realizar as seguintes etapas:
# - Solicitar ao usuário que digite um número inteiro positivo.
# - Verificar se o número digitado é negativo. Se for, interromper o programa..
# - Se o número for positivo, calcular e exibir a tabuada desse número.
# - Voltar ao passo 1 e repetir o processo até que um número negativo seja digitado.
def ex00():
	print(f'{PINK}Faça um programa que mostre a tabuada(de 1 a 10) de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.\nO programa deve realizar as seguintes etapas:\n - Solicitar ao usuário que digite um número inteiro positivo.\n - Verificar se o número digitado é negativo. Se for, interromper o programa..\n - Se o número for positivo, calcular e exibir a tabuada desse número.\n - Voltar ao passo 1 e repetir o processo até que um número negativo seja digitado.{RESET}')
	while True:
		n = int(input("Digite um número: "))
		if n < 0:
			break
		for i in range(0, 11):
			print(f'{n} x {i} = {n * i}')

# Desenvolva um programa que receba como entrada 10 números digitados pelo usuário. Em seguida, o programa deve calcular e exibir o menor e o maior valor dentre os números fornecidos.
# O programa deve solicitar ao usuário que digite os números e, em seguida, realizar a comparação para encontrar o menor e o maior valor. Por fim, exibirá os resultados encontrados
# O programa deve realizar as seguintes etapas:
# - Inicialize as variáveis menor_numero e maior_numero com valores extremos, como o maior número possível e o menor número possível, respectivamente.
# - Crie um loop que irá iterar 10 vezes para ler os 10 números digitados pelo usuário.
# - Dentro do loop, solicite ao usuário que digite um número.
# - Verifique se o número digitado é menor que menor_numero ou se é maior que maior_numero. Se for, atualize o valor de menor_numero e o maior_numero.
# - Exiba o menor número encontrado e o maior número encontrado.
def ex01():
	print(f'{PINK}Desenvolva um programa que receba como entrada 10 números digitados pelo usuário. Em seguida, o programa deve calcular e exibir o menor e o maior valor dentre os números fornecidos.\nO programa deve solicitar ao usuário que digite os números e, em seguida, realizar a comparação para encontrar o menor e o maior valor. Por fim, exibirá os resultados encontrados\nO programa deve realizar as seguintes etapas:\n - Inicialize as variáveis menor_numero e maior_numero com valores extremos, como o maior número possível e o menor número possível, respectivamente.\n - Crie um loop que irá iterar 10 vezes para ler os 10 números digitados pelo usuário.\n - Dentro do loop, solicite ao usuário que digite um número.\n - Verifique se o número digitado é menor que menor_numero ou se é maior que maior_numero. Se for, atualize o valor de menor_numero e o maior_numero.\n - Exiba o menor número encontrado e o maior número encontrado.{RESET}')
	import sys
	menor = sys.maxsize
	maior = -sys.maxsize - 1
	for i in range(10):
		n = int(input("Digite um número: "))
		menor =  n * (n < menor) + menor * (not n < menor)
		maior =  n * (n > maior) + maior * (not n > maior)
	print(f'Menor: {menor}\nMaior: {maior}')

# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [51-75] e [76-100] e quantos estão fora destes intervalos. A entrada de dados deverá terminar quando for lido um número negativo.
# O programa deve realizar as seguintes etapas:
# - inicialize as variáveis contador_intervalo1, contador_intervalo2, contador_intervalo3 e contador_fora como 0.
# - Inicie um loop que continuará enquanto o número lido for positivo.
# - Leia um número do usuário.
# - Verifique se o número é negativo. Se for, saia do loop.
# - Verifique em qual intervalo o número se enquadra e incremente o contador correspondente.
# - Retorne ao passo 3.
# - Exiba a contagem de números em cada intervalo. Encerre o programa.
def ex02():
	print(f'{PINK}Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [51-75] e [76-100] e quantos estão fora destes intervalos. A entrada de dados deverá terminar quando for lido um número negativo.\nO programa deve realizar as seguintes etapas:\n - inicialize as variáveis contador_intervalo1, contador_intervalo2, contador_intervalo3 e contador_fora como 0.\n - Inicie um loop que continuará enquanto o número lido for positivo.\n - Leia um número do usuário.\n - Verifique se o número é negativo. Se for, saia do loop.\n - Verifique em qual intervalo o número se enquadra e incremente o contador correspondente.\n - Retorne ao passo 3.\n - Exiba a contagem de números em cada intervalo.\n - Encerre o programa.{RESET}')
	from enum import Enum
	class Cont(Enum):
		FST = 0
		SND = 1
		TRD = 2
		OUT = 3
	contador = [0, 0, 0, 0]
	n = 0
	while True:
		n = int(input("Digite um número: "))
		if n < 0:
			break
		contador[Cont.FST.value] += n >= 0 and n <= 25
		contador[Cont.OUT.value] += n >= 26 and n <= 50
		contador[Cont.SND.value] += n >= 51 and n <= 75
		contador[Cont.TRD.value] += n >= 76 and n <= 100
		print(f'Intervalo 1: {contador[Cont.FST.value]}\nIntervalo 2: {contador[Cont.SND.value]}\nIntervalo 3: {contador[Cont.TRD.value]}\nFora dos Intervalos: {contador[Cont.OUT.value]}')

def ex03():
	print(f'{PINK}{RESET}')

def ex04():
	print(f'{PINK}{RESET}')

max_amount = 5
exs = [ex00, ex01, ex02, ex03, ex04]
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
