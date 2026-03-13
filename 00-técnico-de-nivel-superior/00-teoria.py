"""
_______________________________________________________
HARDWARE:
-------------------------------------------------------

Se provee los componentes fisicos necesarios para que funcione los
procesos y programas. Ej:
    ● Procesador (CPU): Se encarga de interpretar y ejecutar programas.
    ● Memoria RAM: Almacena temporalmente datos e instrucciones para la CPU.
    ● Disco Duro o SSD: almacena para el S.O., aplicaciones y datos del usuario.
    ● Tarjeta Gráfica (GPU): Maneja los cálculos necesarios para gráficos y videos.
    ● Dispositivos de Entrada: teclado, mouse, micrófono, escáner, cámara, 
pantallas táctiles, tabletas gráficas, lectores de código o QR y por ultimo
si la impresora es con escaner si es de entrada ahora sin escaner la impresora
es de salida, etc.
    ● Dispositivos de salida: monitor o pantalla, impresora, parlantes, auriculares,
proyector, actuadores o luces indicadoras, etc.

_______________________________________________________
SOFTWARE: Conjunto de programas que gestionan las operaciones del computador.
-------------------------------------------------------
Tipos de SOFTWARE:
    ● Base.
    ● Aplicación.
    ● Desarrollo.
    ● Comunicación.

● Base: conjunto de programas esenciales que sirven de soporte para su uso.
Además permite que el usuario pueda interactuar con el HARDWARE. Ej:
    - Utilitarios básicos: BIOS/UEFI, herramientas de diagnóstico, gestores de archivos, 
etc. Realizan tareas esenciales de configuración, arranque y mantenimiento.
    - SO(SISTEMA OPERATIVO): Windows, MacOS, Linux, Android, etc.  
Administrar recursos del hardware y ofrece interfaz al usuario.
    - Controladores (drivers): impresora, tarjeta gráfica, tarjeta de sonido, etc. 
Permiten que el sistema operativo se comunique con periféricos específicos.
    - Entornos de programación de sistema: GNU, compiladores básicos, intérpretes 
de comandos. Facilitan la interacción con el sistema y el desarrollo de software.

-----------------------------------------------------------------------------------------
● Aplicación: son diseñados o creados para los usuarios finales. Ej:
    - Productividad para realizar tareas específicas: Microsoft Office (Word, Excel, 
PowerPoint), Google Workspace (Docs, Sheets, Slides).
    - Entretenimiento y recreación: Juegos de video (The Sims, Fortnite), reproductores 
multimedia (VLC, Windows Media Player).
    - Educación facilitan el aprendizaje: Khan Academy, Duolingo, Blackboard.
    - Diseño y Creatividad son para crear y editar gráficos, videos y otros contenidos 
creativos: Adobe, Photoshop, CorelDRAW, Final Cut Pro.

-----------------------------------------------------------------------------------------
● Desarrollo: son programas para crear, depurar, mantener y mejorar codigos  
de otros programas. Ej:
    - Entornos de Desarrollo Integrados (IDE): Visual Studio, IntelliJ IDEA, Eclipse.
    - Editores de Texto Avanzados: Visual Studio Code, Sublime Text, Atom.
    - Sistemas de Control de Versiones: Git.
    - Herramientas de Compilación y Automatización: Maven, Gradle, Ant.
    - Depuradores: GDB (GNU Debugger), LLDB.

-----------------------------------------------------------------------------------------
● Comunicaciones: facilita la transferencia de información entre usuarios y 
sistemas. Estos serían aplicaciones de mensajería, correo electrónico, protocolos 
y servicios. Ej: 
    - Correo electrónico envío y recepción de mensajes y archivos: Gmail, Hotmail, 
    etc.
    - Mensajería instantánea mensajes de texto, voz y video: WhatsApp, Telegram.
    - Videoconferencia reuniones virtuales de video y audio: Zoom, Microsoft Teams, 
    Google Meet.
    - Protocolo de Transferencia de Archivos (FTP) transferencia de archivos de 
    manera segura: FileZilla, WinSCP.
    - Servicios Web se comunican entre sí utilizando protocolos HTTP: REST, SOAP.
    - Middleware comunicación e intercambio de datos entre diferentes aplicaciones y 
    servicios de una arquitectura: Apache Kafka, RabbitMQ.

-----------------------------------------------------------------------------------------
    * Propietario: desarrollado por una empresa o un individuo con derechos exclusivos 
    sobre su uso. Bajo licencia. Además es respaldada por un soporte técnico. Ej:
        - Sistemas Operativos. Windows, macOS.
        - Ofimática. Microsoft Office, Adobe Acrobat.
        - Entornos de desarrollo integrados (IDE). Microsoft Visual Studio. 
        IntelliJ IDEA.

    * Libre: es código fuente que está disponible para que cualquiera lo use. Además 
    ofrece beneficios técnicos, económicos y promueve la colaboración y acceso al 
    conocimiento. Cuatro libertades esenciales para usar el software libre:
    - Libertad 0: ejecutar el programa como se desee, para cualquier propósito.
    - Libertad 1: estudiar cómo funciona y modificarlo a gusto del usuario.
    - Libertad 2: redistribuir copias.
    - Libertad 3: redistribuir copias de versiones modificadas.
    * Open source: aunque el software libre es muy parecido, cuando hablamos de open 
    source nos referimos al código abierto como una herramienta de colaboración y 
    desarrollo técnico. En cambio, el software libre enfatiza las libertades del 
    usuario al usar, modificar y distribuir el programa.

_______________________________________________________
#! PROGRAMACIÓN
-------------------------------------------------------
¿Qué es la programación? 
Es la comunicación entre persona/maquina de manera legible para pasar a ser
traducido en bits. 
¿Qué es programar? 
Es un conjunto de instrucciones para usarlos en uno o varios lenguajes de 
programación.
    * Ámbitos de la programación: 
        Videojuegos, aplicaciones Web, programas, sistemas de control, Testing QA, 
        datos, inteligencia artificial, etc. para diferentes dispositivos.
    * Lenguaje De Programación: 
        Usa reglas gramaticales y sintácticas por un programador donde escribe 
        instrucciones o secuencias de órdenes tambien llamado código fuente.
    * Alfabeto: 
        Es el conjunto de símbolos que un lenguaje de programación reconoce como 
        válidos. Incluye letras, números, signos de puntuación y operadores. Es 
        como el “abecedario” del lenguaje.
    * Léxico: 
    Son las reglas que indican cómo se pueden combinar esos símbolos del alfabeto 
    para formar unidades con significado llamadas tokens.
    * Tokens:
        Son las piezas mínimas que el compilador entiende. Pueden ser palabras 
reservadas (como if, while, return), identificadores (nombres de variables o funciones), 
números, operadores (+, -, *, /), etc.
    * Palabras reservadas: 
    Son tokens especiales que ya tienen un significado definido en el lenguaje y 
    no se pueden usar para otra cosa. 
    * TOKENS:
        - Identificador que elige el programador: x, largo, PI.
        - Palabras Claves o Reservadas del lenguaje: If, while, return.
        - Literal de referencia o de asignación: false, “cumpleaños”, 6,47989e-5.
        - Operador de simbolos sobre argumentos y dan su resultado: -, +, <, >=, =, ^.
        - Delimitador o separador: (), {}, "", ``;
        - Comentario que no seran ejecutados: Ej en PYTHON 
    “””puede ser muy largo”””, #hasta fin de línea.
    * Sintáctico: 
    Se define si una oracion o contruccion esta escrita correctamente.
    * Semántico: 
    Se define si una frase tiene sentido y le da un significado a sus elementos 
    y expresiones.

_______________________________________________________
Lenguajes De Bajo Nivel: 
Son lenguajes cercanos al hardware, dependientes de las instrucciones de la CPU. No son 
portables entre distintos procesadores.
    - Lenguaje máquina: instrucciones reconocidas directamente por los circuitos del 
procesador. Se codifican en binario (0 y 1). Los datos se referencian por su 
posición de memoria.
    - Lenguaje ensamblador: representación simbólica del lenguaje máquina mediante 
códigos mnemotécnicos (palabras cortas y fáciles de recordar). Necesita un traductor 
(ensamblador) para convertirse en lenguaje máquina. Permite usar etiquetas en lugar 
de posiciones de memoria.

Lenguajes De Alto Nivel:
Son lenguajes creados para superar las dificultades de los lenguajes de bajo nivel. 
Se caracterizan por ser más fáciles de escribir, leer y comprender, ya que usan una 
sintaxis cercana al lenguaje humano o matemático.

    - Clasificación histórica: se dividen en generaciones (1ra, 2da, 3ra, 4ta y 5ta) según 
la evolución de sus características y nivel de abstracción.

    - Clasificación alto o bajo nivel: depende de la cercanía al hardware. Los de alto 
nivel tienen mayor abstracción y son independientes del procesador; los de bajo nivel 
dependen directamente de la CPU.

    - Clasificación por paradigmas: el paradigma es el modelo o estilo de programación.
        * Imperativa, orientada a objetos y dirigida por eventos de paradigmas 
    procedurales (describen pasos a seguir).
        * Funcional y lógico: paradigmas declarativos (describen el problema a resolver).
    - Clasificación por propósito: distingue entre lenguajes de propósito general 
(usados en múltiples áreas) y lenguajes de propósito específico (enseñanza, cálculo 
científico, gestión, inteligencia artificial, multiplataforma, internet).

    - Clasificación según administración de memoria: puede ser estática (reservada de 
forma fija), en pila (asignada en bloques temporales) o dinámica (asignada y liberada en 
tiempo de ejecución).

    - Clasificación según la forma de traducir a lenguaje máquina: pueden ser interpretados 
(ejecutados línea por línea por un intérprete) o compilados (traducidos completos a lenguaje 
máquina antes de ejecutarse).
_______________________________________________________

Interpretación vs Compilación:

     📌 Compilación:
        * El compilador traduce todo el código fuente de una sola vez.
        * El resultado es un archivo binario (ejecutable) que la computadora 
        entiende directamente.
        * Una vez compilado:
            No se necesita el código fuente para ejecutar el programa.
            El programa se ejecuta más rápido.
            Para usarlo en otra máquina:
            Solo se distribuye el archivo binario (si es compatible con el sistema).
        * Ejemplos de lenguajes compilados: C, C++, Go.

    📌 Interpretación:
        * El intérprete lee el código fuente línea por línea.
        * Cada línea se traduce a lenguaje máquina en el momento de ejecutarse.
        * Cada vez que se ejecuta el programa:
        * El intérprete vuelve a leer y traducir todo el código.
        * Para usarlo en otra máquina:
            Se necesita el código fuente y el intérprete instalado.
        * Ejemplos de lenguajes interpretados: Python, JavaScript, Ruby.

¿Cómo resolver el problema? ¿Por donde empiezo?

1. Comprender el problema: 
- ¿Cuál es el problema que requiere una solución? 
- ¿Cuales son las entradas y salidas esperadas?
2. Analizar ejemplos:
- ¿Identificar ejemplos de entrada y salida con valores concretos?
- ¿Cuáles son sus tipos de datos?
- ¿Se requieren validaciones?
- ¿Qué patrones o reglas podemos identificar en esos ejemplos?
3. Diseñar la solución:
- ¿Es posible resolverlo matematicamente? y si es asi, 
¿Cómo lo realizarias con lapiz y papel?
- ¿Existe una funcion de python(u otro lenguaje) que lo resuelva? y si es asi,
investigar sobre la misma a fin de evaluar si es factible utilizarla en tu programa.
- ¿Existe condiciones o restricciones especificas? es decir,
- ¿Sucede bajo ciertas condiciones?
- ¿Existen instrucciones que se repiten? o bien ¿Requiere recorrer una lista o arreglo?
4. Codificar:
- Codifica la solución. Utiliza las herramientaas de depuración de código para
ayudarte en caso de ser necesario.
5. Optimizar:
- La solución ¿Es eficiente? ¿Puede mejorarse? ¿Hay casos extremos que deberia
considerar?

_______________________________________________________

🔍 Análisis del Problema

Una vez comprendido el problema, se debe identificar:
    ● Datos de entrada: información que recibe el sistema.
    ● Datos de salida: resultados que se desean obtener.
    ● Procesos: métodos, fórmulas o cálculos necesarios.
Una buena práctica es pensar como si fueras la computadora, es decir:
    ● ¿Qué instrucciones necesito?
    ● ¿En qué orden debo ejecutarlas?

🧠 Diseño del Algoritmo

    ● En esta etapa se define cómo se va a resolver el problema paso a paso.
    ● Antes de escribir código:
        - Se aplica el pensamiento computacional.
        - Se divide el problema en acciones claras, lógicas y ordenadas.

📘 ¿Qué es un algoritmo?
    Un algoritmo es una secuencia finita, ordenada y no ambigua de 
    instrucciones que permite resolver un problema específico.

✅ Características de un algoritmo

Un buen algoritmo debe ser:
    ● No ambiguo: cada paso se interpreta de una sola manera.
    ● Finito: tiene inicio y fin.
    ● Ordenado: los pasos siguen una secuencia lógica.
    ● Definido: no admite dobles interpretaciones.
    ● General: sirve para distintos casos similares.
    ● Eficiente: se ejecuta en un tiempo razonable.

INICIO
1- Verificar si hay café molido
2- Si no hay, comprar café
3- Llenar la cafetera con agua
4- Colocar el filtro
5- Agregar el café molido
6- Encender la cafetera
7- Esperar
8- Servir el café
FIN

_______________________________________________________

Diagramas de Flujo:
Es la representación gráfica de un algoritmo, donde los pasos se muestran de forma 
secuencial y lógica mediante símbolos especiales conectados por líneas.

Importancia de los diagramas de flujo: 
    Cumplen un rol fundamental en la programación porque:
        * Facilitan la comprensión de problemas complejos.
        * Se elaboran antes de escribir el código fuente.
        * Mejoran la comunicación entre programadores y usuarios.
        * Permiten detectar errores lógicos de manera temprana.
        * Ayudan a visualizar claramente el funcionamiento del algoritmo.

    ¿Cómo se representa un diagrama de flujo?:
    * Se utilizan símbolos gráficos, cada uno con un significado específico.
    * Los símbolos representan procesos, decisiones, entradas y salidas. 
    * Las líneas de flujo indican el orden en que deben ejecutarse las acciones.
    * Los símbolos están normalizados por ANSI, lo que garantiza una interpretación 
    estándar.

    ¿Qué representa cada dibujo?
    * Circulo: Countinuidad del diagrama en la misma pagina.
    * Flecha Cuadrada: Conector hacia otra pagina.
    * Flecha Redondeada: Salida de información en pantalla.
    * Cuadro tras cuadro (DOCUMENTOS MULTIPLES): Salida de información por impresora
    * Flechas: Lineas en dirección donde la secuencia de las operaciones se realizan

Cálculo del volumen de una caja:
En el ejemplo mencionado, el diagrama de flujo muestra el proceso para calcular 
el volumen de una caja a partir de sus dimensiones:
    Entradas: valores a, b y c
    Proceso: multiplicar las dimensiones
    volumen = a x b x c
    Salida: volumen de la caja

Recomendaciones para diseñar diagramas de flujo:
    Para que un diagrama sea claro y correcto, se recomienda:
        * Usar únicamente líneas horizontales y/o verticales.
        * Evitar el cruce de líneas, utilizando conectores si es necesario.
        * Usar conectores solo cuando sea indispensable.
        * No dejar líneas de flujo sin conectar.
        * Disponer los símbolos para que se lean de arriba hacia abajo y de 
    izquierda a derecha.
        * Escribir textos claros y breves dentro de los símbolos, evitando 
    frases largas.

Idea clave para memorizar
    Un diagrama de flujo permite ver el algoritmo, entenderlo antes de 
    programar y detectar errores sin escribir código.

_______________________________________________________

Pseudocódigo:
El pseudocódigo es una de las herramientas de diseño más utilizadas en 
programación para resolver problemas informáticos. Permite expresar la solución 
de un problema de forma clara y detallada, de manera muy cercana a un lenguaje 
de programación real.

Es una mezcla entre lenguaje humano (español, inglés u otro) y 
lógica de programación.

¿Para qué se usa el pseudocódigo?: 
    * Para diseñar programas antes de escribir código real.
    * Para representar los pasos de un algoritmo de forma ordenada.
    * Para expresar la lógica del problema sin depender de un lenguaje específico.
    * Para facilitar la traducción posterior a un lenguaje de programación.

El pseudocódigo no es un lenguaje de programación, pero utiliza instrucciones 
similares. Además el pseudocódigo puede ser trasladado directamente a un lenguaje real,
no es recomendable programar directamente.

Esto se debe a que:
    * Se pueden cometer errores lógicos.
    * Falta planificación.
    * El código se vuelve más difícil de corregir y entender.

Características del pseudocódigo:
    * Describe pasos claros y precisos.
    * Sigue una secuencia lógica.
    * Produce siempre el mismo resultado si se usan los mismos datos de entrada.
    * Tiene un inicio y un fin, por lo tanto es finito.

Ventajas del pseudocódigo frente al diagrama de flujo:
    * Ocupa menos espacio.
    * Permite representar operaciones repetitivas complejas con mayor facilidad.
    * Es muy fácil de convertir en un programa real.
    * Permite identificar claramente los niveles de cada operación si se respetan 
las reglas.

Ejemplo de Pseudocódigo:
Calcular el área de un círculo

PSEINT(Podria ser un lugar para escribir pseudocódigo)
INICIO
Definir PI = 3.14159
LEER radio
area = PI * radio * radio
ESCRIBIR "El área del círculo es: " area
FIN

El pseudocódigo permite pensar la solución, ordenarla, y luego convertirla 
fácilmente en código real.

_______________________________________________________

Codificación:
Escribir la solución del problema en un lenguaje mediante un diagrama de flujo 
o pseudocódigo. El resultado se escribe en un lenguaje de programación de alto 
nivel. Codificar es transformar el algoritmo en código.

Compilación y Ejecución. Una vez escrito el código fuente:
    * Debe ser traducido a lenguaje máquina.
    * Esta traducción se realiza mediante la compilación, dependiendo del 
    lenguaje utilizado.
    * Si durante la compilación no hay errores, el programa puede ejecutarse. 
    Si existen errores, es necesario corregirlos antes de continuar.

Verificación y Depuración: 
Los errores en programación son comunes y aumentan con la complejidad 
del problema:
    * Depuración: proceso de identificar y eliminar errores del programa.
    * Incluye tanto errores: 
        - Sintácticos (mal escritos).
        - Lógicos (el programa funciona, pero da resultados incorrectos).
        - La depuración es una etapa tan importante y creativa como el 
        desarrollo del algoritmo.
El éxito del programa depende en gran parte de una buena depuración.

Mantenimiento:
Un programa no es algo estático, sino un producto vivo. 
Durante su ciclo de vida:
    * Se realizan modificaciones.
    * Se aplican mejoras.
    * Se corrigen errores detectados con el uso.
El mantenimiento permite que el programa siga siendo útil con el tiempo.

Documentación:
La documentación es la información escrita que permite entender, usar 
y mantener un programa. Es importante ya que un programa puede ser usado 
o modificado por otros desarrolladores. Facilita futuras correcciones o mejoras.

Tipos de documentación:
    * Documentación Interna:
        - Son comentarios dentro del código fuente.
        - Ayudan a entender qué hace cada parte del programa.
    * Documentación Externa:
        Se presenta en un documento aparte e incluye:
            - Descripción del problema
            - Nombre del autor
            - Algoritmo (diagrama de flujo o pseudocódigo)
            - Diccionario de datos
            - Código fuente
    * Manual del Usuario:
        - Explica paso a paso cómo usar el programa.
        - Está dirigido al usuario final para que obtenga el resultado deseado.
    
Resumen general del proceso:
    1. Definición del problema
    2. Análisis
    3. Diseño del algoritmo
    4. Codificación
    5. Compilación y ejecución
    6. Depuración
    7. Mantenimiento
    8. Documentación

Programar no termina cuando el código funciona, continúa con pruebas, mantenimiento
y documentación.

_______________________________________________________

Lenguaje de programación Python: Python es un lenguaje de programación de alto nivel, 
interpretado, con una sintaxis simple y legible. Creado por Guido van Rossum a 
fines de los años 80 y publicado oficialmente en 1991. Fue diseñado con un objetivo 
claro y fácil de aprender, leer y usar.

Enfoque en el desarrollo y evolución del código abierto de Python:
Una de sus herramientas más importantes para la evolución del lenguaje son las PEP 
(Python Enhancement Proposals). ¿Qué son las PEP? Son documentos que proponen:
    * Cambios en el lenguaje
    * Mejoras en la sintaxis
    * Ajustes en la semántica o gramática
    * Cualquier persona puede proponer una PEP, la cual:
        - Se analiza
        - Se debate públicamente
        - Se acepta o se rechaza

PEPs importantes:
    * 8: Guía de estilo para escribir código Python
    * 20: El Zen de Python (filosofía del lenguaje)
    * 257: Convenciones para documentación
    * 484: Tipado estático en Python
    * 3107: Convenciones de nombres

Usos actuales de Python:
    - Análisis de datos
    - Machine Learning 
    - Inteligencia Artificial
    - Desarrollo web
    - DevOps
    - Automatización de tareas

Características principales de Python:
    * Sintaxis simple: código claro, fácil de leer y escribir.
    * Lenguaje interpretado: se ejecuta línea por línea, sin compilación previa.
    * Tipado dinámico: no es necesario declarar el tipo de las variables.
    * Fuertemente tipado: no permite operar variables de distintos tipos sin 
    conversión explícita.
    * Librerías extensivas: gran cantidad de módulos y frameworks.
    * Orientado a objetos: soporta POO, pero también programación procedural 
    y funcional.
    * Modularidad: permite organizar el código en módulos reutilizables.
    * Extensibilidad: se pueden crear módulos propios.
    * Multiplataforma: funciona en Windows, macOS y Linux.

Zen de Python: es un conjunto de principios que reflejan la filosofía del lenguaje.
Escrito por Tim Peters. Principios promueven ideas como:
    * Claridad
    * Simplicidad
    * Legibilidad
    * Buen diseño
"""