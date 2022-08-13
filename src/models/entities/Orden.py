from utils.DateFormat import DateFormat


class Orden():
    def __init__(self, nro_orden, estado, id_cliente=None, fecha_orden=None, largo_vidrio=None, ancho_vidrio=None) -> None:
        self.nro_orden = nro_orden
        self.estado = estado
        self.id_cliente = id_cliente
        self.fecha_orden = fecha_orden
        self.largo_vidrio = largo_vidrio
        self.ancho_vidrio = ancho_vidrio

    def to_JSON(self):
        return {
            'nro_orden': self.nro_orden,
            'estado': self.estado,
            'id_cliente': self.id_cliente,
            'fecha_orden': DateFormat.convert_date(self.fecha_orden),
            'largo_vidrio': self.largo_vidrio,
            'ancho_vidrio': self.ancho_vidrio

        }
