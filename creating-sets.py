# SETS EN PYTHON
# Como ocurre con las listas y las tuplas, los sets se declaran ingresando sus elementos entre {llaves}.
# Un set es una manera de almacenar datos en una variable de manera desordenada.
# Es decir, no podemos saber exactamente el orden en que utilizará sus items. 

# CREANDO UN SET

print('CREANDO UN SET') # Muestro título
colors = {'red', 'green', 'blue'} # Creo el set y sus items.
print(colors) # Muestro la var.

# Cada vez que ejecutemos estas líneas Python mostrará la variable 'colors' de manera aleatoria. 


# LONGITUD DE UN SET
# Para saber la cantidad de items que contiene un set, lo hacemos mediante la función LEN().

print('LONGITUD DE UN SET') # Muestro título.
print(len(colors)) # Muestro la longitud de la var. En este caso será 3.


# TIPOS DE DATOS EN UN SET
# Los sets pueden almacenar cualquier tipo de datos en Python. Int, float, str, boolean, complex.

print('TIPO DE DATOS EN UN SET') # Muestor título.
myset = ('hello', 35, True, 2.5) # Creo la var y sus items.
print(myset, type(myset)) # Muestro el valor de la var y su tipo de dato.


# NO ADMITE ITEMS DUPLICADOS
# En Python un set no permite duplicar algún item, solo mostrará el primero.

colors = {'red', 'green', 'blue', 'red'}
print(colors)

       
