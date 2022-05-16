Produccion=dict(
    Enero=1234,
    febrero=5678765,
    marzo=78654,
    abril=87654,
    mayo=9876,
    junio=3565,
    julio=45657,
    agosto=9876,
    septiembre=4546,
    octubre=8764,
    noviembre=3645,
    diciembre=4657,
)

llave_min=min(Produccion.keys(), key=lambda k:Produccion[k])
print('El mes de menor produccion fue:',llave_min,Produccion[llave_min])

llave_max=max(Produccion.keys(), key=lambda k:Produccion[k])
print('El mes de mayor prodducion fue:',llave_max,Produccion[llave_max])

prom=tuple(Produccion.values())
b=len(prom)
suma=0
for val in prom:
    suma+=val
print('El promedio es: ',suma/b)

for key in Produccion.keys():
    if (Produccion[key]>=prom):
        print('El mes',key,'es mayor que es promedio')
        
    elif (Produccion[key]<= prom):
        print(f'El mes:',{key},'es menor que el promedio')
        

