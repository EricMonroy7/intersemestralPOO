from cosas import Alumno, Perro
                                                          A :
def main():
    all = Alunno("jose",19, "ICO")
    print(vars(al1))
    al1.__nombre ="Diego"
    print(vars(al1))
    al1.set_nombre("Maria")
    print(vars(al1))
    print("-----To string ----")
    print(all)
    al1.set_edad(999)
    print(all)
    all.estudiar (4)
    print("-- PERRO ---")
    perro1 = Perro("Poddle", 2, 0.35)
    print(vars(perro1))
    perro1.raza = "De la calle"
    print(vars(perro1))
    perro1.__raza ="otra"
    print(vars(perro1))
    perrol.edad = 12
    perrol.estatura = 0.43
    print(perro1)
    cachore = Perro.es_cachorro(perro1.edad)
    print(cachoro)
    Perro.dormir()
    danes = Perro.perro_grande(0.8)
    print(danes)

main()
