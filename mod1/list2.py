RESET = "\033[0m"
RED = "\033[38;5;9m"
PINK = "\033[38;5;13m"
ORANGE = "\033[38;5;214m"
TEAL = "\033[38;5;14m"

def ex00():
    print(f'{PINK}Implemente um programa que leia 3 números inteiros e verifique se os números representam um terno pitagórico.{RESET}')
    a = (int(input("informe o cateto 1(a): ")))
    b = (int(input("informe o cateto 2(b): ")))
    c = (int(input("informe a hipotenusa(c): ")))
    if a ** 2 + b ** 2 == c ** 2:
        print(f"{a},{b},{c} representam um terno pitagórico")
    else:
        print(f"{a},{b},{c} NÃO representam um terno pitagórico")

def ex01():
    print(f'{PINK}Implemente um algoritmo que ao receber o salário atual de um funcionário, calcule o valor do novo salário, reajustado de acordo com a tabela abaixo:\nAbaixo de R$500 | 15%\nDe R$500 até R$1000 | 10%\nAcima de R$1000 | 5%{RESET}')
    s = int(input("Informe o salário atual: "))
    r = [15, 10, 5]
    if s in range(0, 500):
         s *= 1 + r[0] * 0.01
    elif 500 < s <= 1000:
        s *= 1 + r[1] * 0.01
    else:
        s *= 1 + r[2] * 0.01
    print("Novo salario: %d" % s)

def ex02():
    print(f'{PINK}Implemente um programa em linguagem Python que lê um valor (i), inteiro e positivo e 3 valores a, b e c. Se o valor de (i) é par então calcular e imprimir na tela a média aritmética de a, b e c. Caso contrário (o numero seja impar) e i>10 então calcular e imprimir na tela a média aritmética e ponderada de a, b e c. Os pesos dos valores são respectivamente 2, 3 e 4.{RESET}')
    i = int(input("Informe i: "))
    a = int(input("Informe a: "))
    b = int(input("Informe b: "))
    c = int(input("Informe c: "))

    ma = (a + b + c) / 3
    mp = ((a * 2) + (b * 3) + (c * 4)) / (2 + 3 + 4)

    if i % 2 and i > 10:
        print(f"MA: {ma:.1f} MP: {mp:.1f}")
    else:
        print(f"MA: {ma:.1f}")

def ex03():
    print(f'{PINK}Um pedreiro precisa calcular quantos ladrilhos devem ser comprados para cobrir a área de uma sala dada em cm². Implemente um programa que leia do teclado o tipo do ladrilho e a área da sala. Ladrilho tipo 1 tem 80cm² e tipo 2 tem 60cm²{RESET}')
    import math

    l = int(input("Forneça o tipo de ladrilho (1 ou 2): "))
    a = int(input("Forneça a área da sala: "))
    A = [80, 60]

    if 0 < l < 3: print("Quantidade de ladrilhos: %d" % math.ceil(a / A[l - 1]))

def ex04():
    print(f'{PINK}Implemente um Programa que verifique se uma letra digitada é vogal ou consoante.{RESET}')
    c = input("Informe uma letra: ")
    vogais = ['a', 'e', 'i', 'o', 'u']
    res = ["Consoante", "Vogal"]
    print("%s" % res[vogais.count(c.lower()) > 0])

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
