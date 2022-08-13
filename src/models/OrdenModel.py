from database.db import get_connection
from .entities.Orden import Orden


class OrdenModel():

    # Metodo para listar ordenes
    @classmethod
    def get_ordenes(self):
        try:
            connection = get_connection()
            ordenes = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT nro_orden, estado, id_cliente, fecha_orden, largo_vidrio, ancho_vidrio FROM ordenes")
                resulset = cursor.fetchall()

                for row in resulset:
                    orden = Orden(row[0], row[1], row[2], row[3],row[4],row[5],)
                    ordenes.append(orden.to_JSON())

            connection.close()
            return ordenes

        except Exception as ex:
            raise Exception(ex)

    # Metodo para crear una orden
    @classmethod
    def add_orden(self, orden):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO ordenes (nro_orden, estado, id_cliente, fecha_orden, largo_vidrio, ancho_vidrio)
                                VALUES (%s, %s, %s, %s, %s, %s)""", (orden.nro_orden, orden.estado, orden.id_cliente, orden.fecha_orden, orden.largo_vidrio, orden.ancho_vidrio))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    
    # Metodo para cambiar el estado de una orden
    @classmethod
    def update_orden(self, orden):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE ordenes SET estado=%s
                                WHERE nro_orden = %s """, (orden.estado, orden.nro_orden))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)


     # Metodo para eliminar una orden
    @classmethod
    def delete_orden(self, orden):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM ordenes WHERE nro_orden= %s", (orden.nro_orden,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def validar_cliente(self,orden):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM clientes WHERE id_cliente= %s", (orden.id_cliente,))              
                affected_rows = cursor.rowcount
                if (affected_rows == 1):
                    affected_rows = 1
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
