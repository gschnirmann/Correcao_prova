listaNotas = []
listaBaixas = []
listaMedias = []
listaAltas = []
soma = 0
cont = 0
alunos = 25

#while nota != -1 and cont < alunos:
#-----------------------------------#
while True:
    #Pedimos nota para o professor (deve ser entre 0 e 10)
    nota = int(input("Informe a nota: "))
    #Validação de saída
    if nota == -1 or cont == alunos:
        print("Saindo do programa...")
        break
    #Validar se nota está correta no intervalo (0 - 10)
    if nota < 0 or nota > 10:
        print("Nota inválida, informe novamente...")
        continue
    else:
        #insere nota na lista
        listaNotas.append(nota)
        soma += nota
        cont += 1
        #verificar em qual sub lista a nota está:
        if nota >= 7:
            listaAltas.append(nota)
        elif nota >= 4 and nota < 7:
            listaMedias.append(nota)
        else:
            listaBaixas.append(nota)

#Imprimindo informações
if len(listaNotas) > 0:
    media = soma/cont
    print(f"Notas: {listaNotas}, média: {media}")
    print(f"Altas: {listaAltas}, quantidade: {len(listaAltas)}")
    print(f"Médias: {listaMedias}, quantidade: {len(listaMedias)}")
    print(f"Baixas: {listaBaixas}, quantidade: {len(listaBaixas)}")
else:
    print("Lista vazia... sem notas para calcular")