#Crear empleado
from mipaquete.modelado import * # Importamos el paquete
e = Empleado() # le damos el objeto e  a la clase empleado
e.agregar_nombre("Luis") #mandamos valores a cada uno de los metodos siguientes que llamamos con e
e.agregar_apellido("Benitez")
e.agregar_cedula("1110001")
print(e.presentar_datos()) #presentamos  los datos

print("") # espacio

e1 = EmpleadoPorHoras() ## le damos el objeto e1  a la clase empleado por horas
nombre = input("Ingrese su su nombre:\n") # pedimos por teclado que ingrese el nombre y alamcenamos en una variable
e1.agregar_nombre(nombre)   # le mandamos  lo que ingreso el usuario  a la funcion 
e1.agregar_apellido("Andrade") # mandamos valores a cada uno de los siguientes  funciones
e1.agregar_cedula("112233")
e1.agregar_numero_horas(20.2)
e1.agregar_valor_hora(15)
print(e1.presentar_datos()) #presentamos los datos

print("") #espacio

e2 = EmpleadoFijo() #e damos el objeto e2  a la clase empleado fijo
e2.agregar_sueldo(300.2) # mandamos valores float a la funcion agregar sueldo
e2.descuento_seguro = 10 #porcentaje
comision = input("Ingrese comision:\n") # pedimos por teclado que ingrese la comision y alamcenamos en una variable
comision = float(comision) # a esa misma variable la transformamos de tipo cadena a float
e2.agregar_comision_fija(comision) #la variable con el nuevo tipo le mandamos a la funcion
e2.nombre ="Ana" # mandamos valores a cada uno de los siguientes  funciones
e2.apellido = "Diaz"
print(e2.presentar_datos()) #presentamos los datos