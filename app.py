from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "key"  

def generar_contraseña(cc: str) -> str:
    return f"Inicio*{cc[-4:]}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cc = (request.form.get('cc') or '').strip()

        if not cc.isdigit() or not (8 <= len(cc) <= 10):
            flash('Por favor, ingresa una cédula válida (8 a 10 dígitos).')
            return redirect(url_for('index'))

        clave = generar_contraseña(cc)

        return render_template('listo.html', app_name='Usuarios tecnoglass', clave=clave)

    return render_template('index.html', app_name='Usuarios tecnoglass')

if __name__ == "__main__":
    app.run(host="10.1.131.31", port=5000, debug=True)
