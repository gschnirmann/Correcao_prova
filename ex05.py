#Pokemon [NOME, FORÇA, AGILIDADE, ATAQUE, DEFESA, ENERGIA, PONTOS]
pikachu = ["Pikachu", 77, 200, 180, 155, 200, 0]
charmander = ["Charmander", 120, 142, 180, 150,190, 0]
empates = 0
#comparar atributos (1 - 5)
for i in range (1, 6):
    if pikachu[i] > charmander[i]:
        pikachu[6] += pikachu[i]-charmander[i]
    elif charmander[i] > pikachu[i]:
        charmander[6] += charmander[i]-pikachu[i]
    else:
        empates += 1

if pikachu[6] > charmander[6]:
    print(f"{ pikachu[0]} venceu a batalha com {pikachu [6]} pontos.")
elif charmander[6] > pikachu[6]:
    print(f"{charmander[0]} venceu a batalha com {charmander[6]} pontos.")
else:
    print(f"Número de tríbutos de empate: {empates}")