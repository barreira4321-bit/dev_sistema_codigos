# Passagem por Valor
def levelUp(raphael):
    raphael += 1
    # O += é a mesma coisa que escrever
    # raphael = raphael + 1
    print('Idade atual:', raphael)

def levelDown (idade):
    idade = idade -1
    # Mesma coisa de idade -= 1
    return idade

idade = 10
levelUp(idade)
print('Idade depois da levelUp: ', idade)
 # necessario que receba o valor do "return" na linha 11
 # se não tiver a variavel (a esquerda do igual)
 # você perderá o valor

levelDown(idade)
print('Idade depois da levelDown:', idade)