"""_summary_:
    Esta fase inicializa un vector de permutación llamado S, basado en la clave proporcionada. El vector S tiene 256 posiciones (del 0 al 255), representando todos los posibles valores de un byte. El propósito del KSA es generar una permutación inicial del vector S en función de la clave.    
    
    Se inicializa el vector S con los valores [0, 1, 2, ..., 255].
    
    Se utiliza la clave para barajar los valores en S.
    
    Se repite para cada byte de la clave, utilizando un índice variable j que depende de la clave y del vector S.
"""

"""
la llave de ser de 128 bit o 16 caracteres
"""
llave = "joel_briones_SW_"

def ksa(llave):
    """
    __sumary__:
        proposito:
            Inicializa y permuta un vector de 256 elementos (llamado S) basado en la clave proporcionada. Esta es la fase de inicialización del algoritmo RC4.
        
        parametros:
        llave (str): La clave a utilizar para permutar el vector S.
    
    """
    
    llave = [ord(c) for c in llave]
    """
    basicamente lo que hace es que toma letra por letra la key
    y la convierte en un valor entero (ASCII), y lo almacena en una lista
    """
    S = list(range(256))
    j = 0
    
    # permutar el vector S en funcion de la clave
    for i in range(256):
        j = (j + S[i] + llave[i % len(llave)]) % 256
        S[i], S[j] = S[j], S[i]
    """
    eso es elo mismo que esto:
    S[i] = S[j]
    S[j] = S[i]
    """
    return S
    
# end def    

# usar el pizarron

def prga(S, largo_txt):
    """_summary_:
        lo que hace el basicamente esto:
        toma la lista s, y genera una nueva lista, esto lo hace
        de manera aleatoria, pero basada en la lista S
        y de igual manera vuelve a alterar la lista s
        para que no se repitan los valores
    """
    i = 0
    j = 0
    secuencia = []

    # generar el flujo de claves
    for letra in range(largo_txt):
    
        i = (i + 1) % 256
        j = (j + S[i] + S[j]) % 256
        S[i], S[j] = S[j], S[i]
        secuencia.append(S[(S[i] + S[j]) % 256])

    return secuencia

# end def    

# usar el pizarron

# funcion que las une:
def rc4(llave, texto):
    # fase 1: ksa
    S = ksa(llave)
    
    # fase 2: prga
    secuencia = prga(S, len(texto))
    
    # cifrar/ decifrar con XOR
    resultado = []

    for t, k in zip(texto, secuencia):
        resultado.append(t ^ k)

    return bytes(resultado)

palabra = 'joel_briones'


texto_cifrado = rc4(llave=llave, texto=palabra.encode())
print("Texto cifrado:", texto_cifrado)

# Descifrar el texto
texto_descifrado = rc4(llave=llave, texto=texto_cifrado)
print("Texto descifrado:", texto_descifrado.decode())