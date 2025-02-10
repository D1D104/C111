nome_completo = input("Digite seu nome completo: ")

print("Nome em maiusculas:", nome_completo.upper())
print("Nome em minusculas:", nome_completo.lower())
print("Quantidade de letras no nome:", len(nome_completo.replace(" ", ""))) #sem espaço

partes_nome = nome_completo.split()
if len(partes_nome) > 1:
    partes_nome[-1] = "do Inatel"
    novo_nome = " ".join(partes_nome)
    print("Nome alterado:", novo_nome)
else:
    print("Não foi possível alterar o nome.")
