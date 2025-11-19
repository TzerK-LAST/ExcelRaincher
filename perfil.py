from colorama import init, Fore, Style
init(autoreset=True)
import getpass
from auth import hash_password
from utilities import restart

def modificar_perfil(registrados, username_act):
    for usuario in registrados:
        if usuario['Usuario'] == username_act:
            perfil = usuario
            break
    else:
        print("Usuario no encontrado.")
        return
    
    while True:
        print(f"""
{Fore.GREEN}╔══════════════════════════════════════════════════╗
║                                                  ║
║        {Fore.CYAN}🌿  PANEL DE MODIFICACIÓN DE PERFIL  🌿{Fore.GREEN}   ║
║                                                  ║
║      {Fore.WHITE}1 ▸ Cambiar nombre de usuario{Fore.GREEN}               ║             
{Fore.GREEN}║                                   {Fore.GREEN}               ║
║      {Fore.WHITE}2 ▸ Cambiar contraseña       {Fore.GREEN}               ║   
{Fore.GREEN}║                                   {Fore.GREEN}               ║
║      {Fore.WHITE}3 ▸ Salir                    {Fore.GREEN}               ║                       
{Fore.GREEN}║                                                  ║
║        {Fore.WHITE}Selecciona una opción: {Fore.GREEN}                   ║
║                                                  ║
╚══════════════════════════════════════════════════╝
""")

        opcion = input("Selecciona una opción: ")

        match opcion:
            case "1":
                nuevo_nombre = input("Nuevo nombre de usuario: ")
                perfil['Usuario'] = nuevo_nombre
                restart()
                print("Nombre de usuario actualizado.")
            case "2":
                nueva_pass = getpass.getpass("Nueva contraseña: ")
                perfil['Password'] = hash_password(nueva_pass)
                restart()
                print("Contraseña actualizada.")
            case "3":
                restart()
                break
            case _:
                restart()
                print("Opción inválida, intenta de nuevo.")
