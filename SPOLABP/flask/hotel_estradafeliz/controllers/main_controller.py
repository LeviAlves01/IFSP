from flask import Blueprint, redirect, url_for, session

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    perfil = session.get('perfil_id')

    if perfil == 1:
        return redirect(url_for('admin.dashboard'))
    elif perfil == 2:
        return redirect(url_for('recep.dashboard'))
    elif perfil == 3:
        return redirect(url_for('maid.dashboard'))
    elif perfil == 4:
        return redirect(url_for('guest.dashboard'))

    return redirect(url_for('auth.login'))
