maior = 0
contador = 0
numero = int(input("Informe um número"))
maior = numero
while contador < 4:
    if numero > maior:
        maior = numero
    numero = int(input("Informe um número"))
    contador += 1

print(maior)