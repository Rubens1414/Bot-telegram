# -*- coding: utf-8 -*-
"""Bot

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qxYjjk2VzIG-6IWGR3-MWHhCEPIveSec
"""

#Librerias
import matplotlib
import telebot
from sympy.parsing.sympy_parser import parse_expr
import sympy as sp
from sympy import Poly
import io
import matplotlib.pyplot as plt
import numpy as np
# Permite que matplotlib se ejecute en segundo plano
matplotlib.use('Agg')

# Token del bot
bot = telebot.TeleBot("6148003608:AAFwM91O7NqWUznSlHIFLoEGzMxIa0a7eCA")
# Leer archivo y almacenar datos en una lista (Para cargar las estrellas)
with open("constellations/stars.txt") as f:
    print('entro')
    lines = f.readlines()

# Eliminar saltos de línea y separar elementos de cada línea
lines = [line.strip().split() for line in lines]

for line in lines:
    # Verificar si hay más de 6 elementos en la línea
    if len(line) > 6:
        name = ' '.join(line[6:])
        # Verificar si el nombre contiene el carácter ";"
        if ";" in name:
            name_parts = name.split(';')
            line[6:] = name_parts
        else:
            line[6:] = [name]

# Crear matriz NumPy bidimensional 
num_rows = len(lines)
num_cols = max(len(line) for line in lines)
data_2d = np.empty((num_rows, num_cols), dtype=object)

# Copiar datos de lista de listas a matriz NumPy
for i in range(num_rows):
    for j in range(num_cols):
        if j < len(lines[i]):
            data_2d[i, j] = lines[i][j]
        else:
            data_2d[i, j] = ""


def buscar(constelacion,chat_id):
    try:
        with open("constellations/" +constelacion + ".txt") as f:
            lines = f.readlines()
        # Eliminar saltos de línea y separar elementos de cada línea
        lines = [line.strip().split(',') for line in lines]
        #Diccionario donde guardara las coordenadas para las estrellas que tenga nombres
        star_coords = {}
        for row in data_2d:
            if row[6]:
                if row[7]:
                    star_name = row[7].strip()  # Eliminar espacios en nombre de estrella
                    x = float(row[0])
                    y = float(row[1])
                    star_coords[star_name] = (x, y)
                star_name = row[6].strip()  # Eliminar espacios en nombre de estrella
                x = float(row[0])
                y = float(row[1])
                star_coords[star_name] = (x, y)
        #Guarda las coordenadas de las estrellas sin nombre, agregando un nombre i
        star_coords2 = {}
        counter = 1
        for row in data_2d:
            if row[6]:
                pass
            else:
                if row[7]:
                    star_name = row[7].strip()
                    x = float(row[0])
                    y = float(row[1])
                    star_coords2[star_name] = (x, y)
                else:
                    star_name = f"Estrella {counter}"
                    counter += 1
                    x = float(row[0])
                    y = float(row[1])
                    star_coords2[star_name] = (x, y)

        # Crear un diccionario para almacenar los colores de cada estrella
        star_colors = {}
        for name in star_coords:
            star_colors[name] = np.random.rand(3)
        star_colors2 = {}
        for name in star_coords2:
            star_colors2[name] = np.random.rand(3)
        # Crear un arreglo de todas las coordenadas de las estrellas
        star_points = np.array([star_coords[name] for name in star_coords])
        star_points2 = np.array([star_coords2[name] for name in star_coords2])
        # Crear una figura con fondo negro
        fig = plt.figure(facecolor='black')
        ax = fig.add_subplot(1, 1, 1, facecolor='black')

        # Crear un scatter plot con todas las estrellas
        ax.scatter(star_points[:, 0], star_points[:, 1], s=0.9, marker='*', c=list(star_colors.values()))
        ax.scatter(star_points2[:, 0], star_points2[:, 1], s=0.9, marker='*', c=list(star_colors2.values()))

        for line in lines:
            if line[0] in star_coords and line[1] in star_coords:
                x1, y1 = star_coords[line[0]]
                x2, y2 = star_coords[line[1]]
                ax.plot([x1, x2], [y1, y2], color='orange', alpha=0.5)

            # Ajustar los límites del gráfico
        ax.set_xlim([-1.1, 1.1])
        ax.set_ylim([-1.1, 1.1])

        # Ocultar los ejes
        ax.set_xticks([])
        ax.set_yticks([])

        # Guardar la imagen en un buffer
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)

        # Enviar la imagen al chat
        bot.send_photo(chat_id, buf)
        gif_path = "Images\ketnipz-star.gif"  # Ruta al archivo GIF que deseas enviar
        bot.send_animation(chat_id, open(gif_path, "rb"))
        # Limpiar el buffer y el plot
        buf.truncate(0)
        buf.seek(0)
        plt.clf()
    except FileNotFoundError:
     bot.send_message(chat_id, f"No se encontró la constelación: {constelacion}")

