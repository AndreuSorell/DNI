from tabla_asignacion import *

class Dni():
    def __init__(self, dni = ''):
        self.dni = dni
        self.tabla = TablaAsignacion()
    
    def get_dni(self):
        return self.dni

    def set_dni(self, nuevo_dni):
        self.dni = nuevo_dni

    def check_dni(self):
        if (self.check_numero_dni() and self.check_letra()):
            return 'El DNI es correcto'
        else:
            return 'El DNI es incorrecto'

    def check_numero_dni(self):
        # comprobar que la longitud es correcta y que es un int
        numero_dni = self.dni[:-1]
        if (len(numero_dni) == 8 and numero_dni.isdigit()):
            return True
        else:
            return False

    def check_letra(self):
        numero_dni = self.dni[:-1]
        if self.tabla.calculo_letra(numero_dni) == self.dni[-1]:
            return True
        else:
            return False

if __name__ == '__main__':
    dni1 = Dni('78221620T')
    print(dni1.get_dni())
    print(dni1.check_numero_dni())
    print(dni1.check_letra())
    print(dni1.check_dni())
    dni1.set_dni('78221621T')
    print(dni1.get_dni())
    print(dni1.check_dni())