class Empleado:
	def __init__(self): #funcion __init__ donde tenemos las variables a utilizar
		self.nombre = ""            # inicializacion de variables 
		self.apellido = ""
		self.cedula = ""
		self.comision_fija = 0
	#funciones para agregar y obtenerlas 
	def agregar_comision_fija (self , comision):
		self.comision_fija = comision
	def obtener_comision_fija (self):
		return self.comision_fija 
	def agregar_nombre (self , n):
		self.nombre = n
	def obtener_nombre (self):
		return self.nombre 
	def agregar_apellido (self, a):
		self.apellido = a
	def obtener_apellido (self):
		return self.apellido
	def agregar_cedula (self, c):
		self.cedula = c
	def obtener_cedula (self):
		return self.cedula  
	#funcion para presentar los datos
	def presentar_datos (self):
		cadena = "Información de %s %s\n  cedula:%s" %(self.nombre , self.apellido, self.cedula)
		return cadena
    


