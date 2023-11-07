# Online Python - IDE, Editor, Compiler, Interpreter

prueba={"Comun":['a', 'b', 'c','d',], "Arcano":['1','2','3','4']};

#def test(x):
#    print(x)    
key_list = list(prueba.keys())    
value_list = list(prueba.values())     
print(key_list)
print(value_list)


def idAlfabetoPorLetra(var):
    pos = [i for (i, x) in enumerate(value_list) if var in x]
    print(key_list[pos[0]])  

def traducir(alfab1, alfab2, texto):
    texto_trad=""
    for letra in texto:
        print(letra)
    return

idAlfabetoPorLetra('1')
traducir('Comun', 'Arcano', "abcd")