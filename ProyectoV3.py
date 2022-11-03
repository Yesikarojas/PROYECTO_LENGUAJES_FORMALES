import re
from unicodedata import normalize


def viasUrbanas(direccion):
    res = 0
    vias=["transversal","calle", "cll", "cl", "c","carrera", "crr", "cr", "crra","avenida", "av", "ave", "avnd","kr","diagonal"]


    for via in vias:
        
        if via == direccion:
            #print("Comparacion urbana", via, " ddd ", direccion)
            res = 1

    return res




def viasRurales(direccion):
    res = 0

    via=["Via","v", "V", "VIA", "via"]

    for vias in via:
        
        if vias == direccion:
            #print("Comparacion rural", vias)
            res=2

    return res


def eRUrbanas(direcciones):

    direccion= direcciones.lower()
    

    dParte= direccion.split(" ")
    #dParte= dParte1.split(",")
    cont=0 
    if re.findall('avenida|av',dParte[cont]):
        #inicio
         if re.findall('[carrera|crr|cr|crra|kr|calle|cll|cl|c]', dParte[cont]):
            cont+=1
            #print("----------------Entro a 32A")
            if re.findall('[a-z]?\s?[Norte|norte|NORTE|Sur|SUR|sur|N|S|norte|n|sur|s|este|e|oeste|o]?', dParte[cont]):
                cont+=1
                print("entro sur------------",dParte[cont])
                if re.findall('[A-Z]?[a-z]', dParte[cont]):
                    cont+=1
                    #print("entro letra sur------------")
                    if re.findall('[numero|#|n°|n.°|num]', dParte[cont]):
                        cont+=1
                        #print("entro numero------------")
                        if re.findall('[0-9]{1,3}?[-]?[0-9]{1,3}?[a-z]?', dParte[cont]):
                            cont+=1
                            print("La direccion es valida ")

                            if re.findall('[a-z]?[0-9]{1,3}?[-]?[0-9]{1,3}?', dParte[cont]):
                                cont+=1
                               # print("letraaaa")
                        elif re.findall('[Norte|norte|NORTE|Sur|SUR|sur|N|S|este|e|oeste|norte|n|sur|s|o]?', dParte[cont]):
                            cont+=1
                            print("La direccion es valida")
                #inicio
                elif re.findall('[numero|#|n°|n.°|num]', dParte[cont]):
                    cont+=1
                   # print("hola")
                    #inicio
                    if re.findall('[0-9]{1,3}?[-]?[0-9]{1,3}?[a-z]?', dParte[cont]):
                        cont+=1
                        print("La direccion es valida ")

                        if re.findall('[a-z]?[0-9]{1,3}?[-]?[0-9]{1,3}?', dParte[cont]):
                            cont+=1
                            #print("letraaaa")
                    elif re.findall('[Norte|norte|NORTE|Sur|SUR|sur|N|S|este|e|oeste|norte|n|sur|s|o]?', dParte[cont]):
                        cont+=1
                        print("Esta direccion es valida")
        #fin
    elif re.findall('(autopista|aut|boulevard|blv|calle|cll|cl|camino|cn|carrera|cra|cr|kr|kra|carretera|carr|crt|circunvalar|crv|ciudadela|cd|callejon|clj|diagonal|dia|dg|transversal|transv|tv|urbanizacion|urb|variante|vte|kr|diagonal|calle|cll|cl|c|Calle|Cll|Cl|C|CALLE|CLL|CL|C|autopista|au|avenida|av|ak|bis|bulevar|bl|carrera|calle|cl|kr|carretera|ct|circular|cq|circunvalar|cc|cv|paseo|ps|via|vi|vereda|vda|vd|kilometro|km|peatonal|pt|vt|transversal|variante|tc|tv|diagonal|troncal|dg|pasaje|pj|cll|krr)', dParte[cont]):
        
        cont +=1
        #print("-------------------paso", dParte[cont])

        if re.findall('[0-9]{1,3}\s?[a-z]?[bis]?', dParte[cont]):
            cont+=1
            #print("----------------Entro a 32A")
            if re.findall('[a-z]?\s?[Norte|norte|NORTE|Sur|SUR|sur|N|S|este|e|oeste|norte|n|sur|s|o]?', dParte[cont]):
                
                cont+=1
                #print("entro sur------------", dParte[cont])
                if re.findall('[a-z]', dParte[cont]):
                    cont+=1
                    #print("entro letra sur------------")
                    if re.findall('[numero|#|n°|n.°|num]', dParte[cont]):
                        cont+=1
                        #print("entro numero------------")
                        if re.findall('[0-9]{1,3}?[-]?[0-9]{1,3}?[a-z]?', dParte[cont]):
                            cont+=1
                            print("La direccion es valida ")

                            if re.findall('[a-z]?[0-9]{1,3}?[-]?[0-9]{1,3}?', dParte[cont]):
                                cont+=1
                               # print("letraaaa")
                        elif re.findall('[Norte|norte|NORTE|Sur|SUR|sur|N|S|este|e|oeste|norte|n|sur|s|o]?', dParte[cont]):
                            cont+=1
                            print("Esta direccion es valida")
                    #inicio
                    elif re.findall('[0-9]{1,3}?', dParte[cont]):
                        count+=1
                        if re.findall('[A-Z]?[a-z]', dParte[cont]):
                            cont+=1
                            #print("entro letra sur------------")
                            if re.findall('[numero|#|n°|n.°|num]', dParte[cont]):
                                cont+=1
                               # print("entro numero------------")
                                if re.findall('[0-9]{1,3}?[-]?[0-9]{1,3}?[a-z]?', dParte[cont]):
                                    cont+=1
                                    print("La direccion es valida ")

                                    if re.findall('[a-z]?[0-9]{1,3}?[-]?[0-9]{1,3}?', dParte[cont]):
                                        cont+=1
                                       # print("letraaaa")
                                elif re.findall('[Norte|norte|NORTE|Sur|SUR|sur|N|S|este|e|oeste|norte|n|sur|s|o]?', dParte[cont]):
                                    cont+=1
                                    print("Esta direccion es valida")
                                
                    #fin
                    else:
                        print("La direccion no es valida")
                elif re.findall('[numero|#|n°|n.°|num]', dParte[cont]):
                    cont+=1
                    #print("hola")
                    #inicio
                    if re.findall('[0-9]{1,3}?[-]?[0-9]{1,3}?[a-z]?', dParte[cont]):
                        cont+=1
                        print("La direccion es valida ")

                        if re.findall('[a-z]?[0-9]{1,3}?[-]?[0-9]{1,3}?', dParte[cont]):
                            cont+=1
                            #print("letraaaa")
                    elif re.findall('[Norte|norte|NORTE|Sur|SUR|sur|N|S|este|e|oeste|norte|n|sur|s|o]?', dParte[cont]):
                        cont+=1
                        print("La direccion es valida")
                    #fin
                elif  re.findall('[a-z]?[0-9]{1,3}?[-]?[0-9]{1,3}?', dParte[cont]):
                    print("La direccion es valida")

       
                    #fin
        #elif re.findall('[0-9]{1,3}[a-z]?[bis|BIS|Bis]?', dParte[cont]):
         #   cont+=1
         #   print("-------------------Entro a 32a")
        else:
            print("La direccion no es valida")
 #   elif re.findall('', dParte[cont]):
  #      cont +=1




