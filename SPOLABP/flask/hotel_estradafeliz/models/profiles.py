from models.storage import profiles

def get_profile_name(perfil_id):
    p = next((x for x in profiles if x['id']==perfil_id), None)
    return p['nome_perfil'] if p else 'Desconhecido'

