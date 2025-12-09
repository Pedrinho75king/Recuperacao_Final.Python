quantidade = int(input("Quantos números deseja informar? "))

numeros = []

for _ in range(quantidade):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
print("Quantidade de números informados:", len(numeros))