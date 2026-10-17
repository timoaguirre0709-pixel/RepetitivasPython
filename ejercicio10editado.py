producto = 1
numero = 1

while True:
    if numero > 20:
        break
    producto *= numero
    numero += 1

print(f"El producto de los 20 primeros números naturales es: {producto}")
