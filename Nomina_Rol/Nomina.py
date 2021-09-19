from Componentes import Menu,Valida
from helpers import borrarPantalla,gotoxy
from crudArchivos import Archivo
from entidadesRol import *
from datetime import date
import time
# Procesos de las Opciones del Menu Mantenimiento
def empAdministrativos():
    borrarPantalla()  
    validar = Valida()  
    gotoxy(20,2);print("INGRESO DE EMPLEADO ADMINISTRATIVO")
    gotoxy(15,4);print("Nombre: ")
    gotoxy(15,5);print("Dirección: ")
    gotoxy(15,6);print("Cedula: ")
    gotoxy(15,7);print("Telefono: ")
    gotoxy(15,8);print("Sueldo: ")
    gotoxy(15,9);print("Dia de Ingreso: ")
    gotoxy(15,10);print("Mes de Ingreso: ")
    gotoxy(15,11);print("Año de Ingreso: ")
    nom=validar.solo_letras(" ","Error: Solo letras",33,4)
    dire=validar.solo_letras(" ","Error: Solo letras",33,5)
    ced=validar.cedula("Error: Solo numeros total 10",33,6)
    tel=validar.solo_numeros("Error: Solo numeros",33,7)
    suel=validar.solo_decimales("Error: Solo numeros",33,8)
    dia=validar.solo_dia("Error: Solo numeros",33,9)
    mes=validar.solo_mes("Error: Solo numeros",33,10)
    año=validar.solo_año("Error: Solo numeros",33,11)
    fechaIng= date(año,mes,dia)  
    gotoxy(15,12);print("Departamento id[    ]:")
    gotoxy(32,12);id = input().upper()
    archiDepa = Archivo("./archivos/departamento.txt","|")
    empAdmin = archiDepa.buscar(id)
    depaAdmin = Departamento(empAdmin[1],empAdmin[0])
    gotoxy(40,12);print(depaAdmin.descripcion)
    gotoxy(15,13);print("Cargo id[    ]:")
    gotoxy(25,13);id = input().upper()  
    archiCarg = Archivo("./archivos/cargo.txt","|")
    cargAdmin = archiCarg.buscar(id)
    carAdmin = Cargo(cargAdmin[1],cargAdmin[0])  
    gotoxy(40,13);print(carAdmin.descripcion)
    gotoxy(15,16);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,16);grabar = input().lower()
    if grabar == "s":
        archiAdmin = Archivo("./archivos/administrativo.txt","|")
        listaAdmin= archiAdmin.leer()
        idSig="A"+str(len(listaAdmin)+1)
        Admin = Administrativo(nom, depaAdmin,carAdmin,dire,ced,tel,fechaIng,suel,idSig, True)
        dato = Admin.getEmpleado()
        datos = '|'.join(dato)
        archiAdmin.escribir([datos],"a")   
        gotoxy(15,19);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(15,19);input("Registro No fue Grabado\n presione una tecla para continuar...")
    
def empObreros():
    borrarPantalla()  
    validar = Valida()  
    gotoxy(20,2);print("INGRESO DE EMPLEADO OBRERO")
    gotoxy(15,4);print("Nombre: ")
    gotoxy(15,5);print("Dirección: ")
    gotoxy(15,6);print("Cedula: ")
    gotoxy(15,7);print("Telefono: ")
    gotoxy(15,8);print("Sueldo: ")
    gotoxy(15,9);print("Dia de Ingreso: ")
    gotoxy(15,10);print("Mes de Ingreso: ")
    gotoxy(15,11);print("Año de Ingreso: ")
    nom=validar.solo_letras(" ","Error: Solo letras",33,4)
    dire=validar.solo_letras(" ","Error: Solo letras",33,5)
    ced=validar.cedula("Error: Solo numeros en total 10",33,6)
    tel=validar.solo_numeros("Error: Solo numeros",33,7)
    suel=validar.solo_decimales("Error: Solo numeros",33,8)
    dia=validar.solo_dia("Error: Solo numeros",33,9)
    mes=validar.solo_mes("Error: Solo numeros",33,10)
    año=validar.solo_año("Error: Solo numeros",33,11)
    fechaIng= date(año,mes,dia)  
    gotoxy(15,12);print("Departamento id[    ]:")
    gotoxy(32,12);id = input().upper()
    archiDepa = Archivo("./archivos/departamento.txt","|")
    empObr = archiDepa.buscar(id)
    depaObr = Departamento(empObr[1],empObr[0])
    gotoxy(40,12);print(depaObr.descripcion)
    gotoxy(15,13);print("Cargo id[    ]:")
    gotoxy(25,13);id = input().upper()  
    archiCarg = Archivo("./archivos/cargo.txt","|")
    cargObr = archiCarg.buscar(id)
    carObr = Cargo(cargObr[1],cargObr[0])  
    gotoxy(40,13);print(carObr.descripcion)
    gotoxy(15,16);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,16);grabar = input().lower()
    if grabar == "s":
        archiObr = Archivo("./archivos/obrero.txt","|")
        listaObr= archiObr.leer()
        idSig="O"+str(len(listaObr)+1)
        Obre = Obrero(nom, depaObr,carObr,dire,ced,tel,fechaIng,suel,idSig, True)
        dato = Obre.getEmpleado()
        datos = '|'.join(dato)
        archiObr.escribir([datos],"a")   
        gotoxy(15,19);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(15,19);input("Registro No fue Grabado\n presione una tecla para continuar...")

