from colorama import init, Fore, Style
init(autoreset=True)
import random
import time
import threading
import data
from utilities import restart
from tienda import saldo_user
# ============================================
# SISTEMA DE GRANJA - PRODUCCIÓN AUTOMÁTICA
# ============================================

# Producción por segundo para cada tipo de animal (mínimo, máximo)
PRODUCCION_POR_SEGUNDO = {
    "Gallina": (20, 50),      # 20-50 monedas por segundo
    "Pavo": (80, 120),         # 80-120 monedas por segundo
    "Cerdo": (120, 170),        # 120-170 monedas por segundo
    "Ovaje": (170, 200),       # 170-200 monedas por segundo
    "Vaca": (220, 260)        # 220-260 monedas por segundo
}

# Estado de la granja
granja_estado = {
    "activo": False,
    "hilo": None,
    "segundos_totales": 0,
    "dinero_generado": 0
}

def producir_cada_segundo():
    """
    Función que se ejecuta automáticamente cada segundo.
    Los animales del inventario producen dinero.
    """
    while granja_estado["activo"]:
        try:
            time.sleep(1)  # Espera 60 segundo real
            
            total_producido = 0
            animales_activos = 0
            
            # Revisar cada tipo de animal en el inventario
            for animal, cantidad in data.inventario.items():
                if cantidad > 0 and animal in PRODUCCION_POR_SEGUNDO:
                    animales_activos += cantidad
                    
                    # Calcular producción por cada animal de este tipo
                    minimo, maximo = PRODUCCION_POR_SEGUNDO[animal]
                    
                    for _ in range(cantidad):
                        data.saldo_user = random.randint(minimo, maximo)
                        total_producido += data.saldo_user
            
            if total_producido > 0:
                # Actualizar saldo global
                data.saldo_user += total_producido
                
                granja_estado["segundos_totales"] += 1
                granja_estado["dinero_generado"] += total_producido
                
                # Mostrar cada 5 segundos para no saturar la consola
                if granja_estado["segundos_totales"] % 5 == 0:
                    print(f"\n💰 [GRANJA] {animales_activos} animales generaron {total_producido} G")
                    print(f"🏦 Saldo actual: {saldo_user} G")
                    print(f"📊 Total generado: {granja_estado['dinero_generado']} G")
        except Exception as e:
            print(f"⚠️ Error en producción: {e}")
            time.sleep(1)
            continue

def iniciar_granja():
    """Inicia el sistema de producción automática de la granja"""
    try:
        
        if granja_estado["activo"]:
            print(f"{Fore.CYAN}\n La granja ya está activa")
            return
        
        # Contar animales disponibles
        total_animales = sum(data.inventario.values())
        
        if total_animales == 0:
            print(f"{Fore.RED}\n No tienes animales en tu inventario.")
            print(" vuelva con la (opcion 4) para ir a la tienda .")
            return
        
        granja_estado["activo"] = True
        granja_estado["segundos_totales"] = 0
        granja_estado["dinero_generado"] = 0
        
        hilo = threading.Thread(target=producir_cada_segundo, daemon=True)
        hilo.start()
        granja_estado["hilo"] = hilo
        
        
        print(f"""
{Fore.GREEN}╔══════════════════════════════════════════════════╗
║                                                  ║
║             {Fore.CYAN}🌱 ¡GRANJA INICIADA CON ÉXITO! 🌱{Fore.GREEN}             ║
║                                                  ║
║   {Fore.WHITE}Tus {Fore.YELLOW}{total_animales}{Fore.WHITE} animales comenzarán a producir dinero.  ║
║
║   {Fore.WHITE}⏱️  Producción automática cada {Fore.CYAN}60 segundos{Fore.WHITE}.              ║
║
║   {Fore.WHITE}🧺  Puedes seguir usando el menú mientras la         ║
║       producción continúa.                                ║
║                                                  ║
╚══════════════════════════════════════════════════╝
""")
    except Exception as e:
        print(f"{Fore.RED}\n Error al iniciar granja: {e}")

