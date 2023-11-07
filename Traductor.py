# Online Python - IDE, Editor, Compiler, Interpreter

alfabeto={"Comun":['a', 'b', 'c','d'],
        "Arcano":['1','2','3','4'],
        "Elfico":['5', '6', '7','8']}


key_list = list(alfabeto.keys())    
value_list = list(alfabeto.values())  
valueSingleList= [item for sublist in alfabeto.values() for item in sublist]



def idAlfabetoPorLetra(letra):
    pos = [i for (i, x) in enumerate(value_list) if letra in x]
    
    return key_list[pos[0]]


def traducir(alfab1, alfab2, texto):
    texto_trad=""
    for letra in texto:
        if letra in alfabeto[alfab1]:
            texto_trad=texto_trad+alfabeto[alfab2][alfabeto[alfab1].index(letra)]
        else:
            texto_trad=texto_trad+letra
    print(texto_trad)


def autoTraducir(alfab, texto):
    for letra in texto:
        if letra in valueSingleList:
            return traducir(idAlfabetoPorLetra(letra), alfab, texto)
    
    
#print(idAlfabetoPorLetra('a'))
#traducir('Comun', 'Arcano', "abcd a")
autoTraducir('Arcano',"abcd a")
