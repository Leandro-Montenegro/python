class Error:
    def __init__(self, codigo, numero, mensajes, horas, segundos):
        self.codigo = codigo
        self.numero = numero
        self.mensajes = mensajes
        self.horas = horas
        self.segundos = segundos

    def __str__(self):
        r = "codigo: " + str(self.codigo) + ",numero: " + str(self.numero)
        r += ",mensajes: " + str(self.mensajes) + ", horas: " + str(self.horas)
        r += ", segundos: " + str(self.segundos)
        return r
