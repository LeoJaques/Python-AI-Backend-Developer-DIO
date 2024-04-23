from typing import TypedDict, List
from datetime import date

class Usuario(TypedDict):
    id: int
    nome: str
    data_de_nascimento: date
    cpf: int
    endereco: {
        logradouro: str,
        bairro: str,
        cidade: str,
        estado: str,
    }
    
usuarios: List[Usuario] = []

def verificar_cpf_existente(cpf: int) -> bool:
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return True
    return False

def criar_usuario(usuario: Usuario):
    if not verificar_cpf_existente(novo_usuario['cpf']):
        usuarios.append(novo_usuario)
        print("Usuário adicionado com sucesso!")
    else:
        print("CPF já existe na lista de usuários.")

def listar_usuario():
    pass

print('kkeai man')