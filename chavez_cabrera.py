#boleta de la compra de repuestos para moto
#declaracion de variables
neumaticos,armadura_doble,fibra_de_carbono,cadena_unitaria=0.0,0.0,0.0,0.0

#input
neumaticos=float(input("ingrese neumaticos:"))
armadura_doble=float(input("ingrese armadura doble:"))
fibra_de_carbono=float(input("ingrese fibra de carbono:"))
cadena_unitaria=float(input("ingrese cadena unitaria:"))

#processing
total_a_pagar=(neumaticos+armadura_doble+fibra_de_carbono+cadena_unitaria)

#detector
#comprador compulsivo cuando el total > 100
comprador_compulsivo=(total_a_pagar > 100)

#output
print("#################################")
print("# boleta de compra de repuestos para moto #")
print("#####################################")
print("neumaticos: ",neumaticos,"             #")
print("armadura_doble: ",armadura_doble,"    #")
print("fibra_de_carbono: ",fibra_de_carbono,"   #")
print("cadena_unitaria: ",cadena_unitaria,"     #")
print("########################################")
print("total_a_pagar: ",total_a_pagar,"          #")
print("comprador compulsivo: ",comprador_compulsivo,"  #")
print("##########################################")


#boleta de medicamentos en solidaridad
#declaracion de variables
nombre_del_paciente,paracetamol,diclofenaco,doloneurobion="",0.0,0.0,0.0

#input
nombre_del_paciente=input("ingrese nombre del paciente:")
paracetamol=float(input("ingrese paracetamol:"))
diclofenaco=float(input("ingrese diclofenaco:"))
doloneurobion=float(input("ingrese doloneurobion:"))

#processing
monto_a_pagar=(paracetamol+diclofenaco+doloneurobion)

#detector
#comprador compulsivo cuando el total > 120
comprador_compulsivo=(monto_a_pagar > 120)

#output
print("##############################")
print("# boleta de medicamentos #")
print("##############################")
print("nombre_del_paracetamol: ",nombre_del_paciente,"    #")
print("paracetamol: ",paracetamol,"     #")
print("diclofenaco: ",diclofenaco,"     #")
print("doloneurobion: ",diclofenaco,"   #")
print("##############################")
print("monto_a_pagar: ",monto_a_pagar,"  #")
print("comprador compulsivo: ",comprador_compulsivo,"     #")
print("##############################")


#formulario para el comedor universitario
#declaracion de variables
nombre_del_solicitante,edad,ano_de_inscripcion,pago_mensual_por_cinco_años="",0,"",0.0

#input
nombre_del_solicitante=input("ingrese nombre del solicitante:")
edad=int(input("ingrese edad:"))
ano_de_inscripcion =input("ingrese ano de ingreso:")
pago_mensual=float(input("ingrese pago mensual:"))

#processing
monto_total=(pago_mensual*5)

#detector
#comprador compulsivo cuando el total > 80
comprador_compulsivo=(monto_total > 80)

#output
print("##################################")
print("# formulario para el comedor #")
print("##################################")
print("nombre del solicitante: ",nombre_del_solicitante,"  #")
print("edad: ",edad,"    #")
print("ano de inscripcion: ",ano_de_inscripcion,"  #")
print("pago mensual: ",pago_mensual,"  #")
print("##################################")
print("monto_total: ",monto_total,"   #")
print("comprador compulsivo: ",comprador_compulsivo,"   #")
print("##################################")


#promedio de gastos de la empresa de textiles sully
#declaracion de variables
tela_animal_print,hilo_blanco,hilo_rojo,maquina_remalladora=0.0,0.0,0.0,0.0

#input
tela_animal_print=float(input("ingrese teta animal print:"))
hilo_blanco=float(input("ingrese hilo blanco:"))
hilo_rojo=float(input("ingrese hilo rojo:"))
maquina_remalladora=float(input("ingrese maquina remalladora:"))

#processing
prom=(tela_animal_print+hilo_blanco+hilo_rojo+maquina_remalladora)/4

#detector
#comprador compulsivo cuando el prom > 30
comprador_compulsivo=(prom > 30)

#output
print("##################################")
print("# promedio de la fabrica textil #")
print("##################################")
print("tela animal print: ",tela_animal_print,"  #")
print("hilo blanco: ",hilo_blanco,"  #")
print("hilo rojo: ",hilo_rojo,"  #")
print("maquina remalladora: ",maquina_remalladora,"   #")
print("##################################")
print("prom: ",prom,"      #")
print("comprador compulsivo: ",comprador_compulsivo,"  #")
print("##################################")



