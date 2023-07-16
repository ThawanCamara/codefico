RESET = "\033[0m"
RED = "\033[38;5;9m"
PINK = "\033[38;5;13m"
ORANGE = "\033[38;5;214m"
TEAL = "\033[38;5;14m"

# Implemente um programa para ler a quantidade de lados q (um numero inteiro) de um poĺıgono regular, e a medida do lado L(um numero real), classificar o polıgono, calcular e imprimir o valor da área (A, com duas casas decimais), conforme as descricões a seguir:
# q < 3: "Não é um polígono";
# q = 3: "triângulo" com área: A = (L^2 * √3) / 4;
# q = 4: "quadrado" com área: A = L^2;
# q = 5: "pentágono" com área: A = (5 * L^2) / (4 * tan(0.6283));
# q = 6: "hexágono" com área: A = (3 * L^2 * √3) / 2;
# q > 6: "Polígono não identificado".
def ex00():
	print(f'{PINK}Implemente um programa para ler a quantidade de lados q (um numero inteiro) de um poĺıgono regular, e a medida do lado L(um numero real), classificar o polıgono, calcular e imprimir o valor da área (A, com duas casas decimais), conforme as descricões a seguir:\nq < 3: "Não é um polígono";\nq = 3: "triângulo" com área: A = (L^2 * √3) / 4;\nq = 4: "quadrado" com área: A = L^2;\nq = 5: "pentágono" com área: A = (5 * L^2) / (4 * tan(0.6283));\nq = 6: "hexágono" com área: A = (3 * L^2 * √3) / 2;\nq > 6: "Polígono não identificado"{RESET}')
	import math
	def triangle(L):
		return ((L * L) * math.sqrt(3)) / 4
	def square(L):
		return L * L
	def penta(L):
		return (5 * (L * L)) / (4 * math.tan(0.6283))
	def hexa(L):
		return (3 * (L * L) * math.sqrt(3)) / 2
	
	msg = ["Não é um polígono", "Triângulo", "Quadrado", "Pentágono", "Hexágono", "Polígono não identificado"]
	funcs = [triangle, square, penta, hexa]
	q = int(input("Digite a quantidade de lados: "))
	if (q < 3):
		print(msg[0])
	elif (3 <= q < 7):
		L = float(input("Digite o tamanho do lado: "))
		A = funcs[q - 3](L)
		print(f"{msg[q - 2]} com área: {A:.2f}")
	else:
		print(msg[5])

# Escreva um programa que leia um número inteiro e verifique se ele é divisível por 2 e por 3.
# Caso seja, exiba a mensagem "O número é divisível por 2 e por 3".
# Caso contrário, se for divisível apenas por 2, exiba a mensagem "O número é divisível por 2, mas não por 3".
# Caso não seja divisível por 2, exiba a mensagem "O número não é divisível por 2".
def ex01():
	print(f'{PINK}Escreva um programa que leia um número inteiro e verifique se ele é divisível por 2 e por 3.\nCaso seja, exiba a mensagem "O número é divisível por 2 e por 3".\nCaso contrário, se for divisível apenas por 2, exiba a mensagem "O número é divisível por 2, mas não por 3".\nCaso não seja divisível por 2, exiba a mensagem "O número não é divisível por 2".{RESET}')
	n = int(input("Digite um número: "))
	msg = ["O número é divisível por 2",
		"O número não é divisível por 2",
		" e por 3.",
		", mas não por 3.",
		"."]
	n2 = n % 2 != 0
	n3 = n % 3 != 0
	# 'n3 + 2' cria o deslocamento
	# '1 - n2' anula as duas mensagens de 3 caso 2 seja inválido [1 - 1]
	# '4 * n2' só possui valor significativo se 2 der erro. Nesse caso joga a segunda mensagem para "."
	print(f"{msg[n2]}{msg[(n3 + 2) * (1 - n2) + (4 * n2)]}")

