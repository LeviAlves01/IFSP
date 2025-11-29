from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.storage import users, rooms

maid_bp = Blueprint('maid', 'maid', template_folder='../templates')

def require_maid():
    uid = session.get('user_id')
    u = next((x for x in users if x['id']==uid), None)
    return u and u['perfil_id']==3

@maid_bp.route('/')
def list_rooms():
    if not require_maid():
        flash('Acesso negado: Camareira apenas')
        return redirect(url_for('auth.login'))
    return render_template('maid/list.html', rooms=rooms)

@maid_bp.route('/update/<numero>', methods=['GET','POST'])
def update_clean_status(numero):
    if not require_maid():
        flash('Acesso negado')
        return redirect(url_for('auth.login'))
    room = next((r for r in rooms if r['numero_quarto']==numero), None)
    if not room:
        flash('Quarto não encontrado')
        return redirect(url_for('maid.list_rooms'))
    if request.method=='POST':
        room['status_limpeza']=request.form['status']
        flash('Status atualizado')
        return redirect(url_for('maid.list_rooms'))
    return render_template('maid/update.html', room=room)