def mostrarEstrellas(chat_id):
  # Crear un diccionario para almacenar las coordenadas de las estrellas
  

  star_coords = {}
  for row in data_2d:
      if row[6]:
          if row[7]:
              star_name = row[7].strip()  # Eliminar espacios en nombre de estrella
              x = float(row[0])
              y = float(row[1])
              star_coords[star_name] = (x, y)
          star_name = row[6].strip()  # Eliminar espacios en nombre de estrella
          x = float(row[0])
          y = float(row[1])
          star_coords[star_name] = (x, y)

  star_coords2 = {}
  counter = 1
  for row in data_2d:
      if row[6]:
        pass
      else:
          if row[7]:
              star_name = row[7].strip()
              x = float(row[0])
              y = float(row[1])
              star_coords2[star_name] = (x, y)
          else:
              star_name = f"Estrella {counter}"
              counter += 1
              x = float(row[0])
              y = float(row[1])
              star_coords2[star_name] = (x, y)

  # Crear un diccionario para almacenar los colores de cada estrella
  star_colors = {}
  for name in star_coords:
      star_colors[name] = np.random.rand(3)
  star_colors2 = {}
  for name in star_coords2:
      star_colors2[name] = np.random.rand(3)
  # Crear un arreglo de todas las coordenadas de las estrellas
  star_points = np.array([star_coords[name] for name in star_coords])
  star_points2 = np.array([star_coords2[name] for name in star_coords2])
  # Crear una figura con fondo negro
  fig = plt.figure(facecolor='black')
  ax = fig.add_subplot(1, 1, 1, facecolor='black')

  # Crear un scatter plot con todas las estrellas
  ax.scatter(star_points[:, 0], star_points[:, 1], s=0.9, marker='*', c=list(star_colors.values()))
  ax.scatter(star_points2[:, 0], star_points2[:, 1], s=0.9, marker='*', c=list(star_colors2.values()))
      # Ajustar los límites del gráfico
  ax.set_xlim([-1.1, 1.1])
  ax.set_ylim([-1.1, 1.1])

  # Ocultar los ejes
  ax.set_xticks([])
  ax.set_yticks([])

 
  # Guardar la imagen en un buffer
  buf = io.BytesIO()
  plt.savefig(buf, format="png")
  buf.seek(0)

  # Enviar la imagen al chat
  bot.send_photo(chat_id, buf)
  gif_path = "Bot_telgram\Images\ketnipz-star.gif"  # Ruta al archivo GIF que deseas enviar
  bot.send_animation(chat_id, open(gif_path, "rb"))
  # Limpiar el buffer y el plot
  buf.truncate(0)
  buf.seek(0)
  plt.clf()

