from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from models.storage import users, guests, reservations, room_types, rooms, invoices, next_id

recep_bp = Blueprint('recep', 'recep', template_folder='../templates')

def require_recep():
    uid = session.get('user_id')
    u = next((x for x in users if x['id']==uid), None)
    return u and u['perfil_id']==2

@recep_bp.route('/')
def dashboard():
    if not require_recep():
        flash('Acesso negado: Recepcionista apenas')
        return redirect(url_for('auth.login'))
    return render_template('recep/dashboard.html', reservations=reservations, guests=guests)

@recep_bp.route('/reservations/create', methods=['GET','POST'])
def create_reservation():
    if not require_recep():
        flash('Acesso negado')
        return redirect(url_for('auth.login'))
    if request.method=='POST':
        # create guest if necessary
        if not request.form.get('id_hospede'):
            hid = next_id(guests,'id_hospede')
            guests.append({'id_hospede':hid,'nome_completo':request.form['nome_hospede'],'documento':request.form['doc'],'telefone':request.form.get('telefone',''),'email':request.form.get('email',''),'id_usuario_sistema':None})
        else:
            hid = int(request.form['id_hospede'])
        dt_in = request.form['data_checkin']
        dt_out = request.form['data_checkout']
        # calculate days
        from datetime import datetime
        d1 = datetime.strptime(dt_in,'%Y-%m-%d').date()
        d2 = datetime.strptime(dt_out,'%Y-%m-%d').date()
        dias = max((d2-d1).days,1)
        tipo = int(request.form['id_tipo'])
        tipo_obj = next((t for t in room_types if t['id_tipo']==tipo), room_types[0])
        valor = tipo_obj['preco_diaria_base'] * dias
        novo = {'id_reserva': next_id(reservations,'id_reserva'), 'id_hospede_principal': hid, 'numero_quarto': request.form.get('numero_quarto') or None, 'data_checkin': d1, 'data_checkout': d2, 'status_reserva':'Confirmada','valor_total':valor}
        reservations.append(novo)
        flash('Reserva criada')
        return redirect(url_for('recep.dashboard'))
    return render_template('recep/create_reservation.html', room_types=room_types, guests=guests)

@recep_bp.route('/reservations/edit/<int:res_id>', methods=['GET','POST'])
def edit_reservation(res_id):
    if not require_recep():
        flash('Acesso negado')
        return redirect(url_for('auth.login'))
    r = next((x for x in reservations if x['id_reserva']==res_id), None)
    if not r:
        flash('Reserva não encontrada')
        return redirect(url_for('recep.dashboard'))
    if request.method=='POST':
        r['numero_quarto'] = request.form.get('numero_quarto') or None
        r['status_reserva'] = request.form.get('status_reserva')
        flash('Atualizado')
        return redirect(url_for('recep.dashboard'))
    return render_template('recep/edit_reservation.html', r=r)

@recep_bp.route('/checkin/<int:res_id>')
def checkin(res_id):
    if not require_recep():
        flash('Acesso negado')
        return redirect(url_for('auth.login'))
    r = next((x for x in reservations if x['id_reserva']==res_id), None)
    if not r:
        flash('Reserva não encontrada')
        return redirect(url_for('recep.dashboard'))
    r['status_reserva']='Em Estadia'
    # create invoice
    inv = {'id_fatura': next_id(invoices,'id_fatura'), 'id_reserva': r['id_reserva'], 'data_emissao': __import__('datetime').datetime.now(), 'valor_servicos':0.0, 'valor_diarias': r['valor_total'], 'status_pagamento':'Pendente'}
    invoices.append(inv)
    flash('Check-in realizado')
    return redirect(url_for('recep.dashboard'))

@recep_bp.route('/checkout/<int:res_id>')
def checkout(res_id):
    if not require_recep():
        flash('Acesso negado')
        return redirect(url_for('auth.login'))
    r = next((x for x in reservations if x['id_reserva']==res_id), None)
    if not r:
        flash('Reserva não encontrada')
        return redirect(url_for('recep.dashboard'))
    r['status_reserva']='Concluída'
    inv = next((i for i in invoices if i['id_reserva']==r['id_reserva']), None)
    if inv:
        inv['status_pagamento']='Pendente'
    flash('Check-out realizado')
    return redirect(url_for('recep.dashboard'))

