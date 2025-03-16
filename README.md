# API de Nombres de Personas

Esta API sencilla, desarrollada con Flask, proporciona un endpoint para obtener una lista de nombres de personas en formato JSON.

## Requisitos

* Python 3.6 o superior
* Flask (instalable con `pip install Flask`)

## Cómo ejecutar la API

1.  **Guarda el código:** Guarda el código de la API en un archivo llamado, por ejemplo, `main.py`.
2.  **Ejecuta la aplicación:** Abre una terminal o ventana de comandos, navega hasta el directorio donde guardaste el archivo `main.py` y ejecuta el siguiente comando:

    ```bash
    python main.py
    ```

    Esto iniciará el servidor de desarrollo de Flask. Por defecto, la API estará disponible en `http://127.0.0.1:5000/`.

## Cómo consumir el endpoint

### Endpoint: `/personas`

  Método: GET
  Descripción: Devuelve una lista de nombres de personas en formato JSON.
* **Respuesta:**

    ```json
    {
    "personas": ["Juan", "Carlos", "Ana", "Pedro", "Luisa", "julian", "samuel"]
    }
    ```

### Ejemplos de consumo

#### Usando `curl` (terminal)

```bash
curl [http://127.0.0.1:5000/personas](https://www.google.com/search?q=http://127.0.0.1:5000/personas)
