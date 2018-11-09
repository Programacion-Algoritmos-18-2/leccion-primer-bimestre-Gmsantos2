class Empleado(object):
	
	def __init__(self): #funcion __init__ donde tenemos las variables a utilizar
		self.nombre = ""            # inicializacion de variables 
		self.apellido = ""
		self.cedula = ""
		self.comision_fija = 0.0
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

class EmpleadoPorHoras(Empleado):
	
	def __init__ (self):#funcion __init__ donde tenemos las variables a utilizar
		super(EmpleadoPorHoras, self).__init__()  #utilizamos el super para ocupar las funciones de la clase Empleado
		self.numero_horas = 0  # inicializacion de variables 
		self.valor_hora = 0.0
	
	#FUNCIONES DONDE VAMOS A AGREGAR EL VALOR QUE SE INGRESA POR EL  MAIN Y LO OBTENEMOS PARA PODER PRESENTARLO AL FINAL
	def agregar_numero_horas (self, a):
		self.numero_horas = a
	
	def obtener_numero_horas (self):
		return self.numero_horas

	def agregar_valor_hora (self, b):
		self.valor_hora = b
	
	def obtener_valor_hora (self):
		return self.valor_hora

	def calcular_sueldo_final(self):
		q = self.numero_horas* self.valor_hora 
		return q

	#funcion para presentar los datos
	def presentar_datos(self):
		cadena = ("%s\nNumero horas: %.2f\nValor hora: %d\nSueldo final:%.2f"%(super(EmpleadoPorHoras, self).presentar_datos(),self.obtener_numero_horas(),self.obtener_valor_hora(),self.calcular_sueldo_final()))
		return cadena 

class EmpleadoFijo(Empleado):
	
	def __init__ (self):#funcion __init__ donde tenemos las variables a utilizar
		super(EmpleadoFijo, self).__init__()  #utilizamos el super para ocupar las funciones de la clase Empleado
		self.sueldo_fijo = 0.0  # inicializacion de variables 
		self.descuento_seguro = 0.0 
	
	#FUNCIONES DONDE VAMOS A AGREGAR EL VALOR QUE SE INGRESA POR EL  MAIN Y LO OBTENEMOS PARA PODER PRESENTARLO AL FINAL
	def agregar_sueldo (self, s):
		self.sueldo_fijo = s
	
	def obtener_sueldo (self):
		return self.sueldo_fijo

	def descuento_seguro (self, d):
		self.descuento_seguro = (d / 100) * self.sueldo_fijo

	
	def obtener_descuento_seguro (self):
		return self.descuento_seguro 

	def calcular_sueldo_final(self):
		q = self.sueldo_fijo + self.obtener_comision_fija() - self.descuento_seguro 
		return q

	#funcion para presentar los datos
	def presentar_datos(self):
		cadena = ("%s\nSueldo: %.2f\nDescuento: %d (porcentaje)\nSueldo final:%.2f"%(super(EmpleadoFijo, self).presentar_datos(),self.obtener_sueldo(),self.obtener_descuento_seguro(),self.calcular_sueldo_final()))
		return cadena 

class EmpleadoPorSemana(Empleado):
	
	def __init__(self):#funcion __init__ donde tenemos las variables a utilizar
		super(EmpleadoPorSemana, self).__init__() #utilizamos el super para ocupar las funciones de la clase Empleado
		self.numero_semanas = 0  # inicializacion de variables 
		self.valor_semanal = 0

	#FUNCIONES DONDE VAMOS A AGREGAR EL VALOR QUE SE INGRESA POR EL  MAIN Y LO OBTENEMOS PARA PODER PRESENTARLO AL FINAL
	def agregar_numero_semanas(self, semanas):
		self.numero_semanas = semanas

	def agregar_valor_semanal(self, valor):
		self.valor_semanal = valor

	def obtener_numero_semanas(self):
		return numero_semanas

	def obtener_valor_semanal(self):
		return valor_semanal

	def calcular_sueldo_final(self):
		return self.obtener_numero_semanas() * self.obtener_valor_semanal() + self.obtener_comision_fija()

	#funcion para presentar los datos
	def presentar_datos(self):
		cadena = ("%s\nNumero Semanas: %d\nValor semanal: %.2f\nSueldo final: %.2f\n"  % (super(EmpleadoPorSemana, self).presentar_datos()), self.obtener_numero_semanas(), self.obtener_valor_semanal(), self.calcular_sueldo_final())
		return cadena