def mostrar_constelaciones(chat_id):
  # Leer archivo y almacenar datos en una lista
  with open('constellations/Cygnet.txt') as f:
      lines = f.readlines()
  with open('constellations/Boyero.txt') as f:
      lines1 = f.readlines()
  with open('constellations/Casiopea.txt') as f:
      lines2 = f.readlines()
  with open('constellations/Cazo.txt') as f:
      lines3 = f.readlines()
  with open('constellations/Geminis.txt') as f:
      lines4 = f.readlines()
  with open('constellations/Hydra.txt') as f:
      lines5 = f.readlines()
  with open('constellations/OsaMayor.txt') as f:
      lines6 = f.readlines()
  with open('constellations/OsaMenor.txt') as f:
      lines7 = f.readlines()

  # Eliminar saltos de línea y separar elementos de cada línea
  lines = [line.strip().split(',') for line in lines]
  lines1 = [line.strip().split(',') for line in lines1]
  lines2 = [line.strip().split(',') for line in lines2]
  lines3 = [line.strip().split(',') for line in lines3]
  lines4 = [line.strip().split(',') for line in lines4]
  lines5 = [line.strip().split(',') for line in lines5]
  lines6 = [line.strip().split(',') for line in lines6]
  lines7=  [line.strip().split(',') for line in lines7]
  star_coords = {}

  for row in data_2d:
      if row[6]:
          if row[7]:
            star_name = row[7].strip()  # utiliza strip() para eliminar los espacios
            x = float(row[0])
            y = float(row[1])
            star_coords[star_name] = (x, y)
          star_name = row[6].strip()  # utiliza strip() para eliminar los espacios
          x = float(row[0])
          y = float(row[1])
          star_coords[star_name] = (x, y)




  star_coords2 = {}
  counter = 1
  for row in data_2d:
      if row[6]:
        pass
      else:
          if row[7]:
              star_name = row[7].strip()
              x = float(row[0])
              y = float(row[1])
              star_coords2[star_name] = (x, y)
          else:
              star_name = f"Estrella {counter}"
              counter += 1
              x = float(row[0])
              y = float(row[1])
              star_coords2[star_name] = (x, y)

  # Crear un diccionario para almacenar los colores de cada estrella
  star_colors = {}
  for name in star_coords:
      star_colors[name] = np.random.rand(3)
  star_colors2 = {}
  for name in star_coords2:
      star_colors2[name] = np.random.rand(3)
  # Crear un arreglo de todas las coordenadas de las estrellas
  star_points = np.array([star_coords[name] for name in star_coords])
  star_points2 = np.array([star_coords2[name] for name in star_coords2])
  # Crear una figura con fondo negro
  fig = plt.figure(facecolor='black')
  ax = fig.add_subplot(1, 1, 1, facecolor='black')

  # Crear un scatter plot con todas las estrellas
  ax.scatter(star_points[:, 0], star_points[:, 1], s=0.9, marker='*', c=list(star_colors.values()))
  ax.scatter(star_points2[:, 0], star_points2[:, 1], s=0.9, marker='*', c=list(star_colors2.values()))

  for line in lines:
      if line[0] in star_coords and line[1] in star_coords:
          x1, y1 = star_coords[line[0]]
          x2, y2 = star_coords[line[1]]
          ax.plot([x1, x2], [y1, y2], color='orange', alpha=0.5)
  for line1 in lines1:
      if line1[0] in star_coords and line1[1] in star_coords:
          x1, y1 = star_coords[line1[0]]
          x2, y2 = star_coords[line1[1]]
          ax.plot([x1, x2], [y1, y2], color='orange', alpha=0.5)
  for line2 in lines2:
      if line2[0] in star_coords and line2[1] in star_coords:
          x1, y1 = star_coords[line2[0]]
          x2, y2 = star_coords[line2[1]]
          ax.plot([x1, x2], [y1, y2], color='orange', alpha=0.5)

  for line3 in lines3:
      if line3[0] in star_coords and line3[1] in star_coords:
          x1, y1 = star_coords[line3[0]]
          x2, y2 = star_coords[line3[1]]
          ax.plot([x1, x2], [y1, y2], color='orange', alpha=0.5)
  for line4 in lines4:
      if line4[0] in star_coords and line4[1] in star_coords:
          x1, y1 = star_coords[line4[0]]
          x2, y2 = star_coords[line4[1]]
          ax.plot([x1, x2], [y1, y2], color='orange', alpha=0.5)

  for line5 in lines5:
      if line5[0] in star_coords and line5[1] in star_coords:
          x1, y1 = star_coords[line5[0]]
          x2, y2 = star_coords[line5[1]]
          ax.plot([x1, x2], [y1, y2], color='orange', alpha=0.5)

  for line6 in lines6:
      if line6[0] in star_coords and line6[1] in star_coords:
          x1, y1 = star_coords[line6[0]]
          x2, y2 = star_coords[line6[1]]
          ax.plot([x1, x2], [y1, y2], color='orange', alpha=0.5)

  for line7 in lines7:
      if line7[0] in star_coords and line7[1] in star_coords:
          x1, y1 = star_coords[line7[0]]
          x2, y2 = star_coords[line7[1]]
          ax.plot([x1, x2], [y1, y2], color='orange', alpha=0.5)

  # Ajustar los límites del gráfico
  ax.set_xlim([-1.1, 1.1])
  ax.set_ylim([-1.1, 1.1])

  # Ocultar los ejes
  ax.set_xticks([])
  ax.set_yticks([])

   # Guardar la imagen en un buffer
  buf = io.BytesIO()
  plt.savefig(buf, format="png")
  buf.seek(0)

    # Enviar la imagen al chat
  bot.send_photo(chat_id, buf)
  gif_path = "Images\ketnipz-star.gif"  # Ruta al archivo GIF que deseas enviar
  bot.send_animation(chat_id, open(gif_path, "rb"))
    # Limpiar el buffer y el plot
  buf.truncate(0)
  buf.seek(0)
  plt.clf()
