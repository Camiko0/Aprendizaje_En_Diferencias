""" CREA LISTAS """
class listas():
    
    #Crea listas
    def __init__(self):
        self.caract1 = []
        self.caract2 = []
        self.caract3 = []
        self.caract4 = []

    #Inserta valores
    def insertar (self, select, val):
        if select == 1:
            self.caract1.append(val)
        elif select == 2:
            self.caract2.append(val)
        elif select == 3:
            self.caract3.append(val)
        else:
            self.caract4.append(val)

    #Recupera valores
    def recuperar (self):
        return (self.caract1, self.caract2, self.caract3, self.caract4)
