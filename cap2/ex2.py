numero = int(input("numero para tabuada: "))
inicio = int(input("inicio do intervalo: "))
fim = int(input("fim do intervalo: "))

for i in range(inicio, fim + 1):
    print(f"{numero} x {i} = {numero * i}")