def send_latex_code(latex_text, chat_id):
    try:
        # Configurar el texto de Látex en la imagen
        plt.text(0.5, 0.5, f"${latex_text}$", fontsize=35, horizontalalignment='center')
        plt.axis("off")

        # Guardar la imagen en un buffer
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)

        # Enviar la imagen al chat
        bot.send_photo(chat_id, buf)

        # Limpiar el buffer y el plot
        buf.truncate(0)
        buf.seek(0)
        plt.clf()
    except Exception as e:
        bot.send_message(chat_id, f"Ha ocurrido un error al enviar la imagen: {e}")
        return


def RRLHCCC_RRLNHCCC(funcion, valores_iniciales, chat_id):
    try:
        n = sp.symbols('n')
        recurrencia_input_con_prefijo = funcion.strip() + "-f(n)"
        f = sp.Function('f')
        recurrencia = eval(recurrencia_input_con_prefijo)
        ecuacion_general = sp.rsolve(recurrencia, f(n))
        sistema_ecuaciones = []
        for k, a_k in zip(range(len(valores_iniciales)), valores_iniciales):
            sistema_ecuaciones.append(ecuacion_general.subs(n, k) - a_k)
        constantes = sp.solve(sistema_ecuaciones)
        solucion_general = ecuacion_general.subs(constantes)
        latex_solucion_general = sp.latex(solucion_general)
        print(latex_solucion_general)
        # latex_code = "\\scalebox{2}{" + latex_solucion_general + "}"
        send_latex_code(latex_solucion_general, chat_id)


    except:
        bot.send_message(chat_id, f"Ha ocurrido un error, estamos trabajando para resolver más posibles casos")
        return