def detener_granja():
    """Detiene el sistema de producción automática"""
    if not granja_estado["activo"]:
        print(f"{Fore.RED}\n  La granja no está activa")
        return
    
    granja_estado["activo"] = False
    
    print(f"""
{Fore.GREEN}╔══════════════════════════════════════════════════╗
║                                                  ║
║              {Fore.RED}🛑  ¡GRANJA DETENIDA!  🛑{Fore.GREEN}                 ║
║                                                  ║
║   {Fore.CYAN}📊  Estadísticas finales:{Fore.WHITE}                      ║
║                                                  ║
║     ⏱️  Tiempo activo: {Fore.YELLOW}{granja_estado['segundos_totales']}{Fore.WHITE} segundos      ║
║
║     💰  Dinero generado: {Fore.YELLOW}{granja_estado['dinero_generado']}{Fore.WHITE} G             ║
║                                                  ║
╚══════════════════════════════════════════════════╝
""")
def ver_estado_granja():
    """Muestra el estado actual de la granja"""
    try:
        print("\n" + "=" * 55)
        print(" ESTADO DE LA GRANJA ".center(55))
        print("=" * 55)
        
        if granja_estado["activo"]:
            print("Estado:ACTIVA")
        else:
            print("Estado:INACTIVA")
        
        print(f"Saldo actual: {saldo_user} G")
        print(f"Dinero generado por la granja: {granja_estado['dinero_generado']} G")
        print(f"Tiempo activo: {granja_estado['segundos_totales']} segundos")
        print("-" * 55)
        print(" TUS ANIMALES:")
        print("-" * 55)
        
        total_animales = 0
        animales_encontrados = False
        
        for animal, cantidad in data.inventario.items():
            if cantidad > 0:
                animales_encontrados = True
                emoji = {"Gallina": "🐔", "Pavo": "🦃", "Cerdo": "🐖", "Ovaje": "🐑", "Vaca": "🐄"}
                prod_min, prod_max = PRODUCCION_POR_SEGUNDO.get(animal, (0, 0))
                print(f"{emoji.get(animal, '🐾')} {animal}: {cantidad} unidades ({prod_min}-{prod_max} G/m)")
                total_animales += cantidad
        
        if not animales_encontrados:
            print(f" {Fore.RED}No tienes animales en tu granja")
            print(f" {Fore.LIGHTGREEN_EX}Compra animales en la Tienda (opción 3 del menú principal)")
        else:
            print("-" * 55)
            print(f"Total: {total_animales} animales")
        
        print("=" * 55 + "\n")
    except Exception as e:
        print(f"\nError al mostrar estado: {e}\n")

def menu_granja():
    """Menú principal de la granja - Se puede llamar desde game.py con case 2"""
    try:
        while True:
            print(f"""
{Fore.GREEN}╔══════════════════════════════════════════════════╗
║                                                  ║
║                    {Fore.CYAN}🌾  MENÚ GRANJA  🌾{Fore.GREEN}                    ║
║                                                  ║
║      {Fore.WHITE}1 ▸ Ver estado de la granja        {Fore.GREEN}🌱
║
║      {Fore.WHITE}2 ▸ Iniciar producción automática  {Fore.YELLOW}⚙️
║
║      {Fore.WHITE}3 ▸ Detener producción             {Fore.RED}⛔
║
║      {Fore.WHITE}4 ▸ Volver al menú principal       {Fore.MAGENTA}🏡
{Fore.GREEN}║                                                  ║
║        {Fore.WHITE}Elige una opción: {Fore.GREEN}                     ║
║                                                  ║
╚══════════════════════════════════════════════════╝
""")
            
            opcion = input("\n> Elige una opción: ").strip()
            
            if opcion == "1":
                restart()
                ver_estado_granja()
            
            elif opcion == "2":
                restart()
                iniciar_granja()
            
            elif opcion == "3":
                restart()
                detener_granja()
            
            elif opcion == "4":
                restart()
                print("\n👋 Volviendo al menú principal...")
                break
            
            else:
                restart()
                print("\n❌ Opción inválida. Elige una opción del 1 al 4.")
    except KeyboardInterrupt:
        print("\n\n Menú interrumpido")
        detener_granja()
    except Exception as e:
        print(f"\n Error en el menú de granja: {e}")


# ============================================
# PARA PRUEBAS INDEPENDIENTES
# ============================================

if __name__ == "__main__":
    print("\nSISTEMA DE GRANJA - MODO PRUEBA")
    print("=" * 55)
    
    # Simular algunos animales en el inventario para pruebas
    try:
        print("✅ Módulo data.py cargado correctamente")
        print(f"📊 Saldo inicial: {data.saldo_user} G")
        
        # Agregar animales de prueba
        data.inventario["Gallina"] = 2
        data.inventario["Vaca"] = 1
        print("✅ Animales de prueba agregados (2 Gallinas, 1 Vaca)")
        print()
        
        menu_granja()
    except ImportError:
        print(" No se pudo importar data.py")
        print(" Asegúrate de que data.py está en la misma carpeta")