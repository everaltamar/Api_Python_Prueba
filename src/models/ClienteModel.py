import psycopg2
from database.db import get_connection
from .entities.Cliente import Cliente


class ClienteModel():

    # Metodo para obtener lista de clientes
    @classmethod
    def get_clientes(self):
        try:
            connection = get_connection()
            clientes = []        
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_cliente, nombre, direccion, telefono, nacionalidad, correo FROM clientes ORDER BY nombre ASC")
                resultset = cursor.fetchall()
                for row in resultset:
                    cliente = Cliente(
                        row[0], row[1], row[2], row[3], row[4], row[5])
                    clientes.append(cliente.to_JSON())
            connection.close()
            return clientes
        except Exception as ex:
            raise Exception(ex)

    # Metodo para buscar un cliente
    @classmethod
    def get_cliente(self, id_cliente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_cliente, nombre, direccion, telefono, nacionalidad, correo FROM clientes where id_cliente = %s", (id_cliente,))
                row = cursor.fetchone()
                cliente = None
                if row != None:
                    cliente = Cliente(
                        row[0], row[1], row[2], row[3], row[4], row[5])
                    cliente = cliente.to_JSON()
            connection.close()
            return cliente
        except Exception as ex:
            raise Exception(ex)

    # Metodo para registrar un cliente
    @classmethod
    def add_cliente(self, cliente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO clientes (id_cliente, nombre, direccion, telefono, nacionalidad, correo)
                                VALUES (%s, %s, %s, %s, %s, %s)""", (cliente.id_cliente, cliente.nombre, cliente.direccion, cliente.telefono, cliente.nacionalidad, cliente.correo))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    # metodo para actualizar un cliente
    @classmethod
    def update_cliente(self, cliente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE clientes SET nombre = %s, direccion = %s, telefono = %s, nacionalidad = %s,correo = %s
                                WHERE id_cliente = %s""", (cliente.nombre, cliente.direccion, cliente.telefono, cliente.nacionalidad, cliente.correo, cliente.id_cliente))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    # Metodo para eliminar un cliente
    @classmethod
    def delete_cliente(self, cliente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM clientes WHERE id_cliente= %s", (cliente.id_cliente,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
