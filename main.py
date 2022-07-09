#ALGORITMO RSA
#generamos 2 primos p y q, talque p sea diferente de q y cada uno de tiene que ser k/2 bits (mitad)
import math
import random

aleatorio = random.SystemRandom()

def prueba(n, a):
    exp = n - 1
    while not exp & 1:
        exp >>= 1
    if pow(a, exp, n) == 1:
        return True
    while exp < n - 1:
        if pow(a, exp, n) == n - 1:
            return True
        exp <<= 1
    return False

def Miller_Rabin(n, k = 40):
    for i in range(k):
        a = aleatorio.randrange(2, n - 1)
        if not prueba(n, a):
            return False
    return True

def gen_primo(bits):
    while True:
        a = (aleatorio.randrange(1 << bits - 1, 1 << bits) >> 1) + 1
        if Miller_Rabin(a):
            return a

def euclides(a, b):
    if b == 0:
        return a
    return euclides(b, a % b)

print("Generar numero p primo aleatorio de k/2 bits")
#eleccion = int(input("Elija: "))
eleccion = 64
#mitad = eleccion / 2
#print("Numero p aleatorio de " + str(mitad) + " bits")
print("Valor de p: ")
print(gen_primo(eleccion))
print()
#=============================================================================
print("Generar numero q primo aleatorio de k/2 bits")
#eleccion2 = int(input("Elija: "))
eleccion2 = 64
#mitad2 = eleccion2 / 2
#print("Numero q aleatorio de " + str(mitad2) + " bits"
print("Valor de q: ")
print(gen_primo(eleccion2))
print()
#=============================================================================
#Calculamos n = p * q
n = eleccion * eleccion2
print("Generamos valor de n")
print(n)
print()
#Calcular la función Euler de n
def PHI(ene):
    r = 0
    for i in range(ene):
        d = euclides(i, n)
        if d == 1:
            r = r + 1
    return r
print("Funcion Euler de n es: ")
print(PHI(n))
#=============================================================================
#generamos un número entre [2 y n - 1]
def generar_E(minimo, maximo):
    r = aleatorio.randrange(minimo, maximo)
    return r

print("Generamos el valor de e: ")
e = generar_E(2, n - 1)
print(e)
print()
#============================================================================
#usamos el algoritmo extendido de Euclides 
def extendido_euclides(a, b):
    x1, x2 = 1, 0
    y1, y2 = 0, 1
    while b:
        q, r = divmod(a, b)
        x2, x1 = x1 - q * x2, x2
        y2, y1 = y1 - q * y2, y2
        a, b = b, r
    return a, x1, y1

print("Hallamos d con algoritmo extendido de euclides: ")
d = extendido_euclides(e, n)
print(d)
print()
