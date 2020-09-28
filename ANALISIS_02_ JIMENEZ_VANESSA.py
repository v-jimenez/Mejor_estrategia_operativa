
#Importando archivo csv a diccionario con función open y DictReader

import csv

path = "E:/Cursos/Data Science EmTech/Primer_Proyecto/synergy_logistics_database.csv"

exp_global = []
imp_global = []

with open(path,"r") as archivo_csv:
    lector = csv.DictReader(archivo_csv)

#Obteniendo el valor total y promedio de importaciones 
# y exportaciones con la función de sum y de len

    for linea in lector:
        if linea["total_value"] != 0 and linea["direction"] == "Exports":
            exp_global.append(int(linea["total_value"]))
        else: 
            if linea["total_value"] != 0:
                imp_global.append(int(linea["total_value"]))

export_totales_globales = sum(exp_global)
import_totales_globales = sum(imp_global)

promedio_exp_totales = sum(exp_global) / len(exp_global)
promedio_imp_totales = sum(imp_global) / len(imp_global)
      
print("Exportaciones totales globales: ", export_totales_globales )
print("Importaciones totales globales: ", import_totales_globales)
          
valor_total_movimientos = export_totales_globales + import_totales_globales

print("Valor total: ", valor_total_movimientos)

#Obteniendo mediante conjuntos los países exportadores,
# importadores, y el total de países en general

paises_origen = set()

with open(path,"r") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    archivo_csv.seek(0)
    for linea in lector:
        paises_origen.add(linea["origin"])

print("\n" "Países que mandan productos: " "\n" ,len(paises_origen), paises_origen)

paises_destino = set()

with open(path,"r") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    archivo_csv.seek(0)

    for linea in lector:
        paises_destino.add(linea["destination"])

print("\n""Países que reciben productos: " "\n" ,len(paises_destino), paises_destino)


paises = paises_origen.union(paises_destino)

print("\n" "Total de países: ", len(paises), paises)

# Obteniendo mediante lista, las rutas y medios de transporte
# de las exportaciones, además de sumar su valor total y
# guardándolo en un diccionario

lista_datos = []