def comparar(direccion):
    dParte = direccion.split(" ")
    dirComas = comas(direccion)

    if viasUrbanas(dParte[0])==1:
        print(direccion)
        print("    ----------------  La via es urbana ---------")
        #print("---------------------------> comaaaaaaasss   -------    ",dirComas)
        eRUrbanas(direccion)
      
        
    elif viasRurales(dParte[0])==2:
        print(direccion, " ----------------------- La via es rural -------------------- ")
    else:
        print(direccion, "n/La direccion ingresada no es vaida")




#Quitamos las tildes de todas las direcciones para no tener problemas 
def tildes(direccion):
    res = direccion
    res = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        normalize( "NFD", res), 0, re.I
    )

    # -> NFC
    direccion = normalize( 'NFC', res)
    #print("Entra ----", direccion)
    #print("Sale direccion",res)

    return res


def comas(direcciones):
    aux = direcciones.split(",")
    #Devuelve una lista
    return aux[0]



#Metodo para correr el programa y obtener las direcciones de un txt y guardarlas en una lista
def runner():

    datos = []
    counter=0
    with open("direcciones.txt",encoding="utf8") as fname:
        lineas = fname.readlines()
        
    for linea in lineas:
        #aux=tildes(linea.strip('\n')).split(",")
        #print("---------------------  ------------- ", aux)
        #datos.append(tildes(linea.strip('\n')))
        datos.append(tildes(linea.strip('\n')))
    
            
    for dir in datos:
        #print("Direccion: ",dir)
        counter+=1
        print(counter)
        
        comparar(dir.lower())
        #tildes(dir)
        #print("dir ------ ",dir)
   
#Defino los estados para las transiciones


  
runner()