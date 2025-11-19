Game
🌾 ExcelRaincher 🐔 Un mini‑juego de simulación agrícola creado por Crudzaso Games 🎮 Descripción del juego

ExcelRaincher es el primer mini‑juego desarrollado por Crudzaso Games, un proyecto que combina diversión, estrategia y crecimiento. Te conviertes en un granjero que inicia con una humilde gallina y, a través de compras inteligentes y decisiones estratégicas, podrás hacer crecer tu propia granja.

A medida que tus animales generan ganancias, podrás reinvertir tus ingresos para adquirir nuevos animales, cada uno con distintos niveles de producción.

💡 Objetivo del juego: Expandir tu granja lo máximo posible y reunir la mayor cantidad de animales para maximizar tus ganancias.

🚀 ¿Cómo jugar? 1️⃣ Instalar Visual Studio Code

Ve a: code.visualstudio.com

Descarga la versión compatible con tu sistema operativo (Windows, Linux o macOS)

Ejecuta el instalador

Abre la terminal con Ctrl + Alt + T y escribe:

code

Se recomienda usar la versión 1.105.1

2️⃣ Verificar que tienes Python 3.12.3 instalado

Entra a: python.org

Descarga la versión Python 3.12.3

Ejecuta el instalador

Verifica la instalación con:

python –version

Deberías ver: Python 3.12.3

3️⃣ Descargar el juego

Clona o descarga este repositorio.

4️⃣ Abrir el proyecto

Dirígete a la carpeta donde se encuentren los archivos.

5️⃣ Ejecutar el juego

Abre el archivo principal:

main.py

¡Y listo! 🎉 Tendrás tu primera gallina lista para empezar a generar monedas.

📚 Librerías utilizadas 🔧 Dependencias principales

uuid → Genera identificadores únicos de sesión.

getpass → Solicita contraseñas ocultas para mayor seguridad.

hashlib → Permite crear hash para verificar contraseñas.

colorama → Añade color al juego para una visual más atractiva.

random → Utilizado para generar ganancias aleatorias.

time → Se usa para medir el tiempo activo de cada animal.

threading → Permite procesar varias tareas en paralelo.

os → Limpia la consola y mejora la navegación dentro del juego.

🐄 Sistema de gestión de información

El juego administra toda la información relacionada con la granja del jugador, incluyendo:

🐾 Animales disponibles:

Gallinas

Pavos

Cerdos

Ovejas

Vacas

Cada uno cuenta con:

Su propio costo 💰

Proceso de compra y venta 🔄

Un sistema de generación de dinero ⏳

Toda esta información se gestiona mediante estructuras como diccionarios y funciones que actualizan el estado del juego en tiempo real.

Además:

Se lleva control del dinero disponible

Se calculan las ganancias continuas generadas por todos los animales

La información de la granja se actualiza en pantalla en tiempo real, facilitando decisiones estratégicas

🧪 Estado del proyecto

Este es el primer mini‑juego de la empresa y se encuentra en fase de desarrollo y mejora continua.

👨‍💻 Desarrollado por

Crudzaso Games
