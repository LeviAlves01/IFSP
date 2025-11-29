from flask import Blueprint, render_template, session, flash, redirect, url_for
from models.storage import users, guests, reservations, invoices

guest_bp = Blueprint('guest', 'guest', template_folder='../templates')

def require_guest():
    uid = session.get('user_id')
    u = next((x for x in users if x['id']==uid), None)
    return u and u['perfil_id']==4

@guest_bp.route('/')
def panel():
    if not require_guest():
        flash('Acesso negado: Hóspede apenas')
        return redirect(url_for('auth.login'))
    uid = session.get('user_id')
    guest = next((g for g in guests if g.get('id_usuario_sistema')==uid), None)
    guest_reservas = [r for r in reservations if r['id_hospede_principal']==(guest['id_hospede'] if guest else None)]
    guest_invoices = [inv for inv in invoices if any(r['id_reserva']==inv['id_reserva'] and r['id_hospede_principal']==(guest['id_hospede'] if guest else None) for r in reservations)]
    return render_template('guest/panel.html', reservas=guest_reservas, faturas=guest_invoices)

