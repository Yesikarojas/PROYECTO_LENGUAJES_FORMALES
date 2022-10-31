
import re

class State(object):
    def __init__(self, name, next_state, trans, output):
        self.name = name
        self.next_state = next_state
        self.trans = trans
        self.output = output
        
    def return_name(self):
        return self.name
    
    def return_input(self):
        return self.next_state
    
    def return_trans(self):
        return self.trans

    def return_output(self):
        return self.output


def SplitWord(palabra):
    
    res=palabra.split()
   # for palabras in res:
    #    print(res)
    #print(res[2])

    return res

def AddStates():
    stateL = []

    trans0 = ["q1", "q2"]
    trans1 = ["q2"]
    
    state0 =State("q0", trans0, "^(avenida|calle|carrera|transversal|diagonal)", 0)
    state1 =State("q1", trans1, "(Avenida carrera+avenida carrera+Ac+Av+avenida+AC+ac+AV+av+AVENIDA+AVENIDA CARRERA+Avenida+Avenida Carrera)", 0)

    stateL.append(state0)
    stateL.append(state1)

    return stateL

stateL = AddStates()

def Secuence(i, word):

    
    varAux = []

    print(word[0])
    cont = 0
    #if i>= len(word):
    for wordAux in word:
        #print("holad",cont)
        #print(word[cont], "    ------------     ", stateL[cont].trans )
        if re.search(word[cont], stateL[cont].trans ) is not None:
               print("Aceptado --- ",i)
                #varAux[i]=stateL[cont].name
        else:
                print("No se ha aceptado la direccion")
        cont+=1    
    #else:
    #    print("Hola",len(word))
    #    for w in word:
     #       print(word)
     #   print("El numero de palabras en la direccion es mayor que el numero de estados, NO SE HA ACEPTADO")

def Runner():
    print("Bienvenido")
    cont = 0
    word = SplitWord(input("Ingrese la direccion "))
    for i in stateL:
        Secuence(cont, word)
        cont +=1

Runner()