def cargos():
    borrarPantalla()
    validar = Valida()     
    gotoxy(20,2);print("MANTENIMIENTO DE CARGO")
    gotoxy(15,4);print("Codigo: ")
    gotoxy(15,5);print("Descripcion Cargo: ")
    desCargo= validar.solo_letras(" ","Error: Solo letras",33,5)
    gotoxy(15,6);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,6);grabar = input().lower()
    if grabar == "s":
       archiCargo = Archivo("./archivos/cargo.txt","|")
       cargos = archiCargo.leer()
       if cargos : idSig = int(cargos[-1][0])+1
       else: idSig=1
       cargo = Cargo(desCargo,idSig)
       datos = cargo.getCargo()
       datos = '|'.join(datos)
       archiCargo.escribir([datos],"a")
       gotoxy(15,7);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
       gotoxy(15,7);input("Registro No fue Grabado\n presione una tecla para continuar...")

def departamento():
    borrarPantalla()
    validar = Valida()     
    gotoxy(20,2);print("MANTENIMIENTO DE DEPARTAMENTO")
    gotoxy(15,4);print("Codigo: ")
    gotoxy(15,5);print("Descripcion Departamento: ")
    desDepa= validar.solo_letras(" ","Error: Solo letras",40,5)
    gotoxy(15,6);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,6);grabar = input().lower()
    if grabar == "s":
       archiDepa = Archivo("./archivos/departamento.txt","|")
       depart = archiDepa.leer()
       if depart : idSig = int(depart[-1][0])+1
       else: idSig=1
       dep = Departamento(desDepa,idSig)
       datos = dep.getDepartamento()
       datos = '|'.join(datos)
       archiDepa.escribir([datos],"a")
       gotoxy(15,7);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
       gotoxy(15,7);input("Registro No fue Grabado\n presione una tecla para continuar...")

def empresa():
    borrarPantalla()  
    validar = Valida()    
    gotoxy(20,2);print("MANTENIMIENTO DE EMPRESA")
    gotoxy(15,4);print("Razon Social: ")
    gotoxy(15,5);print("Dirección: ")
    gotoxy(15,6);print("Telefono: ")
    gotoxy(15,7);print("Ruc: ")
    razonSocial= validar.solo_letras(" ","Error: Solo letras",33,4)
    dirección= validar.solo_letras(" ","Error: Solo letras",33,5)
    tel=validar.solo_numeros("Error: Solo numeros",33,6)
    ruc=validar.solo_numeros("Error: Solo numeros",33,7)
    gotoxy(15,8);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,8);grabar = input().lower()
    if grabar == "s":
       archiEmpresa = Archivo("./archivos/empresa.txt","|")
       archiEmpresa.leer()
       emp = Empresa(razonSocial,dirección,tel,ruc)
       datos = emp.getEmpresa()
       datos = '|'.join(datos)
       archiEmpresa.escribir([datos],"w")
       gotoxy(15,9);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
       gotoxy(15,9);input("Registro No fue Grabado\n presione una tecla para continuar...")

