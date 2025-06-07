# app.py
from flask import Flask, render_template, request, redirect, url_for, session, g
from models import User, Trail, Module
from config import SECRET_KEY
from database import init_db, connect_db
import sqlite3 # Importar connect_db para fechar a conexão

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

# Antes de cada requisição, tenta carregar o usuário logado
@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.get_by_id(user_id)

# Rota de Home - Lista todas as trilhas
@app.route('/')
def index():
    trails = Trail.get_all()
    return render_template('index.html', trails=trails)

# Rota para detalhes da trilha
@app.route('/trilha/<int:trail_id>')
def trilha_detalhe(trail_id):
    trail = Trail.get_by_id(trail_id)
    if not trail:
        return "Trilha não encontrada", 404
    modules = trail.get_modules()
    return render_template('trilha_detalhe.html', trail=trail, modules=modules)

# Rota para criar nova trilha (apenas voluntários)
@app.route('/nova_trilha', methods=['GET', 'POST'])
def nova_trilha():
    if not g.user or g.user.role != 'volunteer':
        return redirect(url_for('login')) # Redireciona para login se não for voluntário

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        difficulty = request.form['difficulty']
        creator_id = g.user.id # O criador é o usuário logado

        new_trail = Trail(title=title, description=description, difficulty=difficulty, creator_id=creator_id)
        new_trail.save()
        return redirect(url_for('index'))
    return render_template('nova_trilha.html')

# Rota para adicionar módulo a uma trilha (apenas voluntários)
@app.route('/trilha/<int:trail_id>/novo_modulo', methods=['GET', 'POST'])
def novo_modulo(trail_id):
    if not g.user or g.user.role != 'volunteer':
        return redirect(url_for('login'))

    trail = Trail.get_by_id(trail_id)
    if not trail:
        return "Trilha não encontrada", 404

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_module = Module(trail_id=trail.id, title=title, content=content)
        new_module.save()
        return redirect(url_for('trilha_detalhe', trail_id=trail.id))
    return render_template('novo_modulo.html', trail=trail)

# Rota de Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'] # Em produção, use hashing de senha!

        user = User.get_by_username(username)
        if user and user.password == password: # Validação de senha simples
            session['user_id'] = user.id
            return redirect(url_for('index'))
        else:
            error = "Usuário ou senha inválidos."
            return render_template('login.html', error=error)
    return render_template('login.html')

# Rota de Registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'] # Em produção, use hashing de senha!
        role = request.form['role']

        existing_user = User.get_by_username(username)
        if existing_user:
            error = "Nome de usuário já existe."
            return render_template('register.html', error=error)

        new_user = User(username=username, password=password, role=role)
        new_user.save()
        session['user_id'] = new_user.id # Loga o usuário automaticamente após registro
        return redirect(url_for('index'))
    return render_template('register.html')


# Rota de Logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

# Garante que a conexão com o DB seja fechada após cada requisição
@app.teardown_appcontext
def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    # Inicializa o banco de dados se não existir
    try:
        connect_db().close()
    except sqlite3.OperationalError:
        init_db()
    app.run(debug=True) # debug=True para desenvolvimento. Mude para False em produção.