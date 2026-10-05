quant_par = 0
quant_impar = 0
soma_par = 0
soma_impar = 0

for i in range(1, 11):
    numero = int(input(f"Digite o {i}° número: "))
    
    if numero % 2 == 0:
        quant_par += 1
        soma_par += numero
    else:
        quant_impar += 1
        soma_impar += numero

print(f"A quantidade de números pares é: {quant_par}")
print(f"A quantidade de números ímpares é: {quant_impar}")
print(f"A soma dos números pares é: {soma_par}")
print(f"A soma dos números ímpares é: {soma_impar}")