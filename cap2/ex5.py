numero  = int(input("Numero entre 1000 e 9999: "))

print(f"Unidade: {numero % 10}")
print(f"Dezena: {(numero // 10) % 10 }")
print(f"Centena: {(numero // 100) % 10 }")
print(f"Milhar: {numero // 1000}")