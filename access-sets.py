# # ACCEDER A UN SET
# Los sets en Python no se pueden ordenar los elementos ni idexarlos por su posición.,
# No podremos acceder a ellos mediante una posición específica.

print('ACCESS SET ITEMS') # Muestro título.
colors = {'red', 'green', 'blue'} # Creo la variable con sus items.
print(colors[1]) # Muestro la posición 1, pero esto dará un error.

# Tampoco podemos encontrar los items por su posición negativa. 


# RANGO DE ITEMS EN UN SET
# Tampoco podemos especificar desde donde comienza y donde termina nuestro rango.

print('RANGE OF INDEXES')
colors = {'red','green','blue', 'yellow', 'black', 'white'}
print(colors[2:5]) # Le pido que imprima el rango comenzando por la posición 2 y termine en la posición 5 (pero no incluida).
                   # Esto va dar un error.
  

# EXISTENCIA DE UN ITEM EN UN SET
# Si podemos verificar la existencia de un valor específico dentro de un set.
# Esto se realiza mediante la keyword IN.

print('CHECK IF EXIST BLACK') # Muestro título.
colors = {'red','green','blue', 'yellow', 'black', 'white'} # Creo la var y sus items.
if 'black' in colors: # Si black existe en la var, que haga lo siguiente:
  print('Yes, Black exist in the set') # Muestre este mensaje.

  
# Una vez creado un set, no podemos cambiar sus items, pero podemos agregarle.


