# importe de biblioteca
from flask import Flask, render_template, request

#criar objeto flask "apelido - app"

app = Flask(__name__)

#base fake
base_fake = []

# rotas

@app.route('/')
def inicial():
    return render_template('pagina_inicial.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)