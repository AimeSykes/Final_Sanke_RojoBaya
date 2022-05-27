import pymysql
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def iniciarDB():
    conexion = pymysql.connect(             
        host="localhost",
        user="user_pyapps",             
        password="swcfbmthtaa8",
        database="snake",             
        charset='utf8mb4',
        port=3306)         
    if conexion:             
        print("CONEXIÓN REALIZADA")
    return conexion

def imprimePDF():
    conexion=iniciarDB()
    MiCursor=conexion.cursor()
    c = canvas.Canvas("SNAKE_SCORE.pdf", pagesize=letter)
    MiCursor.execute("select * from score;")
    lista = MiCursor.fetchall()
    if lista:    
    	c.line(40, 720, 572, 720)
    	a = 720
    	for i in range(-1, len(lista), 1):
    		if i==-1:
    			b = a
    			a = a - 20
    			c.line(40, a, 572, a)  # linea inferior
    			c.line(40, b, 40, a)  # primer linea vertical
    			c.drawCentredString(93, a + 5, "id")
    			c.line(146, b, 146, a)  #Primer campo
    			c.drawCentredString(219.125, a + 5, "score")
    			c.line(292.25, b, 292.25, a)  #Primer campo
    			c.drawCentredString(365.375, a + 5, "Registrado")
    			c.line(438.5, b, 438.5, a) ##segndo campo
    			c.drawCentredString(505.25, a + 5, "High Score")
    			c.line(572, b, 572, a)
    		else:
    			b = a
    			a = a - 20
    			c.line(40, a, 572, a)  # linea inferior
    			c.line(40, b, 40, a)  # primer linea vertical
    			c.drawCentredString(93, a + 5, str(lista[i][0]))
    			c.line(146, b, 146, a)  #Primer campo
    			c.drawCentredString(219.125, a + 5, str(lista[i][1]))
    			c.line(292.25, b, 292.25, a)  #Primer campo
    			c.drawCentredString(365.375, a + 5, str(lista[i][2]))
    			c.line(438.5, b, 438.5, a) ##segndo campo
    			c.drawCentredString(505.25, a + 5, str(lista[i][3]))
    			c.line(572, b, 572, a)
    else:
    	c.line(40, 660, 572, 660)
    	c.drawCentredString(306, 661, "NO SE HAN ENCONTRADO REGISTROS DE RESULTADOS")
    c.showPage()
    c.save()
    
imprimePDF()
