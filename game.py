from colorama import init, Fore, Style
init(autoreset=True)
from tienda import mostrar_tienda, compra_animales
from perfil import modificar_perfil
from utilities import restart
menu = True
def menu_principal(): 
    print(f"""
{Fore.GREEN}╔══════════════════════════════════════════════════╗
║                                                  ║
║               {Fore.YELLOW}🌾 {Fore.CYAN}MENU PRINCIPAL{Fore.YELLOW} 🌾{Fore.GREEN}               ║
║                                                  ║
║      {Fore.WHITE}1 ▸ Perfil   👤                             {Fore.GREEN}║
║                                                  ║
{Fore.GREEN}║      {Fore.WHITE}2 ▸ Granja   {Fore.GREEN}🌱                             ║
║                                                  ║
║      {Fore.WHITE}3 ▸ Tienda   {Fore.MAGENTA}🛒           {Fore.GREEN}                  ║
║                                                  ║
║      {Fore.WHITE}4 ▸ Salir    {Fore.YELLOW}🐓            {Fore.GREEN}                 ║ 
{Fore.GREEN}║                                                  ║
║        {Fore.WHITE}Ingrese una opción{Fore.GREEN}                        ║
║                                                  ║
╚══════════════════════════════════════════════════╝
""")
def opciones_menu_pp(registrados, usuario_act):
    global menu
    print(f"""{Fore.GREEN}
                        🌿        .            .      🌾
                {Fore.GREEN}        ~^~    .         .        ~^~
        {Fore.GREEN}       ~^~    ~^~      .       ~^~      ~^~      . 
    {Fore.GREEN}   ~^~  ~^~   ~^~   ~^~    .    ~^~   ~^~   ~^~
{Fore.GREEN}  ~^~  ~^~  ~^~  ~^~  ~^~  ~^~   ~^~  ~^~  ~^~  ~^~  ~^~
{Fore.GREEN}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{Fore.YELLOW}                /\        /\         /\        /\ 
{Fore.YELLOW}       /\      /  \  /\  /  \  /\   /  \  /\  /  \   /\ 
{Fore.YELLOW}    __/  \____/    \/  \/    \/  \_/    \/  \/    \_/  \__
{Fore.YELLOW}~~~                                                    ~~~

{Style.RESET_ALL}{Fore.WHITE}
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   {Fore.CYAN}¡Bienvenido a Excel Rancher! 🌿✨{Fore.WHITE}                                  ║
║                                                                      ║
║   Un mundo de pixel-aventuras te espera: animales por cuidar,        ║
║   estaciones por descubrir y una granja lista para florecer          ║
║   contigo día a día. {Fore.GREEN}🌾💚{Fore.WHITE}                                            ║
║                                                                      ║
║   Respira profundo, toma tus herramientas…                           ║
║   ¡tu historia en Excel Rancher está por comenzar!                   ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║                 {Fore.MAGENTA}⇦  Presiona ENTER para continuar  ⇨{Fore.WHITE}                  ║
╚══════════════════════════════════════════════════════════════════════╝
{Fore.GREEN}
""")
    input()
    restart()
    while menu:
        menu_principal()
        op_menu = input(f"> ")
        if  not op_menu.isdigit():
            print("Inserte una opcion valida del menu.")
            continue
        else:
            pass
        op_menu = int(op_menu)
        match op_menu:
            case 1:
                restart()
                modificar_perfil(registrados, usuario_act)
            case 2:
                restart()
                import granja
                granja.menu_granja()
            case 3:
                restart()
                mostrar_tienda()
                compra_animales()
            case 4:
                restart()
                break
            case _:
                restart()
                print("Ingrese una opcion valida del menu.")

