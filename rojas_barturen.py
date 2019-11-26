#DETECTORES
#Detector de curso aprobado
#declaracion
alumno=""
codigo=""
nota1=0.0
nota2=0.0
nota3=0.0
nota4=0.0

#Input
alumno=input("ingrese nombre del alumno:")
codigo=input("ingrese codigo del alumno:")
nota1=float(input("ingrese nota1:"))
nota2=float(input("ingrese nota2:"))
nota3=float(input("ingrese nota3:"))
nota4=float(input("ingrese nota4:"))

#procesing
promedio=(nota1+nota2+nota3+nota4)/4

#Detector
#el alumno sera aprobado si la nota es > 10
alumno_aprobado=(promedio > 10)

#OUTPUT
print("###########################")
print("#     nota alumno     #")
print("###########################")
print("# alumno : ",alumno,"  #")
print("# codigo: ",codigo,"        #")
print("# nota1: ",nota1,"           #")
print("# nota2: ",nota2," #")
print("# nota3: ",nota3," #")
print("# nota4:",nota4," #")
print("###########################")
print("# promedio: ",promedio,"      #")
print("# alumno_aprobado: ",alumno_aprobado,  "#")
print("###########################")



#Detector de mayor de edad
#declaracion
nombre=""
dni=""
año_nacimiento=0
año_actual=0

#Input
nombre=input("ingrese nombre:")
dni=input("ingrese dni:")
año_nacimiento=int(input("año_nacimiento:"))
año_actual=int(input("año actual:"))

#procesing
edad=(año_actual - año_nacimiento)

#Detector
#es mayor de edad si la edad es  >= 18
mayor_edad=(edad >= 18)

#OUTPUT
print("###########################")
print("#    mayor de edad    #")
print("###########################")
print("# nombre : ",nombre,"  #")
print("# dni: ",dni,"        #")
print("# año_nacimiento: ",año_nacimiento,"           #")
print("# año_actual: S/. ",año_actual," #")
print("###########################")
print("# edad: ",edad,"      #")
print("# mayor_edad: ",mayor_edad,  "#")
print("###########################")



# Detector de comprador compulsivo
#declaracion
cliente=""
producto=""
cantidad=0
costo_uni=0.0
total=0.0

# INPUT
cliente=input("Ingrese el cliente:")
producto=input("Ingrese producto:")
cant=int(input("Ingrese cantidad:"))
costo_uni=float(input("Ingrese costo uni:"))

# PROCESSING
total=cant*costo_uni

# DETECTOR
# Sera comprador compulsivo cuando el total > 150
comprador_compulsivo=(total > 150)

# OUTPUT
print("###########################")
print("#     BOLETA DE PAGO      #")
print("###########################")
print("# Cliente : ",cliente,"  #")
print("# Producto: ",producto,"        #")
print("# Cantidad: ",cant,"           #")
print("# CostoUnitario: S/. ",costo_uni," #")
print("###########################")
print("# Total: S/. ",total,"      #")
print("# Comprador Compulsivo: ",comprador_compulsivo,  "#")
print("###########################")




#Detector de ganacias
#declaracion
nombre=""
ruc=""
producto=""
cantidad=0
pecio_compra=0.0
pecio_venta=0.0

#Input
nombre=input("ingrese nombre:")
ruc=input("ingrese ruc:")
producto=input("ingrese producto:")
cantidad=int(input("ingrese cantidad"))
precio_compra=float(input("ingrese precio de compra:"))
pecio_venta=float(input("ingrese precio de venta:"))

#procesing
ganacia=( pecio_venta - precio_compra)

#Detector
#se optendra ganancias si >= 50
ganacias=(ganacia >= 50)

#OUTPUT
print("###########################")
print("#    ganacias    #")
print("###########################")
print("# nombre : ",nombre,"  #")
print("# ruc: ",ruc,"   #")
print("# producto: ",producto,"           #")
print("# cantidad: ",cantidad," #")
print("# precio_compra: ",pecio_compra," #")
print("# pecio_venta: ",pecio_venta," #")
print("###########################")
print("# ganancia: ",ganancia,"      #")
print("# ganacias: ",ganancias,  "#")
print("###########################")




#Detector comprador mayoritario
#declaracion
nombre=""
ruc=""
compra1=0.0
compra2=0.0
compra3=0.0

#Input
nombre=input("ingrese nombre:")
ruc=input("ingrese ruc:")
compra1=float(input("ingrese compra1:"))
compra2=float(input("ingrese compra2:"))
compra3=float(input("ingrese compra3:"))

#procesing
total=(compra1+compra2+compra3)

#Detector
#es comprador mayoritario si >500
comprador_mayoritario=(total > 500)

