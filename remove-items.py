# ELIMINAR ELEMENTOS DE UN SET
# Para eliminar un item específico debemos usar le método REMOVE() o DISCARD()

print('REMOVE ITEM FROM SET') # Muestro titulo.
colors = {'red','blue', 'green'} # Creo set y sus items.
print(colors) # Muestro var.
colors.remove('blue') # Elimino item 'blue' de la var.
print(colors) # Muestro var actualizada.


# ELIMINAR MEDIANTE POP()
# Por tener la característica de ser una variable desordenada, no podemos especificar la posición a eliminar.
# Mediante POP() se podrá eliminar siempre el último item.


print('REMOVE THROUGH POP') # Muestro titulo.
colors = {'red','blue', 'green'} # Creo set y sus items.
print(colors) # Muestro var.
colors.pop() # Elimino item mediante el método POP() de la var.
print(colors) # Muestro var actualizada.

# Si ejecuto el programa varias veces el elemento eliminado irá variando. 


# LIMPIAR UN SET
# Podremos limpiar el set mediante el méotod CLEAR.

print('CLEAR SET') # Muestro titulo.
colors = {'red','blue', 'green'} # Creo set y sus items.
print(colors) # Muestro var.
colors.clear() # Elimino item mediante el método POP() de la var.
print(colors) # Se mostrará el set vacío. {}


# ELIMINAR UN SET
# Con el keyword DEL() eliminamos el set completamente.

print('DELETE SET') # Muestro titulo.
colors = {'red','blue', 'green'} # Creo set y sus items.
del colors # Elimino la var.
print(colors) # Será un error name 'colors' is not defined.


