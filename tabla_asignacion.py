class TablaAsignacion():

    def __init__(self):
        self.tabla = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']

    def caluclo_letra(self, numero_dni):
        resto = int(numero_dni) % 23
        return self.tabla[resto]

if __name__ == '__main__':
    tabla = TablaAsignacion()
    print(tabla.caluclo_letra(78221620))