# Escreva um programa que leia um número inteiro e verifique se ele está no intervalo de 50 a 100, inclusive. Se o número estiver nesse intervalo, exiba a mensagem "O número está entre 50 e 100". Caso contrário, exiba a mensagem "O número não está entre 50 e 100".
def ex02():
	print(f'{PINK}Escreva um programa que leia um número inteiro e verifique se ele está no intervalo de 50 a 100, inclusive. Se o número estiver nesse intervalo, exiba a mensagem "O número está entre 50 e 100". Caso contrário, exiba a mensagem "O número não está entre 50 e 100".{RESET}')
	msg = ["não ", ""]
	print(f"O número {msg[50 <= int(input('Digite um número: ')) <= 100]}está entre 50 e 100")

# Escreva um programa que leia o peso e a altura de uma pessoa e calcule seu IMC. Em seguida, exiba a classificação do IMC de acordo com a tabela a seguir:
# IMC abaixo de 18.5: Abaixo do peso
# IMC entre 18.5 e 24.9: Peso normal
# IMC entre 25.0 e 29.9: Sobrepeso
# IMC entre 30.0 e 34.9: Obesidade grau 1
# IMC entre 35.0 e 39.9: Obesidade grau 2
# IMC acima de 40.0: Obesidade grau 3 (mórbida)
# Cálculo IMC:
# O índice é calculado da seguinte maneira: divide-se o peso do paciente pela sua altura elevada ao quadrado
def ex03():
	print(f'{PINK}Escreva um programa que leia o peso e a altura de uma pessoa e calcule seu IMC. Em seguida, exiba a classificação do IMC de acordo com a tabela a seguir:\nIMC abaixo de 18.5: Abaixo do peso\nIMC entre 18.5 e 24.9: Peso normal\nIMC entre 25.0 e 29.9: Sobrepeso\nIMC entre 30.0 e 34.9: Obesidade grau 1\nIMC entre 35.0 e 39.9: Obesidade grau 2\nIMC acima de 40.0: Obesidade grau 3 (mórbida)\nCálculo IMC:\nO índice é calculado da seguinte maneira: divide-se o peso do paciente pela sua altura elevada ao quadrado{RESET}')
	txt = ["Abaixo do peso",
		"Peso normal",
		"Sobrepeso",
		"Obesidade grau 1",
		"Obesidade grau 2",
		"Obesidade grau 3 (mórbida)"]
	rng = [0, 18.5,
		18.5, 24.9,
		25.0, 29.9,
		30.0, 34.9,
		35.0, 39.9,
		40.0, 2147483647]
	peso = float(input("Digite o peso (em kg): "))
	altura = float(input("Digite a altura (em metros): "))
	imc = peso / (altura * altura)
	for i in range(5):
		if rng[i * 2] <= imc < rng[(i * 2) + 1]:
			print(f"Seu IMC é {imc:.2f}, o que indica {txt[i]}")

# A feirante está vendendo frutas com os seguintes preços:
#
# Fruta - Até 5 kg | Acima de 5 kg
# Morango - R$ 2,50 por kg | R$ 2,20 por kg
# Maçã - R$ 1,80 por kg | R$ 1,50 por kg
#
# Implemente um programa para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maçãs adquiridas, ambos números reais, e escrever o valor a ser pago pelo cliente (com precisão de duas casas decimais). Se o cliente fornecer pelo menos uma das quantidades menor do que 0 (zero), a mensagem "Entrada inválida" deve ser exibida no terminal.
def ex04():
	print(f'{PINK}A feirante está vendendo frutas com os seguintes preços:\n\nFruta - Até 5 kg | Acima de 5 kg\nMorango - R$ 2,50 por kg | R$ 2,20 por kg\nMaçã - R$ 1,80 por kg | R$ 1,50 por kg\n\nImplemente um programa para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maçãs adquiridas, ambos números reais, e escrever o valor a ser pago pelo cliente (com precisão de duas casas decimais). Se o cliente fornecer pelo menos uma das quantidades menor do que 0 (zero), a mensagem "Entrada inválida" deve ser exibida no terminal.{RESET}')
	price = [2.5, 2.2, 1.8, 1.5]
	mo = float(input("Digite a quantidade de Morangos (em kg): "))
	ma = float(input("Digite a quantidade de Maçãs (em kg): "))
	if (mo < 0 or ma < 0):
		print("Entrada inválida")
	else:
		cost = mo * price[mo > 5] + ma * price[(ma > 5) + 2]
		print(f"O valor total da sua compra é R$ {cost:.2f}")

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
