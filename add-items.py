# AGREGAR ITEMS A UN SET
# Para agregar items a un set ya creado, lo podemos realizar mediante el metodo ADD()

print('ADD ITEMS SET') # Muestro título
colors = {'red', 'green', 'blue'} # Creo var y sus items.
print(colors) # Muestro var
colors.add('white') # Agrego item a la var.
print(colors) # Muestro var actualizada.


# AGREGAR UN SET A OTRO SET
# Python también nos permite crear un set y añadirle los items de otr set.
# Para eso debemos utilizar le método UPDATE()

print('UPDATE SET') # Muestro título
colors = {'red', 'green', 'blue'} # Creo var y sus items.
new_colors = {'black', 'white', 'grey'}
print(colors, new_colors) # Muestro var
colors.update(new_colors) # Agrego item a la var.
print(colors) # Muestro var actualizada.


# AGREGAR UNA LISTA A UN SET
# Podemos agregar una lista o cualquier variable que tenga la capacidad de almacenar items a un set.

print('ADD LIST TO SET') # Muestro título
colors = {'red', 'green', 'blue'} # Creo un set y sus items.
fruits = ['black', 'white', 'grey'] # Creo una lista y sus items.
print(colors, fruits) # Muestro var
colors.update(fruits) # Agrego item a la var.
print(colors) # Muestro var actualizada. 

# En este caso se incluirá los elementos de la lista dentro de la variable set.