def sucesion(secuencia, chat_id):
    try:
        n = sp.symbols('n')
        # Si la cadena ingresada es un string, se convierte en lista de enteros
        if type(secuencia) != list:
            secuencia = [int(x.strip()) for x in secuencia.split(",")]

        # Se halla los coeficientes de la función recurrente
        coeficientes = sp.sequence(secuencia, (n, 1, len(secuencia))).find_linear_recurrence(len(secuencia))

        cadena = ""
        valor_inicial = ""

        # Se escribe la función recurrente con los coeficientes encontrados
        # y se crea una lista con los valores iniciales
        for i in range(len(coeficientes)):
            if coeficientes[i] != 0:
                if i == 0:
                    cadena = f"{coeficientes[i]}*f(n-{i + 1})"
                    valor_inicial = f"{secuencia[i]}"
                else:
                    if coeficientes[i] < 0:
                        cadena = cadena + f"{coeficientes[i]}*f(n-{i + 1})"
                    else:
                        cadena = cadena + f"+{coeficientes[i]}*f(n-{i + 1})"

                    valor_inicial = valor_inicial + f",{secuencia[i]}"

        bot.send_message(chat_id, f"\nFuncion recurrente: {cadena}\n")

        # Se envían los valores iniciales por mensaje
        bot.send_message(chat_id, f"\nValores iniciales: {valor_inicial}\n")
        valor_inicial = [int(val.strip()) for val in valor_inicial.split(",")]

        RRLHCCC_RRLNHCCC(cadena, valor_inicial, chat_id)
    except Exception:
        bot.send_message(chat_id,
                         "\nHa ocurrido un error, verifica que si estes escribiendo la sucesion correctamente\n Ejemplo: 1,2,3,4,5\n")
        return


def FGO2(orden, expresion, chat_id):
    z = parse_expr('z')
    aux = [1, 0]
    try:
        f = parse_expr(expresion)
        Fz = Poly(f.series(x=z, x0=0, n=orden).removeO())
        fn = Fz.all_coeffs()

        if fn == None or fn == aux:
            bot.send_message(chat_id, "La expresión ingresada no es válida.")
            return
    except Exception as e:
        bot.send_message(chat_id, f"Error: {e}")
        return
    bot.send_message(chat_id, f"La secuencia generada es {fn[::-1]}")
    sucesion(fn[::-1], chat_id)



@bot.message_handler(commands=['start'])
def enviar(message):
    texto_html = '<b>BIENVENIDO, SOY BOT-RECURRENTE o BOT-ESTELAR</b> 🥑' + '\n'
    texto_html += ' ' + '\n'
    texto_html += 'A continuacion aqui te dare mis dos personalidades cual quieres que yo sea?:' + '\n'
    texto_html += ' ' + '\n'
    texto_html += 'Comandos:' + '\n'
    texto_html += ' ' + '\n'
    texto_html += '<b>/Recurrente:</b> Modo recurrente' + '\n'
    texto_html += ' ' + '\n'
    texto_html += '<b>/Constelacion :</b> Modo constelaciones' + '\n'
    texto_html += ' ' + '\n'
    texto_html += '❓<b>/help</b> Instrucciones de como utilizar esta eleccion ' + '\n'
    bot.reply_to(message, texto_html, parse_mode="html")

@bot.message_handler(commands=['recurrente'])
def enviar(message):
    texto_html = '<b>BIENVENIDO, SOY BOT-RECURRENTE</b> 🥑' + '\n'
    texto_html += ' ' + '\n'
    texto_html += 'A continuacion aqui te dare el menu de comandos que puedes hacer ' + '\n'
    texto_html += ' ' + '\n'
    texto_html += 'Comandos:' + '\n'
    texto_html += ' ' + '\n'
    texto_html += '<b>/FGO:</b> De la funcion generadora te doy la Funcion no recurrente' + '\n'
    texto_html += ' ' + '\n'
    texto_html += '<b>/f_n :</b> De la funcion recurrente te doy la Funcion no recurrente' + '\n'
    texto_html += ' ' + '\n'
    texto_html += '<b>/sec:</b> De una secuencia te doy la funcion no recurrente' + '\n'
    texto_html += ' ' + '\n'
    texto_html += '❓<b>/help:</b> Instrucciones de como utilizar constelaciones ' + '\n'
    bot.reply_to(message, texto_html, parse_mode="html")