with open(path,"r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    
    for linea in lector:
        lista_datos.append(linea)

las_rutas_exp = {}

for row in lista_datos[1:]:
    if row[1] == "Exports":
        la_ruta = row[2],row[3],row[7]
        if la_ruta in las_rutas_exp:
            las_rutas_exp[la_ruta] += int(row[9])
            
        else:
            las_rutas_exp[la_ruta] = 1

suma_exp = sum(las_rutas_exp.values())

# Obteniendo mediante lista, las rutas y medios de transporte
# de las importaciones, además de sumar su valor total y
# guardándolo en un diccionario. Podría ser una función
# pero se me complicó, aunque después de la entrega ya lo hago
# con más calmita

las_rutas_imp = {}


for row in lista_datos[1:]:
    if row[1] == "Imports":
        la_ruta = row[2],row[3],row[7]
        if la_ruta in las_rutas_imp:
            las_rutas_imp[la_ruta] += int(row[9])
            
        else:
            las_rutas_imp[la_ruta] = 1

suma_imp = sum(las_rutas_imp.values())

# Calculando los porcentajes de las rutas de
# exportaciones e importaciones

porcentajes_exp = {}

for pais in las_rutas_exp:
    porcent_exp = (las_rutas_exp[pais] / suma_exp ) *100
    porcentajes_exp[pais] = porcent_exp
    
porcentajes_imp = {}

for pais in las_rutas_imp:
    porcent_imp = (las_rutas_imp[pais] / suma_imp ) *100
    porcentajes_imp[pais] = porcent_imp

# Obteniendo mediante lista, la frecuencia de los medios 
# de transporte de las importaciones y exportaciones 
# y guardándolo en un diccionario. Sí, también podría ser una
# función

transportes_exp = {}

for row in lista_datos[1:]:
    if row[1] == "Exports":
        transporte_exp = row[7]
        if transporte_exp not in transportes_exp:
            transportes_exp[transporte_exp] = 1
        else:
            transportes_exp[transporte_exp] +=1

transportes_imp = {}

for row in lista_datos[1:]:
    if row[1] == "Imports":
        transporte_imp = row[7]
        if transporte_imp not in transportes_imp:
            transportes_imp[transporte_imp] = 1
        else:
            transportes_imp[transporte_imp] +=1

# Obteniendo mediante lista, el valor total de los medios 
# de transporte de las importaciones y exportaciones
# guardándolo en un diccionario. Podría ser función

los_transportes_exp = {}

for row in lista_datos[1:]:
    if row[1] == "Exports":
        transportee = row[7]
        if transportee in los_transportes_exp:
            los_transportes_exp[transportee] += int(row[9])
            
        else:
            los_transportes_exp[transportee] = 1


los_transportes_imp = {}

for row in lista_datos[1:]:
    if row[1] == "Imports":
        transportei = row[7]
        if transportei in los_transportes_imp:
            los_transportes_imp[transportei] += int(row[9])
            
        else:
            los_transportes_imp[transportei] = 1

# Calculando los porcentajes de los medios de transporte de
# exportaciones e importaciones

porcentajes_t_exp = {}

for transporte in los_transportes_exp:
    porcentajes_t_ex = (los_transportes_exp[transporte] / suma_exp ) *100
    porcentajes_t_exp[transporte] = porcentajes_t_ex
    
porcentajes_t_imp = {}

for transporte in los_transportes_imp:
    porcentajes_t_im = (los_transportes_imp[transporte] / suma_imp ) *100
    porcentajes_t_imp[transporte] = porcentajes_t_im

#Obteniendo la frecuencia de los países y sumando los
# valores totales

los_paises_exp = {}

for row in lista_datos[1:]:
    if row[1] == "Exports":
        el_pais = row[2]
        if el_pais in los_paises_exp:
            los_paises_exp[el_pais] += 1
            
        else:
            los_paises_exp[el_pais] = 1

suma_p_exp = sum(los_paises_exp.values())

los_paises_imp = {}

for row in lista_datos[1:]:
    if row[1] == "Imports":
        el_pais = row[3]
        if el_pais in los_paises_imp:
            los_paises_imp[el_pais] += 1
            
        else:
            los_paises_imp[el_pais] = 1

suma_p_imp = sum(los_paises_imp.values())

# Calculando los porcentajes de los países de
# exportaciones e importaciones

porcentajes_p_exp = {}

for pais in los_paises_exp:
    porcent_exp = (los_paises_exp[pais] / suma_p_exp ) *100
    porcentajes_p_exp[pais] = porcent_exp
    
porcentajes_p_imp = {}

for pais in los_paises_imp:
    porcent_imp = (los_paises_imp[pais] / suma_p_imp ) *100
    porcentajes_p_imp[pais] = porcent_imp

# Combinando todas las consignas para saber las mejores rutas,
# poniendo en lista los
# países y transportes que aportan las mayores ganancias,
# y el año para compararlos en cualquier momento. También 
# creo que podría convertirse en una función donde se indique
# el país, año y medio de transporte.

mejores_paises = [ "Thailand","China","Mexico","Japan",
                  "Germany", "United Arab Emirates","USA",
                  "Australia","South Korea","France",
                  "United Kingdom" ]

mejores_transportes = ["Sea", "Rail","Air"]

fecha_reciente = ["2015","2016","2017","2018","2019", "2020"]

mejores_importaciones = {}

for row in lista_datos[1:]:
    if row[1] == "Imports" and row[3] in mejores_paises:
        if row[7] in mejores_transportes and row[4] in fecha_reciente:
            formato = row[2],row[3],row[4], row[7]
            if formato in mejores_importaciones:
                mejores_importaciones[formato] += int(row[9])
            
            else:
                mejores_importaciones[formato] = 1

suma_mejores_imp = sum(mejores_importaciones.values())

mejores_exportaciones = {}

for row in lista_datos[1:]:
    if row[1] == "Exports" and row[3] in mejores_paises:
        if row[7] in mejores_transportes and row[4] in fecha_reciente:
            formato = row[2],row[3],row[4], row[7]
            if formato in mejores_exportaciones:
                mejores_exportaciones[formato] += int(row[9])
            
            else:
                mejores_exportaciones[formato] = 1

suma_mejores_exp = sum(mejores_exportaciones.values())

# Calculando los porcentajes de las mejores rutas de
# exportaciones e importaciones

porcentajes_mejores_exp = {}

for ruta in mejores_exportaciones:
    porcent_exp = (mejores_exportaciones[ruta] / suma_mejores_exp ) *100
    porcentajes_mejores_exp[ruta] = porcent_exp
    
porcentajes__mejores_imp = {}


for ruta in mejores_importaciones:
    porcent_imp = (mejores_importaciones[ruta] / suma_mejores_imp ) *100
    porcentajes__mejores_imp[ruta] = porcent_imp




# Y este código es aparte, sólo es para consulta en caso de
# querer contar mediante dirección y destino algún país en
# particular

pais_imp = {}

for row in lista_datos[1:]:
    if row[1] == "Imports" and row[3] == "Australia":
        pais_destino = row[3]
        if pais_destino in pais_imp:
            pais_imp[pais_destino] += 1
            
        else:
            pais_imp[pais_destino] = 1

print(pais_imp)



