## Modulo 3

def suma(a, b, c):
    res = a + b + c
    print('la suma es:', res)
    
tp = 55, 55.22, 33.33
suma(*tp)

def saluda(nombre, edad, sexo, nacionalidad):
    print('Hola', nombre)
    print('Tienes', edad)
    print('eres del sexo', sexo)
    print('eres de nacionalidad', nacionalidad)
    
dicc = {'nombre':'Miguel C.', 'edad':22, 'sexo':'Masculino','nacionalidad':'Mexicana'}
saluda(**dicc)

def invierte(lst):
    print(lst)
    lst_rev = lst[::-1]
    print(lst_rev)
    
lst = ["IPP", "Python", "Scripting", "Curso", "Material"]
invierte(lst)

def completa(dct1, dct2):
    dct2.update(dct1)
    print(dct2)
    
dict1 = {'bookA':1,'bookB':2,'bookC':3}
dict2 = {'bookC':2,'bookD':4,'bookE':5}
completa(dict1,dict2)

## Script 1
mylist = list((1,2,3,4))
print(mylist)
print(type(mylist))

mytuple = tuple(mylist)
print(mytuple)
print(type(mytuple))

## Script 2

lista1 = list(('nombre', 'edad', 'direccion'))
lista2 = list(('Juan','30','Valparaiso'))

clave_tupla = tuple(lista1)
valor_tupla = tuple(lista2)

dicc = dict(zip(clave_tupla, valor_tupla))
print(dicc)
print(type(dicc))
