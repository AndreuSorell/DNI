from tabla_asignacion import *

class Dni():
    def __init__(self, dni = ''):
        self.dni = dni
        self.tabla = TablaAsignacion()
    
    def get_dni(self):
        return self.dni

    def set_dni(self, nuevo_dni):
        self.dni = nuevo_dni
        print(self.dni)

    """ 
    def check_numero_dni(self):
        comprobar que la longitud es correcta y que es un int
    """

    def check_letra(self):
        numero_dni = self.dni[:-1]
        if self.tabla.caluclo_letra(numero_dni) == self.dni[-1]:
            print('La letra es correcta')
        else:
            print('El dni no es correcto')

if __name__ == '__main__':
    dni1 = Dni('78221620T')
    print(dni1.get_dni())
    dni1.check_letra()
    dni1.set_dni('78221621T')
    print(dni1.get_dni())
    dni1.check_letra()