import hashlib
import uuid
import getpass

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generar_id():
    return str(uuid.uuid4())

def registrar_usuario(username, password, registrados):
    for usuario in registrados:
        if usuario and usuario['Usuario'] == username:
            return False
    user_id = generar_id()
    password_hash = hash_password(password)
    nuevo_usuario = {
        'ID': user_id,
        'Usuario': username,
        'Password': password_hash
    }
    registrados.append(nuevo_usuario)
    return True

def autenticacion_sesion(username, password, registrados):
    intentos_max = 3
    intentos = 0

    usuario_encontrado = None
    for usuario in registrados:
        if usuario and usuario['Usuario'] == username:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        return False

    while intentos < intentos_max:
        password_hash = hash_password(password)
        if password_hash == usuario_encontrado['Password']:
            return True
        else:
            intentos += 1
            if intentos < intentos_max:
                print(f"Contraseña incorrecta. Intentos restantes: {intentos_max - intentos}")
                password = getpass.getpass("")
            else:
                print("Demasiados intentos fallidos. Regresando al menú.")
                return False
    return False
