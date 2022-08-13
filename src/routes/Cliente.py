from flask import Blueprint, jsonify, request

# entities
from models.entities.Cliente import Cliente

# modelos
from models.ClienteModel import ClienteModel

main = Blueprint('cliente_blueprint', __name__)

# Ruta Para Listar Clientes
@main.route('/')
def get_clientes():
    try:
        clientes = ClienteModel.get_clientes()
        return jsonify(clientes)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


# Ruta para buscar un cliente
@main.route('/<id_cliente>')
def get_cliente(id_cliente):
    try:
        cliente = ClienteModel.get_cliente(id_cliente)
        if cliente != None:
            return jsonify(cliente)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# Ruta para registrar un cliente
@main.route('/add', methods=['POST'])
def add_cliente():
    try:
        id_cliente = request.json['id_cliente']
        nombre = request.json['nombre']
        direccion = request.json['direccion']
        telefono = request.json['telefono']
        nacionalidad = request.json['nacionalidad']
        correo = request.json['correo']

        cliente = Cliente(id_cliente, nombre, direccion,
                          telefono, nacionalidad, correo)

        affected_rows = ClienteModel.add_cliente(cliente)

        if affected_rows == 1:
            return jsonify({'message': "Cliente Registrado Con Exito!"})
        else:
            return jsonify({'message': "Error al Registrar el cliente "}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# Ruta para actualizar un cliente
@main.route('/update/<id_cliente>', methods=['PUT'])
def update_cliente(id_cliente):
    try:
        nombre = request.json['nombre']
        direccion = request.json['direccion']
        telefono = request.json['telefono']
        nacionalidad = request.json['nacionalidad']
        correo = request.json['correo']

        cliente = Cliente(id_cliente, nombre, direccion,
                          telefono, nacionalidad, correo)
        affected_rows = ClienteModel.update_cliente(cliente)

        if affected_rows == 1:
            return jsonify({'message': "Cliente Actualizado Con Exito!"})
        else:
            return jsonify({'message': "Error al actualizar El Cliente"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# Ruta para eliminar un cliente
@main.route('/delete/<id_cliente>', methods=['DELETE'])
def delete_cliente(id_cliente):
    try:
        cliente = Cliente(id_cliente)
        affected_rows = ClienteModel.delete_cliente(cliente)
        if affected_rows == 1:
            return jsonify({'message': "Cliente Eliminado!"})
        else:
            return jsonify({'message': "Error al Eliminar El Cliente"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