#boleta electronica de sodicac
#declaracion de variables
nombre_del_comprador,puerta_acrilica,martillo,pernos,cementos,tablas,igv="",0.0,0.0,0.0,0.0,0.0,0.0

#input
nombre_del_comprador=input("ingrese nombre:")
puerta_acrilica=float(input("ingrese puerta acrilica:"))
martillo=float(input("ingrese martillo:"))
pernos=float(input("ingrese pernos:"))
cementos=float(input("ingrese cemento:"))
tablas=float(input("ingrese tabla:"))
igv=float(input("ingrese igv:"))

#processing
total_a_pagar=(puerta_acrilica+martillo+pernos+cementos*2+tablas+igv)

#detector
#comprador compulsivo cuando el total a pagar > 140
comprador_compulsivo=(total_a_pagar > 140)

#output
print("##################################")
print("# boleta electronica de sodimac  #")
print("##################################")
print("nombre del comprador: ",nombre_del_comprador,"  #")
print("puerta acrilica: ",puerta_acrilica,"      #")
print("martillo: ",martillo,"        #")
print("pernos: ",pernos,"            #")
print("cementos: ",cementos,"        #")
print("tablas: ",tablas,"            #")
print("igv: ",igv,"                  #")
print("##################################")
print("total a pagar: ",total_a_pagar,"  #")
print("comprador compulsivo: ",comprador_compulsivo,"   #")
print("##################################")



#paquete de viajes para familias
#declaracion de variables
nombre,pasaje1,pasaje2,pasaje3,pasaje4,igv="",0.0,0.0,0.0,0.0,0.0

#input
nombre=input("ingrese nombre:")
pasaje1=float(input("ingrese pasaje1:"))
pasaje2=float(input("ingrese pasaje2:"))
pasaje3=float(input("ingrese pasaje3:"))
pasaje4=float(input("ingrese pasaje4:"))
igv=float(input("ingrese igv:"))

#processing
total=(pasaje1+pasaje2+pasaje3+pasaje4)

#detector
#comprador compulsivo cuando el total > 220
comprador_compulsivo=(total > 220)


#output
print("##################################")
print("# paquete de viajes para familia #")
print("nombre: ",nombre,"               #")
print("pasaje1: ",pasaje1,"             #")
print("pasaje2: ",pasaje2,"             #")
print("pasaje3: ",pasaje3,"             #")
print("pasaje4: ",pasaje4,"             #")
print("igv: ",igv,"                     #")
print("##################################")
print("total: ",total,"                 #")
print("comprador compulsivo: ",comprador_compulsivo,"   #")
print("##################################")


#sacar copia de un libro
#declaracion de variables
nombre_del_libro,nro_de_hojas,precio_por_hoja="",0,0.0

#out
nombre_del_libro=input("ingrese nombre del libro:")
nro_de_hojas=int(input("ingrese nro de hojas:"))
precio_por_hoja=float(input("ingrese precio por hoja:"))

#processing
total=(nro_de_hojas*precio_por_hoja)

#detector
#comprador compulsivo cuando el total > 94
comprador_compulsivo=(total > 94)


#output
print("##################################")
print("# sacar copia de un libro #")
print("##################################")
print("nombre del libro: ",nombre_del_libro,"  #")
print("nro de hojas: ",nro_de_hojas,"     #")
print("precio por hoja: ",precio_por_hoja,"    #")
print("##################################")
print("total: ",total,"                      #")
print("comprador compulsivo: ",comprador_compulsivo,"   #")
print("##################################")


#recibo de luz de los 6 primeros meses
#declaracion de variables
enero,febrero,marzo,abril,mayo,junio,igv=0.0,0.0,0.0,0.0,0.0,0.0,0.0

#input
enero=float(input("ingrese enero:"))
febrero=float(input("ingrese febrero:"))
marzo=float(input("ingrese marzo:"))
abril=float(input("ingrese abril:"))
mayo=float(input("ingrese mayo:"))
junio=float(input("ingrese junio:"))
igv=float(input("ingreso igv:"))

#processing
promedio=(enero+febrero+marzo+abril+mayo+junio+igv)/7

#detector
#comprador compulsivo cuando el promedio > 69
comprador_compulsivo=(promedio > 69)

