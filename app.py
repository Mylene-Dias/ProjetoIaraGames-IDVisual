from flask import Flask, render_template, request, redirect, Flask
import os 

app = Flask(__name__)

STATICFILES_DIRS = [
    os.path.join("ASSETS", 'setup/static')
]

@app.route('/')
def cadastro():
    return render_template('cadastro.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    confirmar = request.form['confirmar']
    
    if senha != confirmar:
        Flask('As senhas não coincidem.')
        return redirect('/')
    
    return render_template('sucesso.html', nome=nome, email=email)


if __name__ == '__main__':
    app.run(debug=True)