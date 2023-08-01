## m4

def signo_numero():
    num = int (input())
    if num < 0:
        print()
    elif num == 0:
        print () 
    else:
        print ()
        


def es_par ():
    numero = int (input())
    if numero % 2 != 0:
        print (f"{numero}es impar")
    else:
        print(f"{numero}es par")
        
def n_promedio():
    print("():")
    nota = int (input ())
    while nota != -1:
        total = total + nota
        contar = contar + 1
        print ("():")
        nota = int (input ())
    promedio = total / contar
    print (""+ str(promedio))
    
    
def num_multiplos():
    contador = 0 
    num = int (input(""))
    for i in range (num):
        if (i % num == 0):
            contador += 1
    print("El numero "+ str (num) + "posee" + str(contador) + "multiplos.\n")
    