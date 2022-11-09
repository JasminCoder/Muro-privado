from flask import render_template, redirect, session, request, flash
from flask_app import app

#importamos la clase message
from flask_app.models.messages import Message

#ruta enviar msj
@app.route('/send_message', methods=["POST"])
def send_message():
    #Verificamos que el usuario haya iniciado sesión
    if 'user_id' not in session:
        return redirect('/')

    #Guardamos el mensaje
    Message.save(request.form)
    return redirect('/dashboard')




#ruta eliminar msj
@app.route('/eliminar/mensaje/<int:id>') #en mi URL voy a obtener el ID del mensaje a borrar
def eliminar_mensaje(id):
    #función para eliminar mensaje
    formulario = {"id": id}
    Message.eliminate(formulario)
    return redirect('/dashboard')


