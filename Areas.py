def area_triangulo(base,altura):
    """Calcula el area de un triangulo dada su base y su altura"""
    area=(base)*(altura)/2
    return print("El triangulo tiene un area de {:.2f} cm^2\n".format(area))

def area_circulo(radio):
    """Calcula el area de un circulo dado su radio """
    area=3.14*(radio**2)
    return print("El circulo tiene un area de {:.2f} cm^2\n".format(area))

def area_rectangulo(alto,ancho):
    """Calcula el area de un rectangulo dado sus lados"""
    area=alto*ancho
    return print("El rectangulo tiene un area de {:.2f} cm^2\n".format(area))

def area_dona(radio_menor, radio_mayor):
    """Calcula el area de una dona apartir de un radio mayor y un radio menor"""
    area= (3.14*(radio_mayor**2))- (3.14*(radio_menor**2))
    return print("La dona tiene un area de {:.2f} cm^2\n".format(area))

def area_rombo(diagonal1,diagonal2):
    """Calcula el area de un rombo apartir de sus diagonales"""
    area=diagonal1*diagonal2/2
    return print("EL rombo tiene un area de {:.2f} cm^2\n".format(area))

def menu():
    """Menu del programa con las opciones"""
    print("******** Areas *********\nMarque una opcion:")
    print("1- Triangulo\n2- Circulo\n3- Rectangulo\n4- Dona\n5- Rombo\n0 - Salir\n")
    opcion=int(input())
    while opcion!=0:
        if opcion==1:
            base=float(input("Escriba cuanto mide la base (en cm): "))
            altura=float(input("Indique cuanto mide la altura(en cm): "))
            area_triangulo(base,altura)
        elif opcion==2:
            radio=float(input("Escriba cuanto mide el radio(en cm): "))
            area_circulo(radio)
        elif opcion==3:
            alto=float(input("Indique la atura (en cm): "))
            ancho=float(input("Inque el ancho (en cm): "))
            area_rectangulo(alto,ancho)
        elif opcion==4:
            radio_mayor=float(input("Indique cuanto mide el radio mayor (en cm): "))
            radio_menor=float(input("Indique cuanto mide el radio menor (en cm): "))
            area_dona(radio_menor,radio_mayor)
        elif opcion==5:
            diagonal1=float(input("Indique cuanto mide la diagonal mayor (en cm): "))
            diagonal2=float(input("Indique cuanto mide la diagonal menor(en cm): "))
            area_rombo(diagonal1,diagonal2)
        else:
            print("Opcion invalida, intente nueva mente")
        print("Marque una opcion:\n1- Triangulo\n2- Circulo\n3- Rectangulo\n4- Dona\n5- Rombo\n0-Salir")
        opcion=int(input())

menu()