@bot.message_handler(commands=['Constelacion'])
def enviar(message):
    chat_id = message.chat.id
    texto_html = '<b>BIENVENIDO, SOY BOT-CONSTELACIONES</b>🌌' + '\n'
    texto_html += ' ' + '\n'
    texto_html += 'A continuacion aqui te dare el menu de comandos que puedes hacer ' + '\n'
    texto_html += ' ' + '\n'
    texto_html += 'Comandos:' + '\n'
    texto_html += ' ' + '\n'
    texto_html += '<b>/buscar:</b> Te pedire que me des el nombre de la constelacion que quieres ver' + '\n'
    texto_html += ' ' + '\n'
    texto_html += '<b>/Estrellas:</b> Te dare todas las estrellas que tengo 🌟' + '\n'
    texto_html += ' ' + '\n'
    texto_html += '<b>/TODAS:</b> Te dare TODAS, TOOOODAS las constelaciones que tengo 🌠' + '\n'
    texto_html += ' ' + '\n'
    texto_html += '❓🌟<b>/help:</b> Instrucciones de como utilizar constelaciones' + '\n'
    bot.reply_to(message, texto_html, parse_mode="html")
    gif_path = "Images\ketnipz-star.gif"  # Ruta al archivo GIF que deseas enviar
    bot.send_animation(chat_id, open(gif_path, "rb"))

@bot.message_handler(commands=['Help', 'help'])
def enviar_ayuda(message):
    texto_help_html = 'Tranquilo aqui te dejo las instrucciones de como utilizarme 😊' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += '<b>INSTRUCCIONES BOT-RECURRENTE🥑:</b> ' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += """<b>1️⃣Para FGO: al ingresar el comando /FGO te saldrá el mensaje "Ingresa la FGO", aquí debes escribir un mensaje con tu F(z)teniendo en cuenta que:</b>""" + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += '       💠Si es fracción: ()/() por ejemplo: (1)/(1-z)**2' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += '       💠Si es polinomio, por ejemplo: 1+z+z**2' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += ' ⚠️Luego te saldrá el mensaje "Ingresa el orden", este es el número de la longitud de la secuencia, ejemplo: 20' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += ' ✅Lo que recibirás será un mensaje con la secuencia generada, la función de recurrencia y la función no recurrente ' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += """<b>2️⃣ Para La Funcion de Recurrencia: al ingresar el comando /f_n te saldrá el mensaje "Ingresa la función de recurrencia:", aquí debes escribir un mensaje con tu f(n) teniendo en cuenta que:</b>""" + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += '       💠Puede ser homogénea o no homogénea ' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += '       😡Solo se resuelven f(n) lineales ' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += '       💠El formato es: 2*f(n-2)-f(n-1)' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += ' ⚠️recibirás un mensaje "Ingresa los valores iniciales separados por comas", por Ejemplo: 1,2' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += ' ✅Lo que recibirás será un mensaje con la secuencia generada y la función no recurrente ' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += """<b>3️⃣Para la secuencia: al ingresar el comando /sec te saldrá el mensaje "Ingresa la secuencia", aquí debes escribir un mensaje con la secuencia de la siguiente manera: 1,2,3,4,5,6,7, 8,9,10 Recomendaciones:</b>""" + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += '       💠Ingresa al menos 10 valores ' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += '       💠Asegúrate de poner las comas para separar los valores' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += ' ✅Lo que recibirás será un mensaje con la función recurrente y la función recurrente ' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += '<b>INSTRUCCIONES BOT-ESTELAR 🌌:</b> ' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += ' /buscar : Te mostrara una lista de la constelaciones que tiene solo tienes que ingresar el nombre tal cual como esta en la lista ' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += ' /Estrellas : Aqui no tienes que hacer nada, yo te mando las entrellas y tu feliz 😊🌟' + '\n'
    texto_help_html += ' ' + '\n'
    texto_help_html += '/TODAS : Aqui tampoco te tienes que preocupar, te dare TOOOOOODAS las constelaciones que tengo 🌌🙌 . ' + '\n'
    bot.reply_to(message, texto_help_html, parse_mode="html")


