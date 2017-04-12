import numpy as np

#declaramos todo lo que necesitaremos despues
metodos =[]
eventos = []
params = {}
const = {}
revparams =  {}
acciones= []

#esto procesa cada una de las ecuaciones
#que entran en el archivo
def procesarFuncion(linea):

    global metodos
    #vainas malucas para poder leer sin problemas
    #cada linea
    ans = []
    izq = linea.split("=")[0]
    der = linea.split("=")[1].strip()
    der = der.split("@")[1:]
    ans.append(izq)

    temp = ""
    #aca procesamos cada uno de los parametros de la funcion
    for termino in der:
        termino = procesarTermino(termino)


        temp = temp +termino + " "
    ans.append(temp)
    #y lo metemos en un arreglo para despues imprimirlo
    metodos.append(ans)

#esto es lo que procesa cada termino de la funcion
def procesarTermino(termino):
    global params
    #me interesa cambiar lo que esta adentro
    #de los parentesis por un xs[i] definido
    #previamente por los parametros
    ans = ""
    terminoArr = termino.split("{")
    for i in terminoArr:
        subterminoArr = i.split("}")
        for j in subterminoArr:
            if(params.get(j)!=None):
                ans = ans + params[j]

            else:
                ans = ans + j
    eventos.append(ans.strip())
    return ans



#archivo que vamos a leer
file = open("ejemplo.dat")

#archivo al que escribiremos
outf = open('ecuaciones.py', 'w')
#solo creo que necesitaremos numpy, igual ese archivo solo se va a importar en otro

print("hours =1",file=outf)
print("import numpy as np",file= outf)
#primero van las constantes
#vamos a meterlas en un diccionario, facilita mucho la vida
linea = file.readline()
print("#constantes",file = outf)

while(not linea.startswith("------")):


    linea = file.readline()
    if(not linea.startswith("#") and not linea.startswith("------")):
        key = linea.split("=")[0].strip()
        val = (linea.split("=")[1].strip())
        const[key] = val
        print(linea,file = outf)
print("const = "+str(const),file = outf)
#siguen los valores iniciales
linea = file.readline()
initVals = []
print("#valores iniciales",file = outf)
while(not linea.startswith("------")):
    #solo queremos las lineas que no sean un comentario
    if(not linea.startswith("#")):

        #metemos los parametros en un diccionario y
        #en un diccionario reversado, esto nos sera util despues
        preParam = linea.split("=")[0].strip()
        sizepar = len(params)
        params[preParam] = "xs"+"["+str(sizepar)+"]"
        revparams["xs"+"["+str(sizepar)+"]"] = preParam


        initVals.append(float(linea.split("=")[1].strip()))
    linea = file.readline()
print("initVals = " + str(initVals),file = outf)

#metemos los parametros al archivo
print("#parametros en el diccionario",file = outf)

print("params = " + str(params),file = outf)
#y los parametros reversados tambien
print("#parametros en el diccionario reversados",file = outf)
print("revparams = " + str(revparams),file = outf)
linea = file.readline()
#procesamos cada una de las funciones
while(not linea.startswith("------")):
    procesarFuncion(linea)
    linea = file.readline()

#ahora van las ecuaciones diferenciales
print("#ecuaciones diferenciales",file=outf)

for i in range(len(metodos)):
    #imprimos el encabezado de la funcion
    aimprimir = "def " + metodos[i][0].strip()+"(xs,const,t):"
    print(aimprimir,file=outf)

    #luego el cuerpo
    aimprimir = "\t"+"return "+metodos[i][1]
    print(aimprimir,file=outf)

#por ultimo, metemos todas las funciones a un arreglo

funcArray =[]

for i in params:
    funcArray.append(i)


newFuncArray = ""
funcArray = str(funcArray)

for i in funcArray:
    if(i!="\'"):
        newFuncArray += i
#y lo imprimimos
print("#arreglo de funciones",file = outf)
print("funcArray = " + str(newFuncArray),file = outf)


linea = file.readline()
cont = 0
#leemos las acciones asociadas a cada evento
while(not linea.startswith("------")):
    if(not linea.startswith("#")):

        subacciones = linea.split(",")
        for i in range(len(subacciones)):
            aAgregar = ""
            if(i!=len(subacciones)-1):
                aAgregar = [float(subacciones[i]),cont]
            else:
                aAgregar = [float(subacciones[i][:-1]),cont]
            acciones.append(aAgregar)
        cont+=1
    linea = file.readline()

eventos = np.array(eventos)
acciones = np.array(acciones)
#tenemos que considerar los casos donde hay eventos que
#se comparten entre ecuaciones
#estas dos listas van a cumplir ese proposito
curatedEvents =[]
curatedActions = []
#quitamos los signos de cada evento
for i in range(len(eventos)):
    eventos[i] = eventos[i][1:]

#esto depura los eventos
for i in range(len(eventos)):
    aMirar = eventos[i]
    #en el caso q se repita el evento
    if(aMirar in curatedEvents):
        curatedEvents = np.array(curatedEvents)
        indices = np.where(eventos==aMirar)[0]
        dondeVa = np.where(curatedEvents==aMirar)[0]
        for j in indices:
            curatedActions[int(dondeVa)][int(acciones[int(j)][1])] =acciones[int(j)][0]
        curatedEvents= curatedEvents.tolist()
    #en el caso que no este dentro de la lista depurada
    else:

        curatedEvents.append(aMirar)
        subactions = np.zeros(len(params))
        subactions[int(acciones[i][1])] = acciones[i][0]
        curatedActions.append(subactions.tolist())

#imprimimos las acciones
print("#acciones",file = outf)
print("actions = " + str(curatedActions),file = outf)

#ademas, sacamos los eventos
newEventos  = "["
for i in curatedEvents:
    ans = ""
    for j in i:
        if(i!="\'"):
            ans += j
    newEventos += (ans)+","
newEventos = newEventos[:-1]
newEventos += "]"
print("#eventos",file = outf)
print("def darEventos(xs):",file = outf)
print("\treturn " + str(newEventos),file = outf)

#Y salio para pintura
outf.close()
file.close()
