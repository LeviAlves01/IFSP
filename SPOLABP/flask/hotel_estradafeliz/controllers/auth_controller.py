from flask import Blueprint, render_template, request, redirect, url_for, session, flash, make_response
from models.storage import find_user_by_email, users
from models.profiles import get_profile_name

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        user = find_user_by_email(email)
        if user and user.get('senha') == senha:  # simple hash-free for teaching; replace with hashed in real
            session['user_id'] = user['id']
            resp = make_response(redirect(url_for('auth.after_login')))
            # cookie: theme preference default
            resp.set_cookie('theme', request.cookies.get('theme', 'dark'))
            flash('Login efetuado')
            return resp
        flash('Credenciais inválidas')
    return render_template('auth/login.html')

@auth_bp.route('/after_login')
def after_login():
    uid = session.get('user_id')
    if not uid:
        return redirect(url_for('auth.login'))
    user = next((u for u in users if u['id']==uid), None)
    perfil = get_profile_name(user['perfil_id'])
    if perfil == 'Administrador':
        return redirect(url_for('admin.dashboard'))
    if perfil == 'Recepcionista':
        return redirect(url_for('recep.dashboard'))
    if perfil == 'Camareira':
        return redirect(url_for('maid.list_rooms'))
    return redirect(url_for('guest.panel'))

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Desconectado')
    return redirect(url_for('auth.login'))

