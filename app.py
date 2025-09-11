from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "key"  

def generar_contraseña(cc: str) -> str:
    return f"Inicio*{cc[-4:]}"

registros=[]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cc = (request.form.get('cc') or '').strip()
        sistema=request.form.get('sistema')

        if not cc.isdigit() or not (8 <= len(cc) <= 10):
            flash('Por favor, ingresa una cédula válida (8 a 10 dígitos).')
            return redirect(url_for('index'))

        clave = generar_contraseña(cc)
        registros.append({'cc':cc,'sistema':sistema})

        return render_template('listo.html', app_name='Usuarios tecnoglass', clave=clave)

    return render_template('index.html', app_name='Usuarios tecnoglass')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        if 'delete' in request.form:
            idx = int(request.form.get('delete'))
            registros.pop(idx)
    return render_template('admin.html', registros=registros, app_name='Panel interno')

if __name__ == "__main__":
    app.run(host="10.1.131.31", port=5000, debug=True)

