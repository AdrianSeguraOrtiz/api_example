from flask import Flask, render_template, redirect, request
from flask_pymongo import pymongo

client = pymongo.MongoClient("mongodb+srv://adriansegura:adrianseguraortiz1999@psicotreatbd.e4kvw.mongodb.net/api_example?retryWrites=true&w=majority")
mongo_db = client.get_database('api_example')
mongo_col = pymongo.collection.Collection(mongo_db, 'api_example')

app = Flask(__name__)

@app.route('/')
def pagina_principal():
    return render_template("home.html")

@app.route('/usuarios')
def usuarios():
    usuarios = mongo_col.find()
    return render_template("usuarios.html.j2", users = usuarios, mostrar_enlace = True)

@app.route('/formulario', methods = ['GET', 'POST'])
def formulario():
    if request.method == 'GET':
        return render_template("formulario.html.j2")
    elif request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        clave = request.form['clave']
        usuario = {"nombre" : nombre, "apellidos": apellidos, "clave" : clave}
        mongo_col.insert_one(usuario)
        return redirect("/usuarios")


if __name__ == '__main__':
    app.run(debug=True)