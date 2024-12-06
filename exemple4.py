maior_numero = -999999999999999
number = int(input('Entre com um número ou digite -1 para parar: '))
while number != -1:
    if number > maior_numero:
        maior_numero = number
    number = int(input('Entre com um número ou digite -1 para parar: '))
print('O maior número é: ', maior_numero)