@bot.message_handler(commands=['f_n'])
def enviar_respuesta_f_n(message):
    chat_id = message.chat.id

    def obtener_recurrencia(m):
        recurrencia = m.text.strip()
        bot.send_message(chat_id, f"Recurrencia ingresada: {recurrencia}")
        bot.send_message(chat_id, "Ingresa los valores iniciales separados por comas:")
        bot.register_next_step_handler(m, obtener_valores_iniciales, recurrencia)

    def obtener_valores_iniciales(m, recurrencia):
        try:
            valores_iniciales = [int(val.strip()) for val in m.text.split(",")]
        except Exception as e:
            bot.send_message(chat_id,
                             f"Ha ocurrido un error recuerda: Ingresa los valores iniciales separados por comas")
            return
        bot.send_message(chat_id, f"Valores iniciales ingresados: {valores_iniciales}")
        print(recurrencia)
        print(valores_iniciales)

        RRLHCCC_RRLNHCCC(recurrencia, valores_iniciales, chat_id)

    bot.send_message(chat_id, "Ingresa la recurrencia:")
    bot.register_next_step_handler(message, obtener_recurrencia)


@bot.message_handler(commands=['sec'])
def enviar_respuesta_sec(message):
    chat_id = message.chat.id

    def obtener_sec(m):
        sec = m.text.strip()
        bot.send_message(chat_id, f"Recurrencia ingresada: {sec}")
        obtener_valores_iniciales(m, sec)

    def obtener_valores_iniciales(m, sec):
        sucesion(sec, chat_id)

    bot.send_message(chat_id, "Ingresa la secuencia:")
    bot.register_next_step_handler(message, obtener_sec)


@bot.message_handler(commands=['FGO'])
def enviar_respuesta_fgo(message):
    chat_id = message.chat.id

    def obtener_orden(m, Fgo):
        orden = m.text.strip()
        bot.send_message(chat_id, f"Orden ingresado: {orden}")
        FGO2(int(orden), Fgo, chat_id)

    def obtener_funcion(m):
        Fgo = m.text.strip()
        bot.send_message(chat_id, f"Función ingresada: {Fgo}")
        bot.send_message(chat_id, "Ingresa el orden n (Ejemplo: 15):")
        bot.register_next_step_handler(m, obtener_orden, Fgo)

    bot.send_message(chat_id, "Ingresa la función generadora:")
    bot.register_next_step_handler(message, obtener_funcion)


@bot.message_handler(commands=['buscar'])
def obtener_nombre(message):
    chat_id = message.chat.id

    def llamar_funcion(m):
        nombre = m.text.strip()
        bot.send_message(chat_id, f"Nombre ingresado: {nombre}")
        buscar(nombre, chat_id)

    texto_html = '<b>Lista de constelaciones: 🥑🌠🌌</b>\n\n'
    texto_html += '<b>Boyero</b>\n'
    texto_html += '<b>Casiopea</b>\n'
    texto_html += '<b>Cazo</b>\n'
    texto_html += '<b>Cygnet</b>\n'
    texto_html += '<b>Geminis</b>\n'
    texto_html += '<b>Hydra</b>\n'
    texto_html += '<b>OsaMayor</b>\n'
    texto_html += '<b>OsaMenor</b>\n'

    bot.send_message(chat_id, texto_html, parse_mode="html")
    bot.send_message(chat_id, "Por favor, ingresa un nombre:")
    bot.register_next_step_handler(message, llamar_funcion)

@bot.message_handler(commands=['Estrellas'])
def mostrar_todas_estrellas(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Aqui estan todas las estrellas")
    mostrarEstrellas(chat_id)

@bot.message_handler(commands=['TODAS'])
def mostrar_todas_estrellas(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Aqui estan TODAS las constelaciones")
    mostrar_constelaciones(chat_id)  

@bot.message_handler(content_types=['text'])
def non_command_handler(message):
    command = message.text
    if command != "/help" or command != "/FGO" or command != "/Help" or command != "/f_n" or command != "/sec":
        bot.send_message(message.chat.id, "❓")
        bot.send_message(message.chat.id,
                         "Lo siento, el comando: ('{}')  no existe, utilice /help para saber que comando utilizar".format(
                             command))
if __name__ == '__main__':
    print('Inicio el bot')
    bot.infinity_polling()
