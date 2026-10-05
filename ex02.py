nome = input("Digite seu nome: ")
ano_nasc = int(input("Digite o seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nasc

if idade >= 18:
    print("Você pode fazer a carteira de motorista.")

elif idade < 18 and idade >= 16:
    print("Você já pode votar.")