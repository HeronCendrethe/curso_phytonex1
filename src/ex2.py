import datetime

user = input("Digite seu usuario: ")
timeNow = datetime.datetime.now()
if timeNow.hour < 11:
    print(f"Bom dia: {user}")
elif timeNow.hour < 18:
    print(f"Boa tarde: {user}")
else:
    print(f"Boa noite: {user}")
