from flask import Flask, render_template,request
import math

app=Flask(__name__)

@app.route ('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/procesar_compra',methods=['GET','POST'])
def procesar_compra():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        total = tarros*9000
        if edad >= 18 and edad <= 30:
            descto1 = int(total*0.15)
            pagar = int(total-descto1)
            return render_template('ejercicio1.html',nombre = nombre, total = total , descto = descto1, pagar = pagar)
        elif edad >= 30:
            descto1 = int(total * 0.25)
            pagar = int(total - descto1)
            return render_template('ejercicio1.html', nombre=nombre, total=total, descto=descto1, pagar=pagar)
        else:
            descto1 = int(0)
            pagar = int(total - descto1)
            return render_template('ejercicio1.html', nombre=nombre, total=total, descto=descto1, pagar=pagar)

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/inicio_sesion', methods = ['GET', 'POST'])
def inicio_sesion():
    usuario = request.form['usuario']
    clave = request.form['clave']
    if usuario == 'juan' and clave == 'admin':
        return render_template('ejercicio2.html', mensaje = "Bienvenido administrador ", usuario = usuario)
    elif usuario == "pepe" and clave == "user":
        return render_template('ejercicio2.html', mensaje = "Bienvenido usuario ", usuario = usuario)
    else:
        return render_template('ejercicio2.html', mensaje = "Usuario o Contraseña incorrectos")

if __name__ == '__main__':
        app.run(port=8000, debug=True)