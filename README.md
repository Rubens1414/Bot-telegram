# Bot de Telegram - Constelaciones y Recurrencias

Este proyecto es un bot de Telegram creado en Python con el propósito de manejar dos funcionalidades principales:

1. **Bot-Constelaciones**: Explora las constelaciones, muestra gráficas de estrellas y permite visualizar conexiones estelares.
2. **Bot-Recurrente**: Resuelve funciones generadoras y relaciones de recurrencia.

---

## Funcionalidades

### Bot-Constelaciones 🌌

- **/buscar**: Busca y muestra una constelación específica.
- **/Estrellas**: Muestra todas las estrellas disponibles.
- **/TODAS**: Visualiza todas las constelaciones disponibles.

### Bot-Recurrente 🥑

- **/FGO**: Calcula una función generadora.
- **/f_n**: Resuelve una relación de recurrencia dada.
- **/sec**: Genera la función de recurrencia para una secuencia proporcionada.

---

## Requisitos

Asegúrate de tener los siguientes elementos instalados para ejecutar el proyecto:

- **Python 3.9 o superior**
- Librerías de Python:
  ```bash
  pip install matplotlib telebot sympy numpy
  ```

---

## Instalación

Sigue los pasos para configurar y ejecutar el bot:

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu_usuario/BotTelegram.git
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd BotTelegram
   ```

3. Configura tu **token de Telegram** en el archivo `bot.py`:
   ```python
   bot = telebot.TeleBot("TU_TOKEN_AQUI")
   ```

4. Ejecuta el bot:

   ```bash
   python bot.py
   ```

---

## Ejemplo de Uso

### Comandos Principales

1. **/start**: Muestra el menú de bienvenida y las opciones del bot.
2. **/Constelacion**: Activa el modo Bot-Constelaciones.
3. **/Recurrente**: Activa el modo Bot-Recurrente.

---

## Notas del Proyecto

Este proyecto fue desarrollado como un trabajo académico para explorar conceptos avanzados en Python, como:

- Gráficos con Matplotlib.
- Cálculos matemáticos y simbólicos con Sympy.
- Interacción con la API de Telegram usando Telebot.

El proyecto fue utilizado con fines educativos.

---



