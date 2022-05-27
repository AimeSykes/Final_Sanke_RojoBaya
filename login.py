from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import os
import sys


class Snake_Baya(App):
        
    def build(self):
        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # image widget
        self.window.add_widget(Image(source="logo.png"))

        # label widget
        self.greeting = Label(
                        text= "Cual es tu nombre ?",
                        font_size= 18,
                        color= '#008F39'
                        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
                    multiline= False,
                    padding_y= (20,20),
                    size_hint= (1, 0.5)
                    )

        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
                      text= "Bienvenida",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#FF0000',
                      #remove darker overlay of background colour
                      # background_normal = ""
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        
        self.button = Button(
                      text= "Iniciar Juego",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#FF0000',)
        self.button.bind(on_press=self.callback2)
        self.window.add_widget(self.button)
        
        self.button = Button(
                      text= "Generar reporte de puntajes.pdf",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#FF0000',)
        self.button.bind(on_press=self.callback4)
        self.window.add_widget(self.button)
        print("reporte generado")
        
        self.button = Button(
                      text= "Salir",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#FF0000',
                      #remove darker overlay of background colour
                      # background_normal = ""
                      )
        self.button.bind(on_press=self.callback3)
        self.window.add_widget(self.button)
        return self.window

    def callback(self, instance):
        # change label text to "Hello + user name!"
        self.greeting.text = "Hola " + self.user.text + "!"
        
    def callback2(self, instance):
        os.system('python snk_p.py')
    
    def callback3(self, instance):
        sys.exit()
        
    def callback4(self, instance):
        os.system('python puntajes.py')

# run Say Hello App Calss
if __name__ == "__main__":
    Snake_Baya().run()
