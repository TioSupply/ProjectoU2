class empleados:
    def __init__(self, nombre, apellido, edad, division):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.division = division
        


    def __str__(self):
        return f"nombre = {self.nombre}, {self.apellido}, {self.edad}, {self.division}"
    def getNombre(self):
        self.nombre
    def getApellido(self):
        self.apellido    
#F= permite agregar variables y letras

def agregar(): #Metodo
    nombre = input("Ingrese Nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    division = input("Ingrese su Division: ")
    borrar = ""
    Empleadonuevo = empleados(nombre, apellido, edad, division, borrar)
    listaEmpleados.append(Empleadonuevo)
    #print(Empleadonuevo)

def Informe():
    print(" ")
    print ("--------Lista de Empleados-------- \n")
    for Empleadores in listaEmpleados:
        print(Empleadores)
def borrar():
     L= listaEmpleados
     Informe()
     I= str(input(f"Seleccione al usuario que desea eliminar: \n"))
     for l in L:
        if l.nombre == I:
         respuesta =input(f"Seguro/a que desea eliminar a: {l.nombre} {l.apellido} Si/No \n").title() 
         if (respuesta == 'Si'):
                    listaEmpleados.remove(l)
                    print ("El Usuario a sido borrado")
         elif(respuesta == 'No'):
                    print ("Ocurrio un error inesperado intente nuevamente")

#Inicio del programa    
listaEmpleados = []
while True:
    print("----Crear Cuenta----")
    print("A-Ingrese su Nombre")
    print("B-Ingrese su Apellido")
    print("C-Ingrese su Edad")
    print("D-Ingrese su Cargo")
    print("E-Listado de Empleados: \n")
    print("F-Borrar: ")
    print("G-Cierre de sesion......")
    opcion = input("Ingrese una de las siguientes opciones:  ")
    if(opcion == 'x'):
        print("Saliendo....")
    elif(opcion == 'A'):
       agregar()
    elif(opcion == 'E'):
        Informe()
    elif(opcion == 'F'):
        borrar() 
    elif(opcion== 'G'):
        print("Cerrando sesion....")
        break
    else :
        print("Por favor eliga una opcion disponible")
    