#strings
COOP = "Coop"
MIGROS = "migros"

#numbers
DEFAULT_QUANTITY_TO_ALERT = 1

#BOOLEANS

IS_LOGGED_IN = True

# LISTS 

MOCKUP_PRODUCTS_LIST = ['fregona','cereales','papel higienico']

#TUPLES 

MOCKUP_COUPONS = ('COMIDA A MITAD DE PRECIO',()'PRODUCTO SIN IVA')

#UNPACKING => DESTRUCTURING

(primer_producto, *segundo_producto) = MOCKUP_PRODUCTS_LIST

# SET

SUPERMARKETS = {COOP, MIGROS}
print (SUPERMARKETS)
