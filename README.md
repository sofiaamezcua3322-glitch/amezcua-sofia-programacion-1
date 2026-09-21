# amezcua-sofia-programacion-1

Alumna: Sofia Amezcua Rosales

Curso: Programación I

Carrera: Licenciatura en Creatividad Digital

Propósito: Crear un repositorio personal que usará para resguardar prácticas,
tareas y proyectos futuros.

-----------

## Estructura de carpetas: 
Practicas: Trabajos en clase y tareas

Proyectos: Proyecto final y proyectos personales

----------

## Bitácora de Instalación y Configuración del IDE

Fecha: 21 de septiembre de 2026

Software Instalado: Visual Studio Code (VS Code)

Versión: 1.93 (Última versión estable)

Entornos y Complementos Adicionales: Extensión de Python (Microsoft) y gestor de paquetes pip (para librerías como Pygame).

1. Proceso de Descarga e Instalación:

Se descargó el instalador oficial de Visual Studio Code desde la página oficial (code.visualstudio.com).

Se ejecutó el asistente de instalación, aceptando los términos de licencia. Se marcaron las casillas para agregar la acción "Abrir con Code" al menú contextual del explorador de archivos.

Una vez dentro de la interfaz principal de VS Code, se ingresó a la pestaña de "Extensiones" (Ctrl+Shift+X) y se instaló la extensión oficial de Python para habilitar el resaltado de sintaxis, el autocompletado de código y las herramientas de depuración necesarias para los scripts de los juegos interactivos.

2. Problemas Detectados durante la Configuración:

Problema 1 (Variables de entorno): Al abrir la terminal integrada de Visual Studio Code para ejecutar un archivo .py, el sistema arrojó un error indicando que el comando python y pip no se reconocían como un comando interno o externo.

Problema 2 (Módulos no encontrados): Al intentar hacer pruebas con el código del juego de plataformas, el sistema detuvo la ejecución mostrando el error ModuleNotFoundError: No module named 'pygame', a pesar de que el código base estaba bien estructurado.

3. Soluciones Implementadas:

Solución al Problema 1: Este problema derivó de no haber marcado la casilla "Add Python to PATH" durante la instalación inicial del lenguaje. Para resolverlo directamente desde el IDE, se abrió la Paleta de Comandos (Ctrl+Shift+P), se buscó la opción "Python: Select Interpreter" y se seleccionó manualmente la ruta del ejecutable de Python instalado en el equipo. Después de esto, se cerró y se volvió a abrir la terminal de VS Code para que se actualizaran las rutas.

Solución al Problema 2: Una vez que la terminal integrada reconoció correctamente a Python, se procedió a instalar la librería faltante para el desarrollo del juego. En la misma terminal de VS Code, se introdujo el comando pip install pygame. Una vez finalizada la descarga de los paquetes, los scripts interactivos comenzaron a compilarse y ejecutarse correctamente sin errores de dependencias.

----------

##  Instrucciones breves de cómo clonar y usar el repositorio

1. Clona el repositorio
Abre tu terminal (el Símbolo del sistema, PowerShell o la terminal de Git Bash) en la carpeta donde quieras guardar el proyecto y pega este comando:

git clone https://github.com/sofiaamezcua3322-glitch/amezcua-sofia-programacion-1
(Nota: Debes tener Git instalado en tu computadora para que este comando funcione).

2. Entra a la carpeta del proyecto
Una vez que termine de descargar, métete a la carpeta que se acaba de crear escribiendo esto:

cd amezcua-sofia-programacion-1

3. Ábrelo en Visual Studio Code
Como ya tenemos configurado VS Code, para abrir todos los archivos de golpe directo ahí, nada más escribe:

code .

4. ¡Listo para trabajar!
Ya dentro de VS Code, vas a ver todos los archivos de la clase del lado izquierdo. Para usarlo:

Abre el archivo de Python (o el código que vayamos a usar) dándole doble clic.

Asegúrate de que el intérprete esté seleccionado abajo a la derecha.

Dale al botón de "Run" (el triangulito arriba a la derecha) para correr el código.
