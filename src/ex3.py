name = input("Digite seu nome de usuário: ")

qtdCharsName = len(name)
if qtdCharsName < 6:
    print("O seu nome tem menos de 6 caracteres")
else:
    print(f"{name} Você foi cadastrado!")
