palavras_sem_vogais = 
usuario_palavra = input('Entre com uma palavra:')
usuario_palavra = usuario_palavra.upper()

for letra in usuario_palavra:
    if letra == 'A':
      continue
    elif letra == 'e':
       continue
    elif letra == 'i':
       continue
    elif letra == 'o':
       continue
    else:
       palavras_sem_vogais += letra
print(palavras_sem_vogais)