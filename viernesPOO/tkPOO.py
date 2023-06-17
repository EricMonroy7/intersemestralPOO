importar tkinter como tk

# herencia
clase MiAplicacion(tk.Tk):


def __init__(auto):
    tk.Tk.__init__(uno mismo )
    uno mismo title('Aplicación Python POO, PAPIME PE100423')
    uno mismo geometría('300x200')
    uno mismo configurar(bg='verde claro')
    # Composición
    uno mismo widget = Botón(auto)
    uno mismo artilugio _ paquete()


# otra herencia
clase Boton(tk.Frame):

def __init__(uno mismo, padre):
tk.marco ___init__(auto, padre, bg='azul')
# evento
uno mismo botón = tk.Botón(self, texto="¡¡Presioname!!", comando=self.saludar_ya, bg='celeste')
uno mismo botón _ paquete(pady=20)


def saludar_ya(uno mismo):
imprimir("¡Hola, mundo!")

app = MiAplicación()
aplicación bucle principal()