def parametro():
    borrarPantalla()  
    validar = Valida()    
    gotoxy(20,2);print("MANTENIMIENTO DE DEDUCCIONES")
    gotoxy(15,4);print("Iess: ")
    gotoxy(15,5);print("Comisión: ")
    gotoxy(15,6);print("Antiguedad: ")
    iess=validar.solo_decimales("Error: Solo numeros",33,4)
    comision=validar.solo_decimales("Error: Solo numeros",33,5)
    antiguedad=validar.solo_decimales("Error: Solo numeros",33,6)
    gotoxy(15,7);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,7);grabar = input().lower()
    if grabar == "s":
       archiDeducciones = Archivo("./archivos/deducciones.txt","|")
       archiDeducciones.leer()
       dedu = Deduccion(iess,comision,antiguedad)
       datos= dedu.getDeduccion()
       datos = '|'.join(datos)
       archiDeducciones.escribir([datos],"w")
       gotoxy(15,8);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
       gotoxy(15,8);input("Registro No fue Grabado\n presione una tecla para continuar...")
# ...........................................................
# Opciones del Menu Novedades
def sobretiempos():
    borrarPantalla()     
    gotoxy(20,2);print("INGRESO DE HORAS EXTRAS")
    empleado,entEmpleado = [],None
    aamm,h50,h100=0,0,0
    while not empleado:
        gotoxy(15,5);print("Empleado ID[    ]: ")
        gotoxy(27,5);id = input().upper()
        archiEmpleado = Archivo("./archivos/obrero.txt","|")
        empleado = archiEmpleado.buscar(id)
        if empleado:
            entEmpleado = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0]) 
            gotoxy(35,5);print(entEmpleado.nombre)
        else: 
            gotoxy(27,5);print("No existe Empleado con ese codigo[{}]:".format(id))
            time.sleep(2);gotoxy(27,5);print(" "*40)
    
    gotoxy(15,6);print("Periodo[aaaamm]")
    gotoxy(15,7);print("Horas50: ")
    gotoxy(15,8);print("Horas100: ")
    validar = Valida()
    aamm=validar.solo_numeros("Error: Solo numeros",23,6)
    h50=validar.solo_decimales("Error: Solo numeros",23,7)
    h100=validar.solo_decimales("Error: Solo numeros",24,8)
    gotoxy(15,9);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,9);grabar = input().lower()
    if grabar == "s":
        archiSobretiempo = Archivo("./archivos/sobretiempo.txt","|")
        sobretiempos = archiSobretiempo.leer()
        if sobretiempos : idSig = int(sobretiempos[-1][0])+1
        else: idSig=1
        sobretiempo = Sobretiempo(entEmpleado,aamm,h50,h100,True,idSig)
        datos = sobretiempo.getSobretiempo()
        datos = '|'.join(datos)
        archiSobretiempo.escribir([datos],"a")                 
        gotoxy(10,10);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
       gotoxy(10,10);input("Registro No fue Grabado\n presione una tecla para continuar...")     
     
def prestamos():
    borrarPantalla()  
    validar = Valida()   
    gotoxy(20,2);print("INGRESO DE VALOR DEL PRESTAMO")
    gotoxy(15,4);print("Obrero-Administrativo(O/A): ")
    opc=validar.solo_letras(" ","Error: Solo letras",44,4).upper()
    if opc == "A": 
            gotoxy(15,5);print("A D M I N I S T R A T I V O")
            gotoxy(15,6);print("Empleado ID[    ]: ")
            gotoxy(27,6);id = input().upper()
            archiEmp = Archivo("./archivos/administrativo.txt","|")
            empleado= archiEmp.buscar(id)
            if empleado:
                entEmpleado = Administrativo(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0]) 
                gotoxy(35,6);print(entEmpleado.nombre)
            else: 
                gotoxy(35,6);print("No existe Empleado con ese codigo[{}]:".format(id))
                time.sleep(2);gotoxy(35,6);print(" "*40)
    else:
            gotoxy(15,5);print("O B R E R O")
            gotoxy(15,6);print("Empleado ID[    ]: ")
            gotoxy(27,6);id = input().upper()
            archiEmp = Archivo("./archivos/obrero.txt","|")
            empleado= archiEmp.buscar(id)
            if empleado:
               entEmpleado = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0]) 
               gotoxy(35,6);print(entEmpleado.nombre)
            else: 
                gotoxy(35,6);print("No existe Empleado con ese codigo[{}]:".format(id))
                time.sleep(2);gotoxy(35,6);print(" "*40)

    gotoxy(15,7);print("Periodo[aaaamm]")
    gotoxy(15,8);print("Valor:")
    gotoxy(15,9);print("Número de Pago:")
    gotoxy(15,10);print("Saldo:")
    validar = Valida()
    aamm=validar.solo_numeros("Error: Solo numeros",23,7)
    valor=validar.solo_decimales("Error: Solo numeros",33,8)
    numP=validar.solo_numeros("Error: Solo numeros",33,9)
    saldo=validar.solo_decimales("Error: Solo numeros",33,10)
    gotoxy(15,11);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,11);grabar = input().lower()
    if grabar == "s":
        archiPrestamo = Archivo("./archivos/prestamo.txt","|")
        prestamos = archiPrestamo.leer()
        if prestamos : idSig = int(prestamos[-1][0])+1
        else: idSig=1
        prestamos = Prestamo(entEmpleado,aamm,valor,numP, saldo,True,idSig)
        datos = prestamos.getPrestamo()
        datos = '|'.join(datos)
        archiPrestamo.escribir([datos],"a")                 
        gotoxy(10,13);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(10,13);input("Registro No fue Grabado\n presione una tecla para continuar...")  

