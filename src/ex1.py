num1 = input("Digite um numero inteiro: ")

if num1.isnumeric():
    num1 = int(num1)
    if num1 % 2 == 0:
        print("Numero par")
    else:
        print("Numero Impar")
else:
    print("Digite um numero inteiro!")


