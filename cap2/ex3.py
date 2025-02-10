while True:
    sexo = input("Digite seu sexo (M/F): ").upper()
    
    if sexo == "M":
        print("Sexo Masculino")
        break
    elif sexo == "F":
        print("Sexo Feminino")
        break
    else:
        print("Entrada invalida! Digite novamente (M ou F).")