#output
print("##################################")
print("# recibo de luz #")
print("##################################")
print("enero: ",enero,"      #")
print("febrero: ",febrero,"  #")
print("marzo: ",marzo,"      #")
print("abril: ",abril,"      #")
print("mayo: ",mayo,"        #")
print("junio: ",junio,"      #")
print("igv: ",igv,"          #")
print("##################################")
print("promedio: ",promedio,"   #")
print("comprador compulsivo: ",comprador_compulsivo,"   #")
print("##################################")


#tienda online bellisima
#declaracion de variables
cliente,numero_de_tarjeta,polvo_compacto,rubor,labiales,aretes="","",0.0,0.0,0.0,0.0

#input
cliente=input("cliente:")
numero_de_tarjeta=input("numero de tarjeta:")
polvo_compacto=float(input("ingrese polvo compacto:"))
rubor=float(input("ingrese rubor:"))
labiales=float(input("ingrese labial:"))
aretes=float(input("ingrese aretes:"))

#processing
total=(polvo_compacto+rubor+labiales+aretes*2)

#detector
#comprador compulsivo cuando el total > 50
comprador_compulsivo=(total > 50)

#output
print("###########################################")
print("# tienda online #")
print("###########################################")
print("cliente: ",cliente,"      #")
print("numero de tarjeta: ",numero_de_tarjeta,"  #")
print("polvo compacto: ",polvo_compacto,"        #")
print("rubor: ",rubor,"                          #")
print("labiales: ",labiales,"                    #")
print("aretes: ",aretes,"                        #")
print("###########################################")
print("total: ",total,"                          #")
print("comprador compulsivo: ",comprador_compulsivo,"   #")
print("###########################################")


#conducta del colegio jesus mi amigo en los 4 preros meses
#declaracion de variables
nombre,primer_bimestre,segundo_bimestre,tercer_bimestre,cuarto_bimestre="",0,0,0,0

#input
nombre=input("ingrese nombre:")
primer_bimestre=int(input("ingrese primer bimestre:"))
segundo_bimestre=int(input("ingrese segundo bimestre:"))
tercer_bimestre=int(input("ingrese tercer bimestre:"))
cuarto_bimestre=int(input("ingrese cuarto bimestre:"))

#processing
promedio=(primer_bimestre+segundo_bimestre+tercer_bimestre+cuarto_bimestre)/4

#detector
#comprador compulsivo cuando el promedio > 20
comprador_compulsivo=(promedio > 20)

#output
print("###########################################")
print("# conducta de jesus mi amigo #")
print("###########################################")
print("primer bimestre: ",primer_bimestre,"      #")
print("segundo bimestre: ",segundo_bimestre,"    #")
print("tercer bimestre: ",tercer_bimestre,"      #")
print("cuarto bimestre: ",cuarto_bimestre,"      #")
print("###########################################")
print("promedio: ",promedio,"                    #")
print("comprador compulsivo: ",comprador_compulsivo,"  #")
print("###########################################")



#convertir cadena "123" a un entero
x="123"
a=int(x)
print(a, type(a))

#convertir entero (12) a un real
x=(12)
b=float(x)
print(b, type(b))


#convertir cadena "6211.02" a un real
x="6211.02"
c=float(x)
print(c, type(c))


#convertir cadena "32" a un entero
x="32"
d=int(x)
print(d, type(d))


#convertir entero (12) a una cadena
x=(12)
e=str(x)
print(e, type(e))




#boleta de la compra de repuestos para moto
#declaracion de variables
neumaticos,armadura_doble,fibra_de_carbono,cadena_unitaria=0.0,0.0,0.0,0.0

#input
neumaticos=float(input("ingrese neumaticos:"))
armadura_doble=float(input("ingrese armadura doble:"))
fibra_de_carbono=float(input("ingrese fibra de carbono:"))
cadena_unitaria=float(input("ingrese cadena unitaria:"))

#processing
total_a_pagar=(neumaticos+armadura_doble+fibra_de_carbono+cadena_unitaria)

#output
print("#################################")
print("# boleta de compra de repuestos para moto #")
print("#####################################")
print("neumaticos: ",neumaticos,"             #")
print("armadura_doble: ",armadura_doble,"    #")
print("fibra_de_carbono: ",fibra_de_carbono,"   #")
print("cadena_unitaria: ",cadena_unitaria,"     #")
print("########################################")
print("total_a_pagar: ",total_a_pagar,"          #")
print("##########################################")


