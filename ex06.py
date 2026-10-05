nome_mais_velho = ""
idade_mais_velha = -1

for i in range(1, 6):
    nome = input(f"Digite o nome da pessoa {i}: ")
    idade = int(input(f"Digite a idade da pessoa {i}: "))

    if idade > idade_mais_velha:
        idade_mais_velha = idade
        nome_mais_velho = nome

print(f"A pessoa mais velha é {nome_mais_velho} com {idade_mais_velha} anos.")
