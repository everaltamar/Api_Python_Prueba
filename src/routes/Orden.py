from flask import Blueprint, jsonify, request
import uuid

# entities
from models.entities.Orden import Orden

# modelos
from models.OrdenModel import OrdenModel

main = Blueprint('orden_blueprint', __name__)

# Ruta para listar ordenes
@main.route('/')
def get_ordenes():
    try:
        ordenes = OrdenModel.get_ordenes()
        return jsonify(ordenes)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# Ruta para crear una orden
@main.route('/add', methods=['POST'])
def add_orden():
    try:
        nro_orden = uuid.uuid4()
        id_cliente = request.json['id_cliente']
        fecha_orden = request.json['fecha_orden']
        largo_vidrio = request.json['largo_vidrio']
        ancho_vidrio = request.json['ancho_vidrio']
        estado = 'SOLICITADA'
        #validacion del cliente en tabla clientes        
        orden = Orden(str(nro_orden), estado, id_cliente,
                      fecha_orden, largo_vidrio, ancho_vidrio)

        validacion = OrdenModel.validar_cliente(orden)

        if validacion == 1:
            affected_rows = OrdenModel.add_orden(orden)
        else:
            affected_rows = 0
        
        if affected_rows == 1:
            return jsonify({'message': "Orden Creada Con Exito!"})
        else:
            return jsonify({'message': "Error al crear la orden"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


# Ruta para cambiar el estado de una orden
@main.route('/update/<nro_orden>', methods=['PUT'])
def update_orden(nro_orden):
    try:
        estado = request.json['estado']
        orden = Orden(str(nro_orden), estado)
        affected_rows = OrdenModel.update_orden(orden)

        if affected_rows == 1:
            return jsonify({'message': "Cambio de estado de la orden exitoso!"})
        else:
            return jsonify({'message': "Error al Cambiar el estado de la orden"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


# Ruta para eliminar una orden
@main.route('/delete/<nro_orden>', methods=['DELETE'])
def delete_orden(nro_orden):
    try:
        estado=""
        orden = Orden(nro_orden,estado)
        affected_rows = OrdenModel.delete_orden(orden)
        if affected_rows == 1:
            return jsonify({'message': "Orden Eliminada!"})
        else:
            return jsonify({'message': "Error al eliminar la orden"}), 404
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


