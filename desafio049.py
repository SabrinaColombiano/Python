import math

frase = input('digite uma frase:')

letras = len(frase.replace(" ", ""))

palavras = len(frase.split())

x = 4.71 * (palavras / letras)
y = 0.5 * palavras

metrica = (x +y) - 21.43

if metrica > 14:
    print('14')

elif metrica < 1:
    print('1')

else:
 print(math.ceil(metrica))

print(letras)
print(palavras)