# opciones de Rol de Pago
def rolAdministrativo():
   borrarPantalla()
   # Se ingresa los datos del rol a procesar     
   gotoxy(20,2);print("ROL ADMINISTRATIVO")
   aamm=0
   gotoxy(15,6);print("Periodo[aaaamm]")
   validar = Valida()
   aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   gotoxy(15,7);print("Esta seguro de Procesar el Rol(s/n):")
   gotoxy(54,7);grabar = input().lower()
   entEmpAdm = None
   # Se procesa el rol con la confirmacion del usuario
   if grabar == "s":
        # Obtener lista de empleados a procesar el rol
        archiEmp = Archivo("./archivos/administrativo.txt","|")
        ListaEmpAdm = archiEmp.leer()
        if ListaEmpAdm : 
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            archiDeducciones = Archivo("./archivos/deducciones.txt","|")
            deducciones = archiDeducciones.leer()[0]
            entDeduccion = Deduccion(float(deducciones[0]),float(deducciones[1]),float(deducciones[2]))
            #print(entDeduccion.getIess(),entDeduccion.getComision(),entDeduccion.getAntiguedad())
            nomina = Nomina(date.today(),aamm)
            for empleado in ListaEmpAdm:
              #print(empleado)
              entEmpAdm = Administrativo(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],float(empleado[8]),empleado[0]) 
              #print(entEmpAdm.nombre,entEmpAdm.sueldo)
              nomina.calcularNominaDetalle(entEmpAdm,entDeduccion)
            # grabar cabecera del rol
            datosCab = nomina.getNomina()
            datosCab = '|'.join(datosCab)
            archiRol = Archivo("./archivos/rolCabAdm.txt","|")
            archiRol.escribir([datosCab],"a")
            # grabar detalle del rol
            archiDet = Archivo("./archivos/rolDetAdm.txt","|")
            datosDet = nomina.getDetalle()
            # se graba en el detalle empleado por empleado           
            for dt in datosDet:
                dt = nomina.aamm+'|'+'|'.join(dt)
                archiDet.escribir([dt],"a")
            # imprimir rol
            nomina.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,"A D M I N I S T R A T I V O")
            nomina.mostrarDetalleNomina()
    
   else:
       gotoxy(10,10);input("Rol No fue Procesado\n presione una tecla para continuar...")     

   input("               Presione una tecla continuar...")  

def consultaRol():
   borrarPantalla()
   validar = Valida()
   # Se ingresa los datos del rol a Consultar     
   gotoxy(20,2);print("CONSULTA DE ROL OBRERO - ADMINISTRATIVO")
   rol=0
   aamm=""
   gotoxy(15,4);print("Obrero-Administrativo(O/A): ")
   gotoxy(15,6);print("Periodo[aaaamm]")
   gotoxy(44,4)
   rol=input().upper()
   aamm=validar.solo_numeros("Error: Solo numeros",23,6)
   gotoxy(15,7);print("Esta seguro de consultar el Rol(s/n):")
   gotoxy(54,7);procesar = input().lower()
   if procesar == "s":
        if rol == "A": 
            tit = "A D M I N I S T R A T I V O"
            archiRolCab = Archivo("./archivos/rolCabAdm.txt","|")
            archiRolDet = Archivo("./archivos/rolDetAdm.txt","|")
        else: 
            tit = "O B R E R O"
            archiRolCab = Archivo("./archivos/rolCabObre.txt","|")
            archiRolDet = Archivo("./archivos/rolDetObre.txt","|")
        cabrol = archiRolCab.buscar(aamm)
        if cabrol:
            entCabRol = Nomina(cabrol[1],cabrol[0])
            entCabRol.totIngresos=float(cabrol[2])
            entCabRol.totDescuentos=float(cabrol[3])
            entCabRol.totPagoNeto=float(cabrol[4])
            detalle= archiRolDet.buscarLista(aamm)
            for det in detalle:
                entCabRol.detalleNomina.append(det[1:])    
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            entCabRol.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,tit)
            entCabRol.mostrarDetalleNomina()
        else:
            gotoxy(10,10);input("No existe rol con ese periodo\n presione una tecla para continuar...")     
            
   else:
       gotoxy(10,10);input("Consulta Cancelada\n presione una tecla para continuar...")     
   input("               Presione una tecla continuar...")  