#OUTPUT
print("###########################")
print("#    comprador mayoritario    #")
print("###########################")
print("# nombre : ",nombre,"  #")
print("# ruc: ",ruc,"   #")
print("# compra1: ",compra1," #")
print("# compra2: ",compra2," #")
print("# compra3: ",compra3," #")
print("###########################")
print("# total: ",total,"      #")
print("# comprador_mayoritario: ",comprador_mayoritario,  "#")
print("###########################")




#Detector copradora compulsiva de maquillaje
#declaracion
nombre=""
producto=""
compra1=0.0
compra2=0.0
compra3=0.0

#Input
nombre=input("ingrese nombre:")
producto=input("ingrese producto")
compra1=float(input("ingrese compra1:"))
compra2=float(input("ingrese compra2:"))
compra3=float(input("ingrese compra3:"))

#procesing
total=(compra1+compra2+compra3)

#Detector
#es comprador mayoritario si >400
compradora_compulsiva=(total > 400)

#OUTPUT
print("###########################")
print("#    compradora compulsiva de maquillaje   #")
print("###########################")
print("# nombre : ",nombre,"  #")
print("# compra1: ",compra1," #")
print("# compra2: ",compra2," #")
print("# compra3: ",compra3," #")
print("###########################")
print("# total: ",total,"      #")
print("# compradora_compulsiva: ",compradora_compulsiva,  "#")
print("###########################")



#Detector adicto a las compras
#declaracion
nombre=""
compra1=0.0
compra2=0.0
compra3=0.0

#Input
nombre=input("ingrese nombre:")
compra1=float(input("ingrese compra1:"))
compra2=float(input("ingrese compra2:"))
compra3=float(input("ingrese compra3:"))

#procesing
total=(compra1+compra2+compra3)

#Detector
#es comprador mayoritario si >400
comprador_adicto=(total > 1000)

#OUTPUT
print("###########################")
print("#    comprador adicto  #")
print("###########################")
print("# nombre : ",nombre,"  #")
print("# compra1: ",compra1," #")
print("# compra2: ",compra2," #")
print("# compra3: ",compra3," #")
print("###########################")
print("# total: ",total,"      #")
print("# compradora_adicto: ",comprador_adicto,  "#")
print("###########################")



#Detector socio mayoritario
#declaracion
nombre=""
ruc:""
acciones=0

#Input
nombre=input("ingrese nombre:")
ruc=input("ingrese ruc:")
acciones=int(input("ingrese acciones:"))

#procesing
total=(acciones)

#Detector
#es sosio mayoritario si las acciones es  >20
socio_mayoritario=(total > 20)

#OUTPUT
print("###########################")
print("#    socio mayoritario  #")
print("###########################")
print("# nombre : ",nombre,"  #")
print("# ruc: ",ruc," #")
print("# acciones: ",acciones," #")
print("###########################")
print("# total: ",total,"      #")
print("# socio_mayoritario: ",socio_mayoritario,  "#")
print("###########################")



#Detector de exceso de alumnos en un aula
#declaracion
institucion=""
grado:""
seccion=""
numero_alumnos=0

#Input
institucion=input("ingrese institucion:")
grado=input("ingrese grado:")
seccion=input("ingrese acciones:")
numero_alumnos=int(input("ingrese numero de alumnos:"))

#procesing
total=(numero_alumnos)

#Detector
#hay exceso de alumnos si son  >20
exceso_alumnos=(total > 20)

#OUTPUT
print("###########################")
print("#    exceso de alumnos  #")
print("###########################")
print("# institucion : ",institucion,"  #")
print("# grado: ",seccion," #")
print("# numero_alumnos: ",numero_alumnos," #")
print("###########################")
print("# total: ",total,"      #")
print("# exceso_alumnos: ",exceso_alumnos,  "#")
print("###########################")




#Detector de exceso de compras
#declaracion
cliente=""
dni:""
producto=""
cantidad=0

#Input
cliente=input("ingrese cliente:")
dni=input("ingrese dni:")
producto=input("ingrese producto:")
cantidad=int(input("ingrese cantidad:"))

#procesing
total=(cantidad)

#Detector
#hay exceso de compra si la cantidad de producto es  >50
exceso_compras=(total > 50)

#OUTPUT
print("###########################")
print("#    exceso de compras  #")
print("###########################")
print("# cliente : ",cliente,"  #")
print("# dni: ",dni," #")
print("# producto: ",producto," #")
print("# cantidad: ",cantidad," #")
print("###########################")
print("# total: ",total,"      #")
print("# exceso_compras: ",exceso_compras,  "#")
print("###########################")




#Detector de exceso de precio de arroz
#declaracion
cliente=""
producto=""
cantidad=0.0
precio=0.0
#Input
cliente=input("ingrese cliente:")
producto=input("ingrese producto:")
cantidad=int(input("ingrese cantidad:"))
precio=int(input("ingrese precio:"))

