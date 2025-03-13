from flask import Flask, jsonify  # Importamos Flask para crear la aplicación y jsonify para devolver respuestas en formato JSON.

app = Flask(__name__)  # Creamos una instancia de la aplicación Flask.

# Lista de nombres de personas
personas = ["Juan", "Carlos", "Ana", "Pedro", "Luisa","julian","samuel"]  # Definimos una lista con algunos nombres.

@app.route('/personas', methods=['GET'])  # Definimos una ruta "/personas" que acepta solicitudes GET.
def obtener_personas():
    """
    Endpoint que devuelve una lista de nombres de personas en formato JSON.
    """
    return jsonify({"personas": personas})  # Retornamos la lista de nombres en formato JSON.

if __name__ == '__main__':  # Verificamos si el script se ejecuta directamente.
    app.run(debug=True)  # Iniciamos el servidor en modo depuración (debug), lo que permite ver errores en la consola.
