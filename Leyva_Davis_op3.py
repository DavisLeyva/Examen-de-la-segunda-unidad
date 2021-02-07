from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ObjectProperty, ListProperty
from kivy.uix.button import Button
from Agregar import insert_inventario
import serial
from serial.tools import list_ports
import threading
import time

class SerialhWindow(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)   
        puertos = list_ports.comports()
        for nom, _, _ in puertos:
            self.ids.lista.add_widget(Test(puerto=nom))

class Principal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.contador=1

    lectura = StringProperty('')
    lectura1 = StringProperty('')

        
    def enviar_datos_a_BD(self):

        self.contador+=1
        try:
            if float(self.ids.pantalla1.text)<=41:
                insert_inventario(self.contador,self.ids.nombrepaciente.text,
                                self.ids.apellidopaciente.text,
                                self.ids.dnipaciente.text,
                                self.ids.edadpaciente.text,
                                self.ids.pantalla1.text,
                                self.ids.pantalla.text)
        except:
            pass
    
    def leer_serial(self):

        while arduino:
            if arduino.inWaiting() > 0:
                val = arduino.readline().decode().strip()
                sep_valores_arduino = val.split("/") #Separar los valores
                valor_temperatura = sep_valores_arduino[1] #Valor del sensor de temperatura
                valor_pulso_cardiaco = sep_valores_arduino[0] #Valor del sensor pulso cardiaco
                self.lectura=valor_pulso_cardiaco
                self.lectura1=valor_temperatura

                try:
                    self.ids.sld1.value = int(self.lectura)
                    self.ids.sld2.value = int(self.lectura1)
                except:
                    pass
            else:
                time.sleep(0.02)  

class Test(BoxLayout):

    puerto = StringProperty('')
    
    def conectar_puerto(self, puerto):
        arduino.port = puerto
        arduino.baudrate = 9600
        arduino.open()
        print(f"Puerto {puerto} conectado")
        threading.Thread(target=App.get_running_app().sm.ids.main.leer_serial,
                        daemon=True).start()
        App.get_running_app().sm.current='main'

class SerialhApp(App):
    sm = ObjectProperty(None)
    def build(self):
        self.sm = SerialhWindow()
        return self.sm

if __name__=='__main__':   
    try:
        arduino = serial.Serial()
    except:
        exit()
    
    SerialhApp().run()
    arduino.close()
    print('Puerto serial cerrado')