#procesing
total=(cantidad*precio)

#Detector
#hay exceso de compra si la cantidad de producto es  >50
exceso_precio=(total >10)

#OUTPUT
print("###########################")
print("#    exceso de precio de arroz  #")
print("###########################")
print("# cliente : ",cliente,"  #")
print("# producto: ",producto," #")
print("# cantidad: ",cantidad," #")
print("#    precio:",precio,"       #")
print("###########################")
print("# total: ",total,"      #")
print("# exceso_precio: ",exceso_precio,  "#")
print("###########################")





# CONVERSORES EN PYTHON
# Convertir la cadena "71067137" en entero
x="71067137"
a=int(x) # int("71067137")
print(a, type(a))

# Convertir el entero "25847" en entero
x="25847"
a=int(x) # int("25847")
print(a, type(a))

# Convertir el entero "25.7" en flotante
x="25.41"
a=float(x)      # float("25.41")
print(a, type(a))

# Convertir la cadena "3241" en flotante
x="3241"
a=float(x)      # float("3241")
print(a, type(a))

# Convertir la cadena "151773j" en entero
x="151773j"
a=str(x)      # int("151773j")
print(a, type(a))





# IMPRECION ASCII
#curso aprobado
#declaracion
alumno=""
codigo=""
nota1=0.0
nota2=0.0
nota3=0.0
nota4=0.0

#Input
alumno=input("ingrese nombre del alumno:")
codigo=input("ingrese codigo del alumno:")
nota1=float(input("ingrese nota1:"))
nota2=float(input("ingrese nota2:"))
nota3=float(input("ingrese nota3:"))
nota4=float(input("ingrese nota4:"))

#procesing
promedio=(nota1+nota2+nota3+nota4)/4

#OUTPUT
print("###########################")
print("#     nota alumno     #")
print("###########################")
print("# alumno : ",alumno,"  #")
print("# codigo: ",codigo,"        #")
print("# nota1: ",nota1,"           #")
print("# nota2: ",nota2," #")
print("# nota3: ",nota3," #")
print("# nota4:",nota4," #")
print("###########################")
print("# promedio: ",promedio,"      #")
print("###########################")



#mayor de edad
#declaracion
nombre=""
dni=""
año_nacimiento=0
año_actual=0

#Input
nombre=input("ingrese nombre:")
dni=input("ingrese dni:")
año_nacimiento=int(input("año_nacimiento:"))
año_actual=int(input("año actual:"))

#procesing
edad=(año_actual - año_nacimiento)

#OUTPUT
print("###########################")
print("#    mayor de edad    #")
print("###########################")
print("# nombre : ",nombre,"  #")
print("# dni: ",dni,"        #")
print("# año_nacimiento: ",año_nacimiento,"           #")
print("# año_actual: S/. ",año_actual," #")
print("###########################")
print("# edad: ",edad,"      #")
print("###########################")



#  comprador compulsivo
#declaracion
cliente=""
producto=""
cantidad=0
costo_uni=0.0
total=0.0

# INPUT
cliente=input("Ingrese el cliente:")
producto=input("Ingrese producto:")
cant=int(input("Ingrese cantidad:"))
costo_uni=float(input("Ingrese costo uni:"))

# PROCESSING
total=cant*costo_uni

# OUTPUT
print("###########################")
print("#     BOLETA DE PAGO      #")
print("###########################")
print("# Cliente : ",cliente,"  #")
print("# Producto: ",producto,"        #")
print("# Cantidad: ",cant,"           #")
print("# CostoUnitario: S/. ",costo_uni," #")
print("###########################")
print("# Total: S/. ",total,"      #")
print("###########################")



# ganacias
#declaracion
nombre=""
ruc=""
producto=""
cantidad=0
pecio_compra=0.0
pecio_venta=0.0

#Input
nombre=input("ingrese nombre:")
ruc=input("ingrese ruc:")
producto=input("ingrese producto:")
cantidad=int(input("ingrese cantidad"))
precio_compra=float(input("ingrese precio de compra:"))
pecio_venta=float(input("ingrese precio de venta:"))

#procesing
ganacia=( pecio_venta - precio_compra)

#OUTPUT
print("###########################")
print("#    ganacias    #")
print("###########################")
print("# nombre : ",nombre,"  #")
print("# ruc: ",ruc,"   #")
print("# producto: ",producto,"           #")
print("# cantidad: ",cantidad," #")
print("# precio_compra: ",pecio_compra," #")
print("# pecio_venta: ",pecio_venta," #")
print("###########################")
print("# ganancia: ",ganancia,"      #")
print("###########################")



