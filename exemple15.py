# 0 - Contagem crescente ou decrescente entre dois números
primeiro = int(input("Digite o primeiro número: "))
ultimo = int(input("Digite o último número: "))

if ultimo > primeiro:
    for num in range(primeiro, ultimo + 1):
        print(num, end=" ")
else:
    for num in range(primeiro, ultimo - 1, -1):
        print(num, end=" ")

# 1 - Tabuada de 1 a 10
while True:
    valor = int(input("\n\nDigite um valor inteiro entre 1 e 10: "))
    if 1 <= valor <= 10:
        for i in range(1, 11):
            print(f"{valor} x {i} = {valor * i}")
        break
    else:
        print("Valor inválido. Tente novamente.")

# 2 - Jogo de adivinhar número
import random
numero_secreto = random.randint(1, 100)
print("\nAdivinhe o número entre 1 e 100!")
while True:
    palpite = int(input("Digite seu palpite: "))
    if palpite == numero_secreto:
        print("Parabéns, você acertou!")
        break
    else:
        print("Tente novamente.")

# 3 - Soma de sequência até encontrar número negativo
soma = 0
while True:
    numero = int(input("Digite um número (número negativo para parar): "))
    if numero < 0:
        break
    soma += numero
print(f"A soma dos números digitados é: {soma}")

# 4 - Simulação de lançamento de moeda
lancamentos = int(input("\nQuantas vezes deseja lançar a moeda? "))
caras = coroas = 0
for _ in range(lancamentos):
    resultado = random.randint(0, 1)
    if resultado == 0:
        print("Cara")
        caras += 1
    else:
        print("Coroa")
        coroas += 1
print(f"Total de caras: {caras}, Total de coroas: {coroas}")

# 5 - Simulação de urna eletrônica
votos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
print("\nUrna Eletrônica")
while True:
    print("\nAs opções são:")
    print("1. Candidato Jair Rodrigues\n2. Candidato Carlos Luz\n3. Candidato Neves Rocha\n4. Nulo\n5. Branco\n6. Encerrar votação")
    voto = int(input("Entre com o seu voto: "))
    if voto == 6:
        break
    elif voto in votos:
        votos[voto] += 1
    else:
        print("Voto inválido.")
total_votos = sum(votos.values())
print(f"\nResultado da votação:")
for candidato, num_votos in votos.items():
    print(f"Opção {candidato}: {num_votos} votos")
print(f"Porcentagem de votos nulos: {votos[4] / total_votos * 100:.2f}%")
print(f"Porcentagem de votos brancos: {votos[5] / total_votos * 100:.2f}%")
vencedor = max(votos, key=lambda x: votos[x])
if vencedor in [1, 2, 3]:
    print(f"O candidato vencedor foi: Candidato {vencedor}")
else:
    print("Nenhum candidato venceu.")

# 6 - Rentabilidade de poupança
P = float(input("\nDigite o valor inicial da poupança: "))
i = 0.5 / 100
for mes in range(1, 13):
    M = P * (1 + i)**mes
    print(f"Mês {mes}: R${M:.2f}")

# 7 - Fatorial de um número
numero = int(input("\nDigite um número para calcular o fatorial: "))
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
print(f"O fatorial de {numero} é: {fatorial}")
