quant_par = 0
soma_par = 0
media = 0

for i in range(1, 6):
    numero = int(input(f"Digite o {i}° número: "))
    if numero % 2 == 0:
        quant_par += 1
        soma_par += numero
        media = soma_par / quant_par

print(f"A média dos números pares é: {media}")