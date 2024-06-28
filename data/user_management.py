import json

# Arquivo JSON para armazenar usuários
USERS_FILE = 'data/users.json'

# Carregar usuários do arquivo JSON
def load_users():
    try:
        with open(USERS_FILE, 'r') as file:
            users = json.load(file)
            #print(f"Usuários carregados: {users}")
            return users
    except FileNotFoundError:
        #print("Arquivo de usuários não encontrado.")
        return {}
    except json.JSONDecodeError:
        #print("Erro ao decodificar o arquivo JSON.")
        return {}

# Salvar usuários no arquivo JSON
def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=4)

# Registrar um novo usuário
def register_user(user_id, nome, cargo, privilege_level='admin', commands=["start", "ajuda", "placa", "message", "callback", "register"]):
    users = load_users()
    users[user_id] = {
        'Nome': nome,
        'cargo': cargo,
        'privilege_level': 'admin',
        'commands': ["start", "ajuda", "placa", "message", "callback", "register"] #commands
    }
    save_users(users)
    #print(f"Usuário registrado: {users[user_id]}")

# Verificar se o usuário tem permissão para usar um comando
def has_permission(user_id, command):
    user_id_str = str(user_id)
    users = load_users()
    #print(f"Verificando permissão para o usuário {user_id_str} no comando {command}.")
    user = users.get(user_id_str)
    if user:
        has_perm = command in user['commands']
        #print(f"Permissão encontrada: {has_perm}")
        return has_perm
    print("Usuário não encontrado.")
    return False

# Exemplo de função para verificar privilégio de administrador
def is_admin(user_id):
    user_id_str = str(user_id)
    users = load_users()
    user = users.get(user_id_str)
    if user:
        is_admin = user['privilege_level'] == 'admin'
        #print(f"Verificando se o usuário {user_id_str} é admin: {is_admin}")
        return is_admin
    #print(f"Usuário {user_id_str} não encontrado.")
    return False
