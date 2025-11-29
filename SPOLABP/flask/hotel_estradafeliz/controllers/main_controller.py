from flask import Blueprint, render_template, session, redirect, url_for

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Agora a homepage SEMPRE aparece
    return render_template('index.html')

@main_bp.route('/painel')
def painel():
    # Aqui sim verificamos se está logado
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    perfil = session.get('perfil_id')

    if perfil == 1:
        return redirect(url_for('admin.dashboard'))
    elif perfil == 2:
        return redirect(url_for('recep.dashboard'))
    elif perfil == 3:
        return redirect(url_for('maid.list_rooms'))
    elif perfil == 4:
        return redirect(url_for('guest.panel'))

    return redirect(url_for('auth.login'))
