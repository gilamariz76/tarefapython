import random
numero_secreto = random.randint(1, 100)
tentativa = 1

while tentativa <= 3:
    palpite = int(input('Adivinhe o número secreto (entre 1 e 100): '))
    if palpite == numero_secreto:
        print('Parabéns, você acertou!')
        break
else:
    if palpite > numero_secreto:
        print('O número secreto é menor do que', palpite)
    else:
        print('O Número secreto é maior do que', palpite)
    tentativa += 1

if tentativa > 3:
    print('Suas tentativas acabaram. O número secreto era', numero_secreto)