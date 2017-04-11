import numpy as np

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
    return ans


metodos =[]
params = {}
const = {}
revparams =  {}

#archivo que vamos a leer
file = open("ejemplo.dat")
#archivo al que escribiremos
outf = open('ecuaciones.py', 'w')
#solo creo que necesitaremos numpy, igual ese archivo solo se va a importar en otro
print("import numpy as np",file= outf)
#primero van las constantes
#vamos a meterlas en un diccionario, facilita mucho la vida
linea = file.readline()
print("#constantes",file = outf)

while(not linea.startswith("------")):


    linea = file.readline()
    if(not linea.startswith("#") and not linea.startswith("------")):
        key = linea.split("=")[0].strip()
        val = float(linea.split("=")[1].strip())
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
    funcArray.append(i[0])
newFuncArray = ""
funcArray = str(funcArray)
for i in funcArray:
    if(i!="\'"):
        newFuncArray += i
print("funcArray = " + str(newFuncArray),file = outf)
#Y salio para pintura
outf.close()
file.close()
