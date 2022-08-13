class Cliente():
    def __init__(self, id_cliente, nombre=None, direccion=None, telefono=None, nacionalidad=None, correo=None) -> None:
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.nacionalidad = nacionalidad
        self.correo = correo

    def to_JSON(self):
        return {
            'id_cliente': self.id_cliente,
            'nombre': self.nombre,
            'direccion': self.direccion,
            'telefono': self.telefono,
            'nacionalidad': self.nacionalidad,
            'correo': self.correo,
        }
