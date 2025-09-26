from flask import Flask, request, render_template
import sqlite3
app = Flask(__name__)

def getdb_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def pagina_inicial():
    return render_template('pagina_inicial.html')


@app.route('/sobre/<username>')
def pagina_sobre(username):
    nome = username
    serviços = ["Desenvolvimento Web", "Consultoria em TI", "Analise de Dados"]

    return render_template('sobrenos.html', nome=nome, serviços=serviços)

@app.route('/cadastro', methods=['GET', 'POST'])
def pagina_cadastro():

    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']

            conn = getdb_connection()
            conn.execute('INSERT INTO users (username, email) VALUES (?, ?)', (username, email))
            conn.commit()
            conn.close()
        except sqlite3.IntegrityError:
            erro = "Email já cadastrado!"
            return render_template('cadastro.html', erro=erro)
        
        return f"Usuário {username} cadastrado com sucesso!"

    return render_template('cadastro.html')



@app.route('/usuarios')
def listar_usuarios():
    conn = getdb_connection()
    usuarios = conn.execute('SELECT * FROM users').fetchall()
    conn.commit()
    conn.close()

    return render_template('usuarios.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)
