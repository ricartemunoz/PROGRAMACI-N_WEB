from flask import Flask, render_template,request
import math

app=Flask(__name__)

@app.route ('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/procesar_formulario',methods=['GET','POST'])
def procesar_formulario():
        if request.method == 'POST':
            nota1 = int(request.form['nota1'])
            nota2 = int(request.form['nota2'])
            nota3 = int(request.form['nota3'])
            asistencia = int(request.form['asistencia'])
            promedio = (nota1 + nota2 + nota3)/3
            print(promedio)
            if promedio >=40 and asistencia >=75:
                return render_template('ejercicio1.html', promedio = promedio, estado = 'APROBADO')
            else:
                    return render_template('ejercicio1.html', promedio =promedio, estado = 'REPROBADO')

        return f'debe ingresar las notas'

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/procesar_nombres', methods = ['GET','POST'])
def procesar_nombres():
    if request.method == 'POST':
        lnombre1 = len(request.form['nombre1'])
        lnombre2 = len(request.form['nombre2'])
        lnombre3 = len(request.form['nombre3'])
        if lnombre1 > lnombre2 and lnombre1 > lnombre3:
            return render_template('ejercicio2.html', nombre_largo=request.form['nombre1'], largo = lnombre1)
        elif lnombre2 > lnombre1 and lnombre2 > lnombre3:
            return render_template('ejercicio2.html', nombre_largo=request.form['nombre2'], largo = lnombre2)
        else:
            return render_template('ejercicio2.html', nombre_largo=request.form['nombre3'], largo = lnombre3)


if __name__ == '__main__':
        app.run(port=8000, debug=True)