def rolObrero():
    borrarPantalla()
    # Se ingresa los datos del rol a procesar     
    gotoxy(20,2);print("ROL OBRERO")
    aamm=0
    gotoxy(15,6);print("Periodo[aaaamm]")
    validar = Valida()
    aamm=validar.solo_numeros("Error: Solo numeros",23,6)
    gotoxy(15,7);print("Esta seguro de Procesar el Rol(s/n):")
    gotoxy(54,7);grabar = input().lower()
    entEmpObr = None
    # Se procesa el rol con la confirmacion del usuario
    if grabar == "s":
        # Obtener lista de empleados a procesar el rol
        archiEmp = Archivo("./archivos/obrero.txt","|")
        ListaEmpObr = archiEmp.leer()
        if ListaEmpObr : 
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            archiDeducciones = Archivo("./archivos/deducciones.txt","|")
            deducciones = archiDeducciones.leer()[0]
            entDeduccion = Deduccion(float(deducciones[0]),float(deducciones[1]),float(deducciones[2]))
            #print(entDeduccion.getIess(),entDeduccion.getComision(),entDeduccion.getAntiguedad())
            nomina = Nomina(date.today(),aamm)
            for empleado in ListaEmpObr:
              #print(empleado)
              entEmpObr = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],int(empleado[7][:4]),float(empleado[8]),empleado[0]) 
              nomina.calcularNominaDetalle(entEmpObr,entDeduccion)
            # grabar cabecera del rol
            datosCab = nomina.getNomina()
            datosCab = '|'.join(datosCab)
            archiRol = Archivo("./archivos/rolCabObre.txt","|")
            archiRol.escribir([datosCab],"a")
            # grabar detalle del rol
            archiDet = Archivo("./archivos/rolDetObre.txt","|")
            datosDet = nomina.getDetalle()
            # se graba en el detalle empleado por empleado           
            for dt in datosDet: 
                dt = nomina.aamm+'|'+'|'.join(dt)
                archiDet.escribir([dt],"a")
            # imprimir rol
            nomina.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,"O B R E R O S")
            nomina.mostrarDetalleNomina()
    
    else:
        gotoxy(10,10);input("Rol No fue Procesado\n presione una tecla para continuar...")     

    input("               Presione una tecla continuar...")  

# Menu Proceso Principal
opc=''
while opc !='4':  
    borrarPantalla()      
    menu = Menu("Menu Principal",["1) Mantenimiento","2) Novedades","3) Rol de Pago","4) Salir"],20,10)
    opc = menu.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='7':
            borrarPantalla()    
            menu1 = Menu("Menu Mantenimiento",["1) Empleados Administrativos","2) Empleados Obreros","3) Cargos","4) Departamentos","5) Empresa","6) Parametros","7) Salir"],20,10)
            opc1 = menu1.menu()
            if opc1 == "1":
                empAdministrativos()
            if opc1 == "2":
                empObreros()
            elif opc1 == "3":
                cargos()
            elif opc1 == "4":
                departamento()
            elif opc1 == "5":
                empresa()
            elif opc1 == "6":
                parametro()
                        
    elif opc == "2":
            borrarPantalla()
            menu2 = Menu("Menu Novedades",["1) Sobretiempo","2) Prestamos","3) Salir"],20,10)
            opc2 = menu2.menu()
            if opc2 == "1":
                sobretiempos()
            elif opc2 == "2":
                prestamos()
            
    elif opc == "3":
            borrarPantalla()
            menu3 = Menu("Menu Rol",["1) Rol Administrativos","2) Rol Obreros","3) Consulta Rol","4) Salir"],20,10)
            opc3 = menu3.menu()
            if opc3 == "1":
                rolAdministrativo()
            elif opc3 == "2":
                rolObrero()
            elif opc3 == "3":
                consultaRol()
  
    elif opc == "4":
           borrarPantalla()
           print("Gracias por su visita....")
 
    else:
          print("Opcion no valida") 

input("Presione una tecla para salir")
borrarPantalla()
