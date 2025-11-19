from data import inventario, opciones_animales, precios_animales, saldo_user
from colorama import Fore, Style, init
init(autoreset=True)
from utilities import restart

def mostrar_tienda():
    print(Fore.YELLOW + f"""
    ╔══════════════════════════════════════════════════════╗
    ║{Fore.CYAN}                 🚜  TIENDA  🚜                       {Fore.YELLOW}║
    ║{Fore.CYAN}                                                      {Fore.YELLOW}║
    ╠══════════════════════════════════════════════════════╣
    ║{Fore.GREEN}               ┌─────────────────┐                    {Fore.YELLOW}║
    ║{Fore.GREEN}               │    COMPRAR 🛒                        {Fore.YELLOW}║
    ║{Fore.GREEN}               └─────────────────┘                    {Fore.YELLOW}║
    ║{Fore.GREEN}       Precio Compra     |  Precio Venta              {Fore.YELLOW}║
    ║{Fore.GREEN}-------------------------+----------------------------{Fore.YELLOW}║
    ║{Fore.WHITE}   [1] Gallina 🐔 150 G  |       120 G                {Fore.YELLOW}║
    ║{Fore.WHITE}   [2] Pavo    🦃 220 G  |       176 G                {Fore.YELLOW}║
    ║{Fore.WHITE}   [3] Cerdo   🐖 300 G  |       240 G                {Fore.YELLOW}║
    ║{Fore.WHITE}   [4] Oveja   🐑 400 G  |       320 G                {Fore.YELLOW}║
    ║{Fore.WHITE}   [5] Vaca    🐄 600 G  |       480 G                {Fore.YELLOW}║
    ╠──────────────────────────────────────────────────────╣
    ║{Fore.MAGENTA}                ┌─────────────────┐                   {Fore.YELLOW}║
    ║{Fore.MAGENTA}                │     VENDER 📦    │                  {Fore.YELLOW}║
    ║{Fore.MAGENTA}                └─────────────────┘                   {Fore.YELLOW}║
    ║{Fore.WHITE}                                                      {Fore.YELLOW}║
    ║{Fore.WHITE}   [6] Vender animales                                {Fore.YELLOW}║
    ╠──────────────────────────────────────────────────────╣
    ║{Fore.RED}                ┌─────────────────┐                   {Fore.YELLOW}║
    ║{Fore.RED}                │     SALIR 🚪     │                  {Fore.YELLOW}║
    ║{Fore.RED}                └─────────────────┘                   {Fore.YELLOW}║
    ║{Fore.WHITE}   [7] Salir de la tienda                             {Fore.YELLOW}║
    ╚══════════════════════════════════════════════════════╝
    """)
    print(f"Tu saldo actual es de: {Fore.LIGHTYELLOW_EX}{saldo_user} G\n")
def compra_animales():
    global saldo_user
    val_opcion = True
    print(f"{Fore.RED}Elige una opcion".center(30))
    while val_opcion:
        opcion = input(f"{Fore.LIGHTWHITE_EX}> ")
        if not opcion.isdigit():
            print("Ingrese una opcion valida del menu de la Tienda.")
            continue
        else:
            val_opcion = False
    opcion = int(opcion)
    match opcion:
        case 1 | 2| 3 | 4 | 5:
            animal = opciones_animales[opcion]
            precio = precios_animales[animal]
            val_cant = True
            while val_cant:
                cantidad = input(f"Cuant@s {Fore.CYAN}{animal}s{Style.RESET_ALL} quieres comprar?: ")
                if cantidad.isdigit():
                    cantidad = int(cantidad)
                    val_cant = False
                else:
                    print(f"{Fore.RED}Ingresa una cantidad valida")
            total = precio * cantidad
            restart()
            print(f"El total a pagar seria {Fore.YELLOW}{total} G")
            
            if saldo_user >= total:
                saldo_user -= total
                inventario[animal]+= cantidad
                print(f"{Fore.LIGHTCYAN_EX}Tu compra ha sido exitosa!")
            else:
                restart()
                print(f"{Fore.RED}No tienes saldo suficiente para este compra.\n")
            mostrar_tienda()
            compra_animales()
        case 6:
            animales_en_stock = {animal: cantidad for animal, cantidad in inventario.items() if cantidad > 0}
            if len(animales_en_stock) == 0:
                print(f"{Fore.RED}No tienes animales para vender.")
                mostrar_tienda()
                compra_animales()
                return
            else:
                for animal, cantidad in animales_en_stock.items():
                    print(f"- {animal}: {cantidad}")
            print("\nQue animal deseas vender?\n")
            
            opciones_vender = {}
            numero = 1
            for animal in animales_en_stock:
                opciones_vender[numero] = animal
                print(f"[{numero}] {animal}")
                numero += 1
            val_opcion = True
            while val_opcion:
                opcion_v = input(">Elige una opcion: ")
                if opcion_v.isdigit() and int(opcion_v) in opciones_vender:
                    opcion_v = int(opcion_v)
                    val_opcion = False
                else:
                    print(f"{Fore.RED}Opcion invalida.")
            animal_elegido = opciones_vender[opcion_v]
            val_cantidad_venta = True
            while val_cantidad_venta:
                cantidad_v = input(f"Cuantos {Fore.LIGHTCYAN_EX}{animal_elegido}s{Style.RESET_ALL} deseas vender?: ")
                if cantidad_v.isdigit():
                    cantidad_v = int(cantidad_v)
                    if cantidad_v <= animales_en_stock[animal_elegido]:
                        val_cantidad_venta = False
                    else:
                        print(f"{Fore.RED}No tienes cantidad disponible")
                else:
                    print(f"{Fore.RED}Ingrese un valor valido.")
            precio_compra = precios_animales[animal_elegido]
            precio_venta = int(precio_compra * 0.8)
            total_venta = precio_venta * cantidad_v
            inventario[animal_elegido] -= cantidad_v
            saldo_user += total_venta
            restart()
            print(f"\nVendiste {cantidad_v} {Fore.LIGHTCYAN_EX}{animal_elegido}(s){Fore.RESET} por {Fore.YELLOW}{total_venta} G.")
            print(f"Nuevo saldo: {Fore.YELLOW}{saldo_user} G")
            mostrar_tienda()
            compra_animales()
        case 7:
            restart()
            return
        case _:
            print("Opcion invalida.")
