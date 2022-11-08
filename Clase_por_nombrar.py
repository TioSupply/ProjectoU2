class gestion:
    def __init__(self, nombre_pj, pj_construccion, area_solic, plan_fecha, porc_avance, consult_asig, rec_econo, estado_pj): #pj=projecto
        self.nombre_pj = nombre_pj
        self.pj_contruccion = pj_construccion
        self.plan_fecha = plan_fecha
        self.porc_avance = porc_avance
        self.consult_asig = consult_asig
        self.rec_econo = rec_econo
        self.estado_pj = estado_pj
lgestion = list()

   #Lista
#pj_Folio     Agregar, Modificar, eliminar

def agregar(): 
    nombre_folio = input("Ingrese nombre del nuevo folio:\n ")
    serie_folio = input("Agregue una serial al folio agregado")
    plan_fecha = input("Agrege fecha de inicio y termino al proyecto: ")
    avance = input("Actualice los avances del proyecto: ")
    asignacion = input ("Asigne al supervisor del proyecto: ")
    economico = input("Agrege el valor asignado al proyecto: ")
    nueva_gestion = gestion()
    lgestion.append(nueva_gestion)

def informe():
    print(" ")
    print("-----Detalles de proyectos actuales-----\n")
    for gestion in lgestion:
        print(gestion)

def borrar ():
     print (" ")
     L = lgestion
     informe ()
     I = str (input(f"¿Seguro que desea eliminar el proyecto seleccionado?\n"))
     for l in L:
      if l.nombre == I:
         respuesta = input (f"Seguro que desea eliminar el folio seleccionado {l.nombre}? S/N  \n ").title()
         if (respuesta == 'si'):
            lgestion.remove(L)
         elif (respuesta == 'no'):
            print (f"El elemento {l.nombre} no a sido eliminado")

def actualizar ():
     print (" ")












