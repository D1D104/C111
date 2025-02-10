distancia =float(input("Qual a distancia em KM: "))

if distancia <= 200:
    print(f"Passagem custa {distancia * 0.5}")
else:   
     print(f"Passagem custa {distancia * 0.45}")