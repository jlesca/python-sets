# UNIR DOS O MÁS SETS
# Podremos unir sets mediante el uso del método update() o union()

print('JOIN TWO SETS WITH UPDATE()') # Muestro título.
colors = {'red', 'green', 'blue'} # Creo primer set var.
fruits = {'apple', 'banana', 'cherry'} # Creo segunda set var.
print(colors, fruits) # Muestro ambas var.
colors.update(fruits) # Mediante update() uno los valores de 'colors' con los de 'fruits'.
print(colors) # Muestro la var actualizada.
input() # Salgo del programa.


# Para unir con UNION() debemos declarar una tercer variable para almacenar la unión de las otras dos. 

print('UNIR TWO SETS WITH UNION()') # Muestro título.
colors = {'red', 'green', 'blue'} # Creo primer set var.
fruits = {'apple', 'banana', 'cherry'} # Creo segundo set var.
print(colors, fruits) # Muestro ambas var.
new_set = colors.union(fruits) # Creo tercer var, para unir los valores de 'colors' con los de 'fruits'.
print(new_set) # Muestro tercer var.
input() # Salgo del programa.


# MOSTRAR INTERSECCIONES ENTRE 2 SETS
# Al unir dos o más sets, podremos pedirle a Python que nos muestre solo las coincidencias en caso que encuentre items repetidos.
# Lo realizamos con el método INTERSECTION_UPDATE().

print('FIND INTERESECTION BETWEEN TWO SETS') # Muestro título.
colors = {'red','blue', 'green'} # Creo primer set var.
new_colors = {'yellow', 'red', 'orange'} # Creo segunda set var.
print(colors, new_colors) # Muestro ambas var.
colors.intersection_update(new_colors) # Actualizo el valor de 'colors' dejando solo el valor que se repita en 'new_colors'
print(colors) # Muestro var actualizada. En este caso será 'red'.
input() # Salgo del programa.


# SYMMETRIC DIFFERENCE UPDATE
# También podremos pedirle que una todos los valores, menos los que se repiten entre ambas sets.
# Lo realizamos mediante el método SYMMETRIC_DIFFERENCE_UPDATE().

print('KEEP ONLY THE ITEMS THAT NOT REPEAT IN BOTH SETS') # Muestro título.
colors = {'red','blue', 'green'} # Creo primer var y sus items.
new_colors = {'yellow', 'red', 'orange'} # Creo segunda var y sus items.
colors.symmetric_difference_update(new_colors) # Le pido que una sus valores, menos los que coinciden en ambas. 
print(colors) # Muestro la var actualizada con la unión de ambas, menos las repetidas. En este caso 'red'.
input() # Salgo del programa.