#boleta de medicamentos en solidaridad
#declaracion de variables
nombre_del_paciente,paracetamol,diclofenaco,doloneurobion="",0.0,0.0,0.0

#input
nombre_del_paciente=input("ingrese nombre del paciente:")
paracetamol=float(input("ingrese paracetamol:"))
diclofenaco=float(input("ingrese diclofenaco:"))
doloneurobion=float(input("ingrese doloneurobion:"))

#processing
monto_a_pagar=(paracetamol+diclofenaco+doloneurobion)

#output
print("##############################")
print("# boleta de medicamentos #")
print("##############################")
print("nombre_del_paracetamol: ",nombre_del_paciente,"    #")
print("paracetamol: ",paracetamol,"     #")
print("diclofenaco: ",diclofenaco,"     #")
print("doloneurobion: ",diclofenaco,"   #")
print("##############################")
print("monto_a_pagar: ",monto_a_pagar,"  #")
print("##############################")


#formulario para el comedor universitario
#declaracion de variables
nombre_del_solicitante,edad,ano_de_inscripcion,pago_mensual_por_cinco_años="",0,"",0.0

#input
nombre_del_solicitante=input("ingrese nombre del solicitante:")
edad=int(input("ingrese edad:"))
ano_de_inscripcion =input("ingrese ano de ingreso:")
pago_mensual=float(input("ingrese pago mensual:"))

#processing
monto_total=(pago_mensual*5)

#output
print("##################################")
print("# formulario para el comedor #")
print("##################################")
print("nombre del solicitante: ",nombre_del_solicitante,"  #")
print("edad: ",edad,"    #")
print("ano de inscripcion: ",ano_de_inscripcion,"  #")
print("pago mensual: ",pago_mensual,"  #")
print("##################################")
print("monto_total: ",monto_total,"   #")
print("##################################")



#promedio de gastos de la empresa de textiles sully
#declaracion de variables
tela_animal_print,hilo_blanco,hilo_rojo,maquina_remalladora=0.0,0.0,0.0,0.0

#input
tela_animal_print=float(input("ingrese teta animal print:"))
hilo_blanco=float(input("ingrese hilo blanco:"))
hilo_rojo=float(input("ingrese hilo rojo:"))
maquina_remalladora=float(input("ingrese maquina remalladora:"))

#processing
prom=(tela_animal_print+hilo_blanco+hilo_rojo+maquina_remalladora)/4

#output
print("##################################")
print("# promedio de la fabrica textil #")
print("##################################")
print("tela animal print: ",tela_animal_print,"  #")
print("hilo blanco: ",hilo_blanco,"  #")
print("hilo rojo: ",hilo_rojo,"  #")
print("maquina remalladora: ",maquina_remalladora,"   #")
print("##################################")
print("prom: ",prom,"      #")
print("##################################")



#boleta electronica de sodicac
#declaracion de variables
nombre_del_comprador,puerta_acrilica,martillo,pernos,cementos,tablas,igv="",0.0,0.0,0.0,0.0,0.0,0.0

#input
nombre_del_comprador=input("ingrese nombre:")
puerta_acrilica=float(input("ingrese puerta acrilica:"))
martillo=float(input("ingrese martillo:"))
pernos=float(input("ingrese pernos:"))
cementos=float(input("ingrese cemento:"))
tablas=float(input("ingrese tabla:"))
igv=float(input("ingrese igv:"))

#processing
total_a_pagar=(puerta_acrilica+martillo+pernos+cementos*2+tablas+igv)

#output
print("##################################")
print("# boleta electronica de sodimac  #")
print("##################################")
print("nombre del comprador: ",nombre_del_comprador,"  #")
print("puerta acrilica: ",puerta_acrilica,"      #")
print("martillo: ",martillo,"        #")
print("pernos: ",pernos,"            #")
print("cementos: ",cementos,"        #")
print("tablas: ",tablas,"            #")
print("igv: ",igv,"                  #")
print("##################################")
print("total a pagar: ",total_a_pagar,"  #")
print("##################################")



#paquete de viajes para familias
#declaracion de variables
nombre,pasaje1,pasaje2,pasaje3,pasaje4,igv="",0.0,0.0,0.0,0.0,0.0

#input
nombre=input("ingrese nombre:")
pasaje1=float(input("ingrese pasaje1:"))
pasaje2=float(input("ingrese pasaje2:"))
pasaje3=float(input("ingrese pasaje3:"))
pasaje4=float(input("ingrese pasaje4:"))
igv=float(input("ingrese igv:"))

