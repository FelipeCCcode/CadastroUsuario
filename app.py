from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def getdb_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def pagina_inicial():
    nome_do_usuario = "Felipe"
    compras = ["Maçã", "Banana", "Leite"]
    return render_template('pagina_inicial.html', 
                           nome_usuario=nome_do_usuario, 
                           lista_compras=compras)

@app.route('/sobre/<username>')
def pagina_sobre(username):
    nome = username
    servicos = ["Desenvolvimento Web", "Consultoria em TI", "Analise de Dados"]

    return render_template('sobrenos.html', nome_usuario=nome, lista_servicos=servicos)

@app.route('/cadastro', methods=['GET', 'POST'])
def pagina_cadastro():
    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']

            conn = getdb_connection()
            # CORREÇÃO 3: O nome da tabela é 'user' (singular), como em schema.sql
            conn.execute('INSERT INTO user (username, email) VALUES (?, ?)', (username, email))
            conn.commit()
            conn.close()
        except sqlite3.IntegrityError:
            erro = "Email ou nome de usuário já cadastrado!"
            return render_template('cadastro.html', erro=erro)
        
        # CORREÇÃO 4: Implementamos o padrão Post/Redirect/Get
        # Após o sucesso, redirecionamos para a lista de usuários.
        return redirect(url_for('listar_usuarios'))

    return render_template('cadastro.html')

@app.route('/usuarios')
def listar_usuarios():
    conn = getdb_connection()
    # CORREÇÃO 5: O nome da tabela é 'user' (singular).
    # O commit() foi removido pois não é necessário para um SELECT.
    usuarios = conn.execute('SELECT * FROM user').fetchall()
    conn.close()

    return render_template('usuarios.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)

