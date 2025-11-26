from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

HTML_HOME = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Tabla de Multiplicación</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: #101820;
            color: #f6f6f6;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background: rgba(255,255,255,0.06);
            padding: 30px;
            border-radius: 14px;
            width: 380px;
            backdrop-filter: blur(8px);
            box-shadow: 0px 0px 12px rgba(255,255,255,0.1);
        }
        h1 {
            text-align: center;
            margin-bottom: 15px;
        }
        input {
            width: 100%;
            padding: 10px;
            border-radius: 8px;
            border: none;
            outline: none;
            margin-bottom: 20px;
            font-size: 16px;
        }
        .result {
            margin-top: 20px;
            line-height: 1.6;
            font-size: 17px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Jonathan Chisaguano</h1>

    <form method="GET">
        <input type="number" name="n" placeholder="Ingresa un número" required>
    </form>

    {% if tabla %}
    <div class="result">
        {% for linea in tabla %}
            <div>{{ linea }}</div>
        {% endfor %}
    </div>
    {% endif %}
</div>

</body>
</html>
"""

@app.get("/")
def home():
    numero = request.args.get("n", type=int)
    tabla = None

    if numero is not None:
        tabla = [f"{numero} x {i} = {numero * i}" for i in range(1, 13)]

    return render_template_string(HTML_HOME, tabla=tabla)


@app.get("/api/multiplicar")
def api_multiplicar():
    n = request.args.get("n", type=int)
    if n is None:
        return jsonify({"error": "Debes enviar ?n=numero"}), 400

    tabla = {str(i): n * i for i in range(1, 13)}
    return jsonify({"numero": n, "tabla": tabla})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
