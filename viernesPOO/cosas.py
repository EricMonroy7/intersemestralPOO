class Alumno(Persona):
    descripcion = "Una persona que dice que estudia pero se la pasa en el celular"


def __init__(self, nombre, edad, nc, carrera):
Super().__init__(nombre, edad)
self.__numero_cuenta = nc
self.__carrera = carrera


@property
def numero_cuenta(self):
return self.__numero_cuenta

@numero_cuenta.setter
def numero_cuenta(self, nc):
    self.__numero_cuenta = nc


@property
def carrera(self):
return self.__carrera


@carrera.setter
def carrera(self, carrera):
    self.__carrera = carrera


@property
def horas(self):
    return self.__horas

@horas.setter
def horas(self, h):
    self.__horas = h

    @carrera.setter
    def carrera(self, carrera):
        self.__carrera = carrera

    def __str__(self):
    return super().__str__() + f", Numero de cuenta: {self.__numero_cuenta}


def dormir(self):
    print(super().nombre_, " estd durmiendo como alumno")


@classmethod
def constructor_defecto(cls _):
return cls("", 0, "", "")


class Profesor(Persona):
descripcion = "Una persona que dice que ensefia pero se la pasa leyendo articulos de investigacion"
def __init__(self, nombre, edad, num_tra, area):
    super().__init__(nombre, edad)
    self.__numero_trabajador = num_tra
    self.__area = area


@property
def numero_trabajador(self):
    return self._numero_trabajador


@numero_trabajador.setter
def numero_trabajador(self, num_tra):
    self.__numero_trabajador = num_tra


@area.setter
def area(self, area):
    self._area = area


def __str__(self):
    return super().__str_Qy + f", Numero de trabajador: {self.__num_tra}


def __str__(self): =


return super().__str__() + f", Numero de trabajador: {self.__numero_)

def dormir(self):
    print(super().nombre, " esta durmiendo como profesor")


class AyudanteProfesor(ALumno, Profesor):
    def __init__[setf, nombre, edad, nc, carr, num_tra, area, numero_horas_contratadas)
    Alumno.__init__(nombre, edad, nc, carr)
    Profesor.__init__(nombre, edad, num_tra, area)
    self.__horas = numero_horas


@property
def horas(self):
    return self.__horas


@horas.setter
def horps(self, h):
    self._horas = h


def __str__(self):
    return Alumno.__str__() + Profesor.__str__() + f"Horas de trabajo: {self.__horas}


def dar_clase(self, materia):
print(f"{self.nombre} esta dando {self.area} por {self.horas} horas")


def dormir(self):
    super().dormir()

