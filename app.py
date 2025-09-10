from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "9c99a877bd9adc33848bda91834205e1f9a7ef7a184d99923629f62c7771c0a9"  

def generar_clave_desde_cc(cc: str) -> str:
    return f"Inicio*{cc[-4:]}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cc = (request.form.get('cc') or '').strip()

        if not cc.isdigit() or not (8 <= len(cc) <= 10):
            flash('Por favor, ingresa una cédula válida (8 a 10 dígitos).')
            return redirect(url_for('index'))

        clave = generar_clave_desde_cc(cc)

        return render_template('listo.html', app_name='Usuario tecnoglass', clave=clave)

    return render_template('index.html', app_name='Usuario tecnoglass')