#comprador mayoritario
#declaracion
nombre=""
ruc=""
compra1=0.0
compra2=0.0
compra3=0.0

#Input
nombre=input("ingrese nombre:")
ruc=input("ingrese ruc:")
compra1=float(input("ingrese compra1:"))
compra2=float(input("ingrese compra2:"))
compra3=float(input("ingrese compra3:"))

#procesing
total=(compra1+compra2+compra3)

#OUTPUT
print("###########################")
print("#    comprador mayoritario    #")
print("###########################")
print("# nombre : ",nombre,"  #")
print("# ruc: ",ruc,"   #")
print("# compra1: ",compra1," #")
print("# compra2: ",compra2," #")
print("# compra3: ",compra3," #")
print("###########################")
print("# total: ",total,"      #")
print("###########################")


# copradora compulsiva de maquillaje
#declaracion
nombre=""
producto=""
compra1=0.0
compra2=0.0
compra3=0.0

#Input
nombre=input("ingrese nombre:")
producto=input("ingrese producto")
compra1=float(input("ingrese compra1:"))
compra2=float(input("ingrese compra2:"))
compra3=float(input("ingrese compra3:"))

#procesing
total=(compra1+compra2+compra3)

#OUTPUT
print("###########################")
print("#    compradora compulsiva de maquillaje   #")
print("###########################")
print("# nombre : ",nombre,"  #")
print("# compra1: ",compra1," #")
print("# compra2: ",compra2," #")
print("# compra3: ",compra3," #")
print("###########################")
print("# total: ",total,"      #")
print("###########################")



#adicto a las compras
#declaracion
nombre=""
compra1=0.0
compra2=0.0
compra3=0.0

#Input
nombre=input("ingrese nombre:")
compra1=float(input("ingrese compra1:"))
compra2=float(input("ingrese compra2:"))
compra3=float(input("ingrese compra3:"))

#procesing
total=(compra1+compra2+compra3)

#OUTPUT
print("###########################")
print("#    comprador adicto  #")
print("###########################")
print("# nombre : ",nombre,"  #")
print("# compra1: ",compra1," #")
print("# compra2: ",compra2," #")
print("# compra3: ",compra3," #")
print("###########################")
print("# total: ",total,"      #")
print("###########################")



# socio mayoritario
#declaracion
nombre=""
ruc:""
acciones=0

#Input
nombre=input("ingrese nombre:")
ruc=input("ingrese ruc:")
acciones=int(input("ingrese acciones:"))

#procesing
total=(acciones)

#OUTPUT
print("###########################")
print("#    socio mayoritario  #")
print("###########################")
print("# nombre : ",nombre,"  #")
print("# ruc: ",ruc," #")
print("# acciones: ",acciones," #")
print("###########################")
print("# total: ",total,"      #")
print("###########################")



# exceso de alumnos en un aula
#declaracion
institucion=""
grado:""
seccion=""
numero_alumnos=0

#Input
institucion=input("ingrese institucion:")
grado=input("ingrese grado:")
seccion=input("ingrese acciones:")
numero_alumnos=int(input("ingrese numero de alumnos:"))

#procesing
total=(numero_alumnos)

#OUTPUT
print("###########################")
print("#    exceso de alumnos  #")
print("###########################")
print("# institucion : ",institucion,"  #")
print("# grado: ",seccion," #")
print("# numero_alumnos: ",numero_alumnos," #")
print("###########################")
print("# total: ",total,"      #")
print("###########################")




#exceso de compras
#declaracion
cliente=""
dni:""
producto=""
cantidad=0

#Input
cliente=input("ingrese cliente:")
dni=input("ingrese dni:")
producto=input("ingrese producto:")
cantidad=int(input("ingrese cantidad:"))

#procesing
total=(cantidad)

#OUTPUT
print("###########################")
print("#    exceso de compras  #")
print("###########################")
print("# cliente : ",cliente,"  #")
print("# dni: ",dni," #")
print("# producto: ",producto," #")
print("# cantidad: ",cantidad," #")
print("###########################")
print("# total: ",total,"      #")
print("###########################")




#exceso de precio de arroz
#declaracion
cliente=""
producto=""
cantidad=0.0
precio=0.0
#Input
cliente=input("ingrese cliente:")
producto=input("ingrese producto:")
cantidad=int(input("ingrese cantidad:"))
precio=int(input("ingrese precio:"))

#procesing
total=(cantidad*precio)

#OUTPUT
print("###########################")
print("#    exceso de precio de arroz  #")
print("###########################")
print("# cliente : ",cliente,"  #")
print("# producto: ",producto," #")
print("# cantidad: ",cantidad," #")
print("#    precio:",precio,"       #")
print("###########################")
print("# total: ",total,"      #")
print("###########################")
