from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from models.storage import users, profiles, room_types, rooms, invoices
from models.storage import next_id
from models.profiles import get_profile_name

admin_bp = Blueprint('admin', __name__, template_folder='../templates')

def require_admin():
    uid = session.get('user_id')
    u = next((x for x in users if x['id']==uid), None)
    return u and u['perfil_id']==1

@admin_bp.route('/')
def dashboard():
    if not require_admin():
        flash('Acesso negado: somente Administrador')
        return redirect(url_for('auth.login'))
    total_reservas = sum(1 for r in [])  # placeholder
    receita = sum((inv['valor_diarias'] + inv['valor_servicos']) for inv in invoices) if invoices else 0
    return render_template('admin/dashboard.html', total_reservas=total_reservas, total_quartos=len(rooms), receita=receita)

# Users CRUD
@admin_bp.route('/users')
def manage_users():
    if not require_admin():
        flash('Acesso negado')
        return redirect(url_for('auth.login'))
    return render_template('admin/users.html', users=users, profiles=profiles)

@admin_bp.route('/users/create', methods=['GET','POST'])
def create_user():
    if not require_admin():
        flash('Acesso negado')
        return redirect(url_for('auth.login'))
    if request.method=='POST':
        novo = {'id': next_id(users, 'id'), 'nome_completo': request.form['nome'], 'email': request.form['email'], 'senha': request.form['senha'], 'perfil_id': int(request.form['perfil'])}
        users.append(novo)
        flash('Usuário criado')
        return redirect(url_for('admin.manage_users'))
    return render_template('admin/create_user.html', profiles=profiles)

@admin_bp.route('/room_types')
def list_room_types():
    if not require_admin():
        flash('Acesso negado')
        return redirect(url_for('auth.login'))
    return render_template('admin/room_types.html', types=room_types)

@admin_bp.route('/room_types/create', methods=['GET','POST'])
def create_room_type():
    if not require_admin():
        flash('Acesso negado')
        return redirect(url_for('auth.login'))
    if request.method=='POST':
        novo = {'id_tipo': next_id(room_types,'id_tipo'),'nome_tipo':request.form['nome_tipo'],'capacidade_maxima':int(request.form['capacidade']),'preco_diaria_base':float(request.form['preco']),'descricao':request.form.get('descricao','')}
        room_types.append(novo)
        flash('Tipo criado')
        return redirect(url_for('admin.list_room_types'))
    return render_template('admin/create_room_type.html')

