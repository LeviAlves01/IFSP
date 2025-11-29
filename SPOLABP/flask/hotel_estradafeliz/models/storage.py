import decimal
from datetime import date

# profiles
profiles = [
    {'id':1,'nome_perfil':'Administrador'},
    {'id':2,'nome_perfil':'Recepcionista'},
    {'id':3,'nome_perfil':'Camareira'},
    {'id':4,'nome_perfil':'Hóspede'}
]

# users (senha em texto plano para facilitar testes; trocar por hash em produção)
users = [
    {'id':1,'nome_completo':'Admin Geral','email':'admin@hotel','senha':'admin123','perfil_id':1},
    {'id':2,'nome_completo':'Recepção 1','email':'recep@hotel','senha':'recep123','perfil_id':2},
    {'id':3,'nome_completo':'Camareira 1','email':'cam@hotel','senha':'cam123','perfil_id':3},
    {'id':4,'nome_completo':'Hóspede Exemplo','email':'hosp@hotel','senha':'hosp123','perfil_id':4},
]

# room types
room_types = [
    {'id_tipo':1,'nome_tipo':'Simples','capacidade_maxima':2,'preco_diaria_base':120.0,'descricao':'Quarto simples'},
    {'id_tipo':2,'nome_tipo':'Luxo','capacidade_maxima':3,'preco_diaria_base':220.0,'descricao':'Quarto luxo'},
    {'id_tipo':3,'nome_tipo':'Suíte Presidencial','capacidade_maxima':5,'preco_diaria_base':800.0,'descricao':'Suíte grande'},
]

# rooms
rooms = [
    {'numero_quarto':'101','id_tipo':1,'status_limpeza':'Limpo','localizacao':'Ala Leste'},
    {'numero_quarto':'102','id_tipo':1,'status_limpeza':'Sujo','localizacao':'Ala Leste'},
    {'numero_quarto':'201','id_tipo':2,'status_limpeza':'Limpo','localizacao':'Ala Oeste'},
    {'numero_quarto':'301A','id_tipo':3,'status_limpeza':'Limpando','localizacao':'Cobertura'},
]

# guests
guests = [
    {'id_hospede':1,'nome_completo':'Hóspede Exemplo','documento':'000.000.000-00','telefone':'1199999-9999','email':'hosp@hotel','id_usuario_sistema':4}
]

# reservations
reservations = [
    {'id_reserva':1,'id_hospede_principal':1,'numero_quarto':'101','data_checkin':date.today(),'data_checkout':date.today(),'status_reserva':'Confirmada','valor_total':120.0}
]

# services
services = [
    {'id_servico':1,'nome_servico':'Minibar','preco':25.0},
    {'id_servico':2,'nome_servico':'Lavanderia','preco':40.0},
    {'id_servico':3,'nome_servico':'Café Extra','preco':12.0},
]

# invoices
invoices = []

# invoice items
invoice_items = []

# helpers
def next_id(collection, key):
    if not collection:
        return 1
    return max(item[key] for item in collection) + 1

def find_user_by_email(email):
    return next((u for u in users if u['email']==email), None)

