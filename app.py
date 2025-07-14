from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = int(request.form['asistencia'])
        promedio = (nota1 + nota2 + nota3) / 3
        estado = "APROBADO" if promedio >= 4 and asistencia >= 75 else "REPROBADO"

        resultado = f'Su promedio es: {promedio:.1f} y está {estado}'
    return render_template('ejercicio1.html', resultado=resultado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        nombres = [nombre1, nombre2, nombre3]
        mayor = max(nombres, key=len)
        letras = len(mayor)
        resultado = f'El nombre mas largo es {mayor} y tiene {letras} letras'
    return render_template('ejercicio2.html', resultado=resultado)


if __name__ == '__main__':
    app.run()
