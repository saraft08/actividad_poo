class carta:
    pintas = ('corazones', 'diamantes', 'pica', 'trebol')

    def __init__(self, valor: str, pinta: str):
        self. valor: str = valor
        self.pinta: str = pinta

carta1= carta ('diez', 'corazones')
carta2= carta('rey', 'picas' )
carta3= carta ('dos','trebol')
carta4= carta ('as', 'diamates')

print(f"el valor de la carta es {carta1.valor}, y la pinta de la carta es {carta1.pinta} ")
print(f"el valor de la carta es {carta2.valor}, y la pinta de la carta es {carta2.pinta} ")
print(f"el valor de la carta es {carta3.valor}, y la pinta de la carta es {carta3.pinta} ")
print(f"el valor de la carta es {carta4.valor}, y la pinta de la carta es {carta4.pinta} ")

