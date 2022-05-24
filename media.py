import math
nota1 = int(input ('digite a nota 1:'))
nota2 = int(input ('digite a nota 2:'))
nota3 = int(input ('digite a nota 3:'))
media = (nota1 + nota2 + nota3)/3

if media >= 7 :
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
print(' Sua nota foi {},' .format(media))