#processing
total=(pasaje1+pasaje2+pasaje3+pasaje4)

#output
print("##################################")
print("# paquete de viajes para familia #")
print("nombre: ",nombre,"               #")
print("pasaje1: ",pasaje1,"             #")
print("pasaje2: ",pasaje2,"             #")
print("pasaje3: ",pasaje3,"             #")
print("pasaje4: ",pasaje4,"             #")
print("igv: ",igv,"                     #")
print("##################################")
print("total: ",total,"                 #")
print("##################################")


#sacar copia de un libro
#declaracion de variables
nombre_del_libro,nro_de_hojas,precio_por_hoja="",0,0.0

#out
nombre_del_libro=input("ingrese nombre del libro:")
nro_de_hojas=int(input("ingrese nro de hojas:"))
precio_por_hoja=float(input("ingrese precio por hoja:"))

#processing
total=(nro_de_hojas*precio_por_hoja)

#output
print("##################################")
print("# sacar copia de un libro #")
print("##################################")
print("nombre del libro: ",nombre_del_libro,"  #")
print("nro de hojas: ",nro_de_hojas,"     #")
print("precio por hoja: ",precio_por_hoja,"    #")
print("##################################")
print("total: ",total,"                      #")
print("##################################")


#recibo de luz de los 6 primeros meses
#declaracion de variables
enero,febrero,marzo,abril,mayo,junio,igv=0.0,0.0,0.0,0.0,0.0,0.0,0.0

#input
enero=float(input("ingrese enero:"))
febrero=float(input("ingrese febrero:"))
marzo=float(input("ingrese marzo:"))
abril=float(input("ingrese abril:"))
mayo=float(input("ingrese mayo:"))
junio=float(input("ingrese junio:"))
igv=float(input("ingreso igv:"))

#processing
promedio=(enero+febrero+marzo+abril+mayo+junio+igv)/7

#output
print("##################################")
print("# recibo de luz #")
print("##################################")
print("enero: ",enero,"      #")
print("febrero: ",febrero,"  #")
print("marzo: ",marzo,"      #")
print("abril: ",abril,"      #")
print("mayo: ",mayo,"        #")
print("junio: ",junio,"      #")
print("igv: ",igv,"          #")
print("##################################")
print("promedio: ",promedio,"   #")
print("##################################")

#tienda online bellisima
#declaracion de variables
cliente,numero_de_tarjeta,polvo_compacto,rubor,labiales,aretes="","",0.0,0.0,0.0,0.0

#input
cliente=input("cliente:")
numero_de_tarjeta=input("numero de tarjeta:")
polvo_compacto=float(input("ingrese polvo compacto:"))
rubor=float(input("ingrese rubor:"))
labiales=float(input("ingrese labial:"))
aretes=float(input("ingrese aretes:"))

#processing
total=(polvo_compacto+rubor+labiales+aretes*2)

#output
print("###########################################")
print("# tienda online #")
print("###########################################")
print("cliente: ",cliente,"      #")
print("numero de tarjeta: ",numero_de_tarjeta,"  #")
print("polvo compacto: ",polvo_compacto,"        #")
print("rubor: ",rubor,"                          #")
print("labiales: ",labiales,"                    #")
print("aretes: ",aretes,"                        #")
print("###########################################")
print("total: ",total,"                          #")
print("###########################################")


#conducta del colegio jesus mi amigo en los 4 preros meses
#declaracion de variables
nombre,primer_bimestre,segundo_bimestre,tercer_bimestre,cuarto_bimestre="",0,0,0,0

#input
nombre=input("ingrese nombre:")
primer_bimestre=int(input("ingrese primer bimestre:"))
segundo_bimestre=int(input("ingrese segundo bimestre:"))
tercer_bimestre=int(input("ingrese tercer bimestre:"))
cuarto_bimestre=int(input("ingrese cuarto bimestre:"))

#processing
promedio=(primer_bimestre+segundo_bimestre+tercer_bimestre+cuarto_bimestre)/4

#output
print("###########################################")
print("# conducta de jesus mi amigo #")
print("###########################################")
print("primer bimestre: ",primer_bimestre,"      #")
print("segundo bimestre: ",segundo_bimestre,"    #")
print("tercer bimestre: ",tercer_bimestre,"      #")
print("cuarto bimestre: ",cuarto_bimestre,"      #")
print("###########################################")
print("promedio: ",promedio,"                    #")
print("###########################################")
