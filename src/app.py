import resource
from flask import Flask
from config import config
from flask_cors import CORS
# Rutas
from routes import Cliente
from routes import Orden


app = Flask(__name__)

#LINEA PARA DESPLIGUE 
#CORS(app,resources={"*":{"origins":"http://127.0.0.1:5000"}})

def page_not_found(error):
    return "<h1>PAGINA NO ENCONTRADA</h1>",404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    #BluePrints
    app.register_blueprint(Cliente.main,url_prefix='/api/clientes')
    app.register_blueprint(Orden.main,url_prefix='/api/ordenes')


    # ErrorControles
    app.register_error_handler(404, page_not_found)
    app.run()
