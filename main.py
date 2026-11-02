import random

caracteres = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
longitud = int(input("Escribe la longitud de tu contraseña"))

for i in range(longitud):
    password += random.choice(caracteres)


print("Tu contraseña segura es: ",password)   

