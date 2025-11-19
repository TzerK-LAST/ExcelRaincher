
from data import registrados
from auth import autenticacion_sesion, registrar_usuario
import getpass
import game
from utilities import restart
from colorama import init, Fore, Style
init(autoreset=True)
restart()
def login_user():
    opcion = ""
    while opcion != "3":
        print(f"""{Fore.GREEN}
                    ~^~         .         ~^~
            ~^~   .        ~^~         .        ~^~
        ~^~  ~^~   ~^~    ~^~      .       ~^~     ~^~
{Fore.GREEN}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

{Style.RESET_ALL}{Fore.WHITE}
╔══════════════════════════════════════════════════════════════════════╗
║                              {Fore.CYAN}LOGIN MENU{Fore.WHITE}                              ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║                         1 ▸ Iniciar Sesión                           ║
║                         2 ▸ Registrarse                              ║
║                         3 ▸ Salir                                    ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                  {Fore.MAGENTA}⇦  Selecciona una opción  ⇨{Fore.WHITE}                         ║
╚══════════════════════════════════════════════════════════════════════╝

{Fore.GREEN}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
        opcion = input(f"{Fore.BLUE}> {Style.RESET_ALL}")

        if opcion == "1":
            usuario = input("Ingresa tu usuario: ")
            password = getpass.getpass("Ingresa tu contraseña: ")
            if autenticacion_sesion(usuario, password, registrados):
                print(f"Bienvenido {usuario}")
                restart()
                game.opciones_menu_pp(registrados, usuario)
            else:
                restart()
                print(f"{Fore.RED}Usuario/Contraseña Incorrectos, vuelve a intentarlo")

        elif opcion == "2":
            usuario = input("Ingresa tu nombre de usuario: ")
            password = getpass.getpass("Ingresa tu contraseña: ")
            if registrar_usuario(usuario, password, registrados):
                restart()
                print(f"{Fore.GREEN}Te registraste con éxito!")
            else:
                restart()
                print(f"{Fore.RED}Error, usuario ya existente, inténtalo de nuevo")

        elif opcion == "3":
            print("Hasta luego!")
        else:
            print(f"{Fore.RED}Error, opción invalida")
login_user()
