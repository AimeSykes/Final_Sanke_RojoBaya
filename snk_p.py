import turtle
import time 
import random
import pymysql

conexion = pymysql.connect(             
    host="localhost",
    user="user_pyapps",             
    password="swcfbmthtaa8",
    database="snake",             
    charset='utf8mb4',
    port=3306)         
if conexion:             
    print("conexion realizada")
    MiCursor=conexion.cursor()
    
posponer = 0.1

#Marcador
score = 0
high_score = 0


#Configuracion de la ventana
ventana = turtle.Screen()
ventana.title('Snake Baya')
ventana.bgcolor('black')
ventana.setup(600, 600)
ventana.tracer()

#cabeza de serpiente

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape('square')
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = 'stop'
cabeza.color('white')

#comida

comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.penup()
comida.goto(0,100)
comida.color('red')

#cuerpo serpiente
segmentos = []

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color('white')
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0          High Score: 0", align= "center", font = ("Courier", 24, "normal")) 




#Funciones

def arriba():
    cabeza.direction = 'up'

def abajo():
    cabeza.direction = 'down'

def izquierda():
    cabeza.direction = 'left'

def derecha():
    cabeza.direction = 'right'




def mov():
    if cabeza.direction == 'up':
        y = cabeza.ycor()
        cabeza.sety(y + 20)


    if cabeza.direction == 'down':
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == 'left':
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == 'right':
        x = cabeza.xcor()
        cabeza.setx(x + 20)
        
#teclado

ventana.listen()
ventana.onkeypress(arriba, 'Up')
ventana.onkeypress(abajo, 'Down')
ventana.onkeypress(izquierda, 'Left')
ventana.onkeypress(derecha, 'Right')



while True:
    ventana.update()

    #Colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        print("perdiste")
        cadena="Insert into score values(NULL, {},now(),{});".format(score, high_score)
        MiCursor.execute(cadena)
        conexion.commit()
        print("datos insertado")
        
        # Borrar segmentos:
        for segment in segmentos:
            segment.goto(1000,1000)
        segmentos.clear()
        
        #Resetear marcador
        score = 0
        texto.clear()
        texto.write("Score: {}          High Score: {}".format(score, high_score), 
                    align= "center", font = ("Courier", 24, "normal"))

            


    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)
       # nuevos segmentos  
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape('square')
        nuevo_segmento.color('grey')
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
        
        #Aumentar  marcador
        score += 10
        
        if score > high_score:
            high_score = score
            
        texto.clear()
        texto.write("Score: {}     High Score: {}".format(score, high_score), 
                    align= "center", font = ("Courier", 24, "normal"))

#mover el cuerpo de la serpiente

    totalSeg = len(segmentos)
    for index in range(totalSeg -1,0,-1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
        

    mov()
    time.sleep(posponer)
