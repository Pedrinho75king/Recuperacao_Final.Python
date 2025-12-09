lista = []

while True:
    item = input("Digite um item de compra (ou 'fim' para encerrar): ")

    if item.lower() == "fim":
        break

    lista.append(item)

print("Lista de compras:")
for item in lista:
    print("-", item)