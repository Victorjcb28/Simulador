#! /usr/bin/env python
# -*- coding:CP1252 -*-


import wx

import winsound
global posinicial
global vel
global coeficiente
global tiempo
from visual import*
from visual.controls import *
from visual.graph import *
import math
import pygame





#Funciones que Ejecutan la Simulacion--------------------------------------------------------------------------------------------

def Ingresar(frm):
    """ La funcion Ingresar le pide al usuario que ingrese la altura y le indica cuando no es un dato valido el que ingreso.
    No necesita nngun argumento de entrada.Lo que regresa es la altura que el usuario indico"""
    #se asigna el valor de la variable seguir
    
    #se le pide al usuario que ingresa la altura
    posinicial=float(frm.txtposinicial.GetValue())
    #posinicial=raw_input("Ingrese la altura desde donde se va dejar caer (en metros): ")
   #se condiona para que solo permite ingresar numero positivos 
    
    posinicial=float(posinicial)
    if posinicial>0:
        posinicial=posinicial+2
        return posinicial
    
            

def vf(gravedad, tiempo):
    """ La funci?n vf realiza una operaci?n matematica para encontrar la velocidad final de un cuerpo en caida libre.
    Necesita de argumentos la gravedad y el tiempo. Lo que regresa es la velocidad final"""
    #se realiza un multiplicacion y el valor se le asigna a la variable vf
    vf=gravedad*tiempo
    #se regresa vf
    return vf

def IngVelocidad(frm):
    """ La funci?n le pregunta al usuario la velocida inicial. Lo indica al usuario cuando el dato es erroneo
    Regresa la velocidad que ingreso el usuario convertida a variable tipo float"""
    #se le pide al usuario que ingrese la velocidad inicial
    vel=float(frm.txtvel.GetValue())
    #vel=raw_input("Ingrese la velocidad inicial (m/s): ")
    #se asigna el valor de error
    
    #se condione para que solo se pueden ingresar valores numericos positvios
    
    vel=float(vel)
            #se condiona que sea positivo
    if vel>0:
                #se regresa el valor de vel
        return vel
            

def desplazamientox(tiempo,velocidad):
    """La funci?n realiza una multiplicaci?n para encontrat el desplazamiento horizontal de un objeto
    La funci?n pide como argumentos el tiempo y la velocidad. Regresa el desplazamiento horizontal."""
    #se realiza un operacion para encontrar el el desplzamiento horizaontal
    x=tiempo*velocidad
    #se regresa el valor de x
    return x


def angulo(frm):
    """ La funci?n le pregunta al usuario el angulo. Lo indica al usuario cuando el dato es erroneo (no se encuentra en el rango o no es dato numerico)
    Regresa el angulo que ingreso el usuario convertida a variable tipo float"""
    #se le pide al usuario el angulo
    angulo=int(frm.txtAngulo.GetValue())
    #angulo=raw_input("Ingrese la inclinacion (angulo entre 0 y 90 grados): ")
    #se asigna el valor de error
    
    #se condiona para que solo sea un dato numerico y que este dentro del rango de 0 y 90 grados
    
            #se intenta convertir 
    angulo=int(angulo)
            #se condiona para que solo sea un angulo entre 0 y 90
    if angulo>0 and angulo<91:
                #se regresa el valor de angulo
        return angulo
            

def velocidad(frm):
    """ La funci?n velocidad regresa la velocidad inicial como una variable tipo float.
    Pide de argumento el el dato a revisar y convertir. Regresa el valor como un float"""
    x=int(frm.txtvel.GetValue())
    while type(x)!=float:
        try:
            x=float(x)

            if type(x)==float:
                return x

            else:
                pass

        except:
            print "Ingrese un valor v?lido para la fuerza"
            print
            x=raw_input("?Cu?l es la velocidad inicial del objeto? (m/s): ")


def gravedad(frm):
    """ La funci?n gravedad regresa la gravedad como una variable tipo float.
    Pide de argumento el el dato a revisar y convertir. Regresa el valor como un float"""
    x=int(frm.txtGrav.GetValue())
    while type(x)!=float:
        try:
            x=float(x)

            if type(x)==float:
                return -x

            else:
                pass

        except:
            print "Ingrese un valor valido para la gravedad"
            print
            x=raw_input("?Cu?l es la aceleracion de la gravedad?: m/s")

def alturamax(gravedad, veli):
    """ La funci?n realiza una operaci?n para enocontrar la altura maxima de un objeto.
    La funci?n pide como objeto la gravedad y la velocidad inicial. Regresa la altura maxima"""
    #se realiza varias operacione para encontrar la altura maxima   
    maxima=(veli/2)*(veli/gravedad)
    #se regresa el valor de maxima
    return maxima


def pelota(frm):
    pygame.init()
    pygame.mixer.music.load("2.wav")
    
    
    posinicial=Ingresar(frm)
    
    gravedad=9.8

    
    altura=posinicial
    
    
    tamano=posinicial
    
    
    
    scene = display(title="Simulador de Caida Libre", width=500, height=500, x=0, y=0,center=(0,200/2,100), range=(200, 200, 200),autocenter=1)   
    pelota=sphere(pos=(0,tamano,0),radius=tamano/50, color=color.blue)
    
    
    piso=box(pos=(0,-1,0),size=(200,2,200), color=color.white)
    
    Drops = []
    edificio=box(size=((200/4),200,(200/4)), pos=(-(200/4),(200/2),0), color=color.red)
    
    rect1=box(size=((50/4),10,(50/4)), pos=(-(250/4),(345/2),(50/2)), color=color.yellow)
    rect11=box(size=((50/4),10,(50/4)), pos=(-(150/4),(345/2),(50/2)), color=color.yellow)
    rect2=box(size=((50/4),10,(50/4)), pos=(-(250/4),(300/2),(50/2)), color=color.yellow)
    rect21=box(size=((50/4),10,(50/4)), pos=(-(150/4),(300/2),(50/2)), color=color.yellow)
    rect3=box(size=((50/4),10,(50/4)), pos=(-(250/4),(255/2),(50/2)), color=color.yellow)
    rect31=box(size=((50/4),10,(50/4)), pos=(-(150/4),(255/2),(50/2)), color=color.yellow)
    rect4=box(size=((50/4),10,(50/4)), pos=(-(250/4),(210/2),(50/2)), color=color.yellow)
    rect41=box(size=((50/4),10,(50/4)), pos=(-(150/4),(210/2),(50/2)), color=color.yellow)
    rect3=box(size=((50/4),10,(50/4)), pos=(-(250/4),(165/2),(50/2)), color=color.yellow)
    rect31=box(size=((50/4),10,(50/4)), pos=(-(150/4),(165/2),(50/2)), color=color.yellow)
    rect3=box(size=((50/4),10,(50/4)), pos=(-(250/4),(120/2),(50/2)), color=color.yellow)
    rect31=box(size=((50/4),10,(50/4)), pos=(-(150/4),(120/2),(50/2)), color=color.yellow)
    rect4=box(size=((50/4),10,(50/4)), pos=(-(250/4),(75/2),(50/2)), color=color.yellow)
    rect41=box(size=((50/4),10,(50/4)), pos=(-(150/4),(75/2),(50/2)), color=color.yellow)         
   
    
    
    
#se asigna el valor de las variables necesarias en el proceso
    segundos=0
    dt=0.01
    fin=False
    fon=False
    fan=False
    scene.visible=True
    #se coloca un label con la informacion de donde en que posicion se encuentra la pelota
    
    tiempo=label(pos=(0,posinicial,0), text=str(posinicial-pelota.radius))
    pygame.mixer.music.play(1)
## prueba
    
    
#se condiona para que la pelota continue en caida hasta que este en la posicion 0

        
        
    while not fin:
        
        while not fon:
              
                
              #se coloca las veces que se va a repetir el proceso en un 1 segundo
            rate(100)
	
            #se vuelve invisible el label
        #tiempo1.visible=False
            tiempo.visible=False
            #se elimina el label
        #del tiempo1
            del tiempo
            #se suma los segundos
            segundos+=dt
            #se crea la formula para crear la caida libre
            altura=posinicial-(0.5*gravedad*(segundos)**2)
        
            #se le indica la nueva posicion de la pelota
            pelota.pos=vector(0,altura,0)
        
                #se muestra una label con la altura en que se encuentra la pelota
            tiempo=label(pos=(-50,posinicial/2,0), text="Altura: "+str(altura-pelota.radius)+" m")
          

            
            if altura-(posinicial/50)<=0: #termina la caida
                pygame.mixer.music.stop()
                tiempo.visible=False
                del tiempo
                #del tiempo1
                fin=True
                winsound.PlaySound("1.wav", winsound.SND_FILENAME)
                #Mostrar Mensaje
                etiqueta=label(pos=(200/3,200,100), text="Tiempo: " + str(segundos)+ " s")
                vf1=vf(gravedad, segundos)
    
                etiqueta1=label(pos=(200/2,100,0),text="Velocidad al momento del impacto: "+str(vf1)+ " m/s")
    
                dlg = wx.MessageDialog(None, 'Presione OK para salir de la Simulacion','Diálogo de Mensage', wx.OK|wx.ICON_QUESTION)
        
        

                if dlg.ShowModal()==wx.ID_OK:
                    scene.visible=False
                dlg.Destroy()   
        
        #pelota2.pos=vector(10,0,0)
            if scene.mouse.clicked : #con esta funciona se da click
                pygame.mixer.music.stop()
                fon=True
                m = scene.mouse.getclick()
                loc = m.pos
                vf2=vf(gravedad, segundos)
                lo=label(pos=loc, text="Altura: "+str(altura-pelota.radius)+" m\nVelocidad:"+str(vf2)+ " m/s\nTiempo:"+str(segundos)+"s") 
                
        if scene.kb.keys : #con esta funciona se da click (Teclado)
            pygame.mixer.music.play(1)
            while not fin:
                   #se coloca las veces que se va a repetir el proceso en un 1 segundo
                rate(100)
	
            #se vuelve invisible el label
        #tiempo1.visible=False
                tiempo.visible=False
            #se elimina el label
        #del tiempo1
                del tiempo
            #se suma los segundos
                segundos+=dt
            #se crea la formula para crear la caida libre
                altura=posinicial-(0.5*gravedad*(segundos)**2)
        #altura2=posinicial2-(0.5*gravedad*(segundos)**2)
            #se le indica la nueva posicion de la pelota
                pelota.pos=vector(0,altura,0)
        #pelota2.pos=vector(10,altura2,0)
                #se muestra una label con la altura en que se encuentra la pelota
                tiempo=label(pos=(-50,posinicial/2,0), text="Altura: "+str(altura-pelota.radius)+" m")
        #tiempo=label(pos=(100,50,0), text="Altura: "+str(altura2-pelota2.radius)+" m")  

                if altura-(posinicial/50)<=0: #termina la caida
                    pygame.mixer.music.stop()
                    tiempo.visible=False
                    del tiempo
                    fan=True
                    fin=True
                    winsound.PlaySound("1.wav", winsound.SND_FILENAME)

        
            
            
#se muestra etiquetas con la cantidad desegundos que se tardo y la velocidad al momento del impacto    
    lo.visible=False# Volver el label del "CLICK" invisible
    etiqueta=label(pos=(200/3,200,100), text="Tiempo: " + str(segundos)+ " m/s")
    vf1=vf(gravedad, segundos)
    
    etiqueta1=label(pos=(200/2,100,0),text="Velocidad al momento del impacto: "+str(vf1)+ " m/s")
    
    dlg = wx.MessageDialog(None, 'Presione OK para salir de la Simulacion','Diálogo de Mensage', wx.OK|wx.ICON_QUESTION)
        
        

    if dlg.ShowModal()==wx.ID_OK:
        scene.visible=False
    dlg.Destroy()   
    
def pelotaEner(frm):
    
    #pygame.init()
    #pygame.mixer.music.load("2.wav")
    
    posinicial=Ingresar(frm)
    
    gravedad=9.8


    altura=posinicial
    
    tamano=posinicial
    m=float(frm.txtmasa.GetValue())
    scene = display(title="Simulador de Caida Libre", width=500, height=500, x=0, y=0,center=(0,200/2,100), range=(200, 200, 200),autocenter=1)   
    pelota=sphere(pos=(0,tamano,0),radius=tamano/50, color=color.blue)
    
    
    piso=box(pos=(0,-1,0),size=(200,2,200), color=color.white)
    
    
    edificio=box(size=((200/4),200,(200/4)), pos=(-(200/4),(200/2),0), color=color.red)
    rect1=box(size=((50/4),10,(50/4)), pos=(-(250/4),(345/2),(50/2)), color=color.yellow)
    rect11=box(size=((50/4),10,(50/4)), pos=(-(150/4),(345/2),(50/2)), color=color.yellow)
    rect2=box(size=((50/4),10,(50/4)), pos=(-(250/4),(300/2),(50/2)), color=color.yellow)
    rect21=box(size=((50/4),10,(50/4)), pos=(-(150/4),(300/2),(50/2)), color=color.yellow)
    rect3=box(size=((50/4),10,(50/4)), pos=(-(250/4),(255/2),(50/2)), color=color.yellow)
    rect31=box(size=((50/4),10,(50/4)), pos=(-(150/4),(255/2),(50/2)), color=color.yellow)
    rect4=box(size=((50/4),10,(50/4)), pos=(-(250/4),(210/2),(50/2)), color=color.yellow)
    rect41=box(size=((50/4),10,(50/4)), pos=(-(150/4),(210/2),(50/2)), color=color.yellow)
    rect3=box(size=((50/4),10,(50/4)), pos=(-(250/4),(165/2),(50/2)), color=color.yellow)
    rect31=box(size=((50/4),10,(50/4)), pos=(-(150/4),(165/2),(50/2)), color=color.yellow)
    rect3=box(size=((50/4),10,(50/4)), pos=(-(250/4),(120/2),(50/2)), color=color.yellow)
    rect31=box(size=((50/4),10,(50/4)), pos=(-(150/4),(120/2),(50/2)), color=color.yellow)
    rect4=box(size=((50/4),10,(50/4)), pos=(-(250/4),(75/2),(50/2)), color=color.yellow)
    rect41=box(size=((50/4),10,(50/4)), pos=(-(150/4),(75/2),(50/2)), color=color.yellow)         
   
    
    
    
#se asigna el valor de las variables necesarias en el proceso
    segundos=0
    dt=0.01
    fin=False
    fon=False
    scene.visible=True
    
#se coloca un label con la informacion de donde en que posicion se encuentra la pelota
    tiempo=label(pos=(0,posinicial,0), text=str(posinicial-pelota.radius))

## prueba
    
    #pygame.mixer.music.play(1)
#se condiona para que la pelota continue en caida hasta que este en la posicion 0
   
    while not fin:
        
        while not fon:
            
        
              #se coloca las veces que se va a repetir el proceso en un 1 segundo
            rate(100)
	
            #se vuelve invisible el label
            tiempo.visible=False
            #se elimina el label
            del tiempo
            #se suma los segundos
            segundos+=dt
            #se crea la formula para crear la caida libre
            altura=posinicial-(0.5*gravedad*(segundos)**2)
            #se le indica la nueva posicion de la pelota
            pelota.pos=vector(0,altura,0)
                #se muestra una label con la altura en que se encuentra la pelota
            tiempo=label(pos=(posinicial/3,posinicial/2,0), text="Altura: "+str(altura-pelota.radius)+" m")
                
            if altura-(posinicial/50)<=0:
            #pygame.mixer.music.stop()
            
                tiempo.visible=False
                del tiempo
                fin=True
                winsound.PlaySound("1.wav", winsound.SND_FILENAME)
                etiqueta=label(pos=(200/3,200,100), text="Tiempo: " + str(segundos)+ " m/s")
                vf1=vf(gravedad, segundos)
                Ener=0.5*(m*vf1**2) #Calcular energia con la velocidad final
                etiqueta1=label(pos=(200/2,100,0),text="Velocidad al momento del impacto: "+str(vf1)+ " m/s")
                etiqueta2=label(pos=(200/2,130,20),text="Energia:"+str(Ener))
    
                dlg = wx.MessageDialog(None, 'Presione OK para salir de la Simulacion','Diálogo de Mensage', wx.OK|wx.ICON_QUESTION)
        
        

                if dlg.ShowModal()==wx.ID_OK:
                    scene.visible=False
                dlg.Destroy()   
       
	#calcular velocidad dependiendo de la altura que quiera el usuario
        
            if scene.mouse.clicked : #con esta funciona se da click
                fon=True
                mo = scene.mouse.getclick()
                loc = mo.pos
                vf2=vf(gravedad, segundos)
            
                lo=label(pos=loc, text="Altura: "+str(altura-pelota.radius)+" m\nVelocidad:"+str(vf2)+ " m/s\nEnergia:"+str(0.5*(m*vf2**2)))
        if scene.kb.keys : #con esta funciona se da click (Teclado)
            while not fin:
                #se coloca las veces que se va a repetir el proceso en un 1 segundo
                rate(100)
	
            #se vuelve invisible el label
                tiempo.visible=False
            #se elimina el label
                del tiempo
            #se suma los segundos
                segundos+=dt
            #se crea la formula para crear la caida libre
                altura=posinicial-(0.5*gravedad*(segundos)**2)
            #se le indica la nueva posicion de la pelota
                pelota.pos=vector(0,altura,0)
                #se muestra una label con la altura en que se encuentra la pelota
                tiempo=label(pos=(posinicial/3,posinicial/2,0), text="Altura: "+str(altura-pelota.radius)+" m")


                
        #se condiona para cuando este sobre el suelo deje de caer
                if altura-(posinicial/50)<=0:
            #pygame.mixer.music.stop()
            
                    tiempo.visible=False
                    del tiempo
                    fin=True
                    winsound.PlaySound("1.wav", winsound.SND_FILENAME)
            
            

#se muestra etiquetas con la cantidad desegundos que se tardo y la velocidad al momento del impacto
                    lo.visible=False #label no visible
                    etiqueta=label(pos=(200/3,200,100), text="Tiempo: " + str(segundos)+ " m/s")
                    vf1=vf(gravedad, segundos)
                    Ener=0.5*(m*vf1**2) #Calcular energia con la velocidad final
                    etiqueta1=label(pos=(200/2,100,0),text="Velocidad al momento del impacto: "+str(vf1)+ " m/s")
                    etiqueta2=label(pos=(200/2,130,20),text="Energia:"+str(Ener))
    
                    dlg = wx.MessageDialog(None, 'Presione OK para salir de la Simulacion','Diálogo de Mensage', wx.OK|wx.ICON_QUESTION)
        
        

                    if dlg.ShowModal()==wx.ID_OK:
                        scene.visible=False
                    dlg.Destroy()   
       
 

   
       
def horizontal(frm):
    pygame.init()
    pygame.mixer.music.load("2.wav")
    posinicial=int(frm.txtposinicial.GetValue())
    
    altura= posinicial
    velocidad=IngVelocidad(frm)
    scene = display(title="Simulador de Proyeccion Horizontal", width=500, height=500, x=0, y=0,center=(0,200/2,100), range=(200*2, 200*2, 200*2),autocenter=1)
    pelota1=sphere(pos=(0,posinicial/20,0),radius=posinicial/50, color=color.blue)
    
    piso=box(pos=(0,-1,0),size=(200*2,2,200*2), color=color.white)
    edificio=box(size=((200/4),200,(200/4)), pos=(-(200/4),(200/2),0), color=color.red)
    edificio=box(size=((200/4),200,(200/4)), pos=(-(200/4),(200/2),0), color=color.red)
    rect1=box(size=((50/4),10,(50/4)), pos=(-(250/4),(345/2),(50/2)), color=color.yellow)
    rect11=box(size=((50/4),10,(50/4)), pos=(-(150/4),(345/2),(50/2)), color=color.yellow)
    rect2=box(size=((50/4),10,(50/4)), pos=(-(250/4),(300/2),(50/2)), color=color.yellow)
    rect21=box(size=((50/4),10,(50/4)), pos=(-(150/4),(300/2),(50/2)), color=color.yellow)
    rect3=box(size=((50/4),10,(50/4)), pos=(-(250/4),(255/2),(50/2)), color=color.yellow)
    rect31=box(size=((50/4),10,(50/4)), pos=(-(150/4),(255/2),(50/2)), color=color.yellow)
    rect4=box(size=((50/4),10,(50/4)), pos=(-(250/4),(210/2),(50/2)), color=color.yellow)
    rect41=box(size=((50/4),10,(50/4)), pos=(-(150/4),(210/2),(50/2)), color=color.yellow)
    rect3=box(size=((50/4),10,(50/4)), pos=(-(250/4),(165/2),(50/2)), color=color.yellow)
    rect31=box(size=((50/4),10,(50/4)), pos=(-(150/4),(165/2),(50/2)), color=color.yellow)
    rect3=box(size=((50/4),10,(50/4)), pos=(-(250/4),(120/2),(50/2)), color=color.yellow)
    rect31=box(size=((50/4),10,(50/4)), pos=(-(150/4),(120/2),(50/2)), color=color.yellow)
    rect4=box(size=((50/4),10,(50/4)), pos=(-(250/4),(75/2),(50/2)), color=color.yellow)
    rect41=box(size=((50/4),10,(50/4)), pos=(-(150/4),(75/2),(50/2)), color=color.yellow)         
   



#se asignan el valor de las variables
    gravedad=9.8
    segundos=0
    dt=0.01
    fin=False
    fon=False

#se muestra la posici?n de la pelota
    tiempo=label(pos=(0,posinicial,0), text=str(posinicial-pelota1.radius))
    #tiempo1=label(pos=(0,posinicial,0), text=str(posinicial-pelota1.radius))
    pygame.mixer.music.play(1)
#se condiona para que se repita el proceso 
    while not fin:
        while not fon:

#se le indica cuantas veces realizar el proceso
            rate(100)
        #se le indica que la label llamada tiempo sea invisible para luego eliminarla
            tiempo.visible=False
            #se elimina el label llamado tiempo
            del tiempo
            #se suman los segundos que pasan
            segundos+=dt
            #se le indica que altura es la formula de movimiento en el eje y
            altura=posinicial-(0.5*gravedad*(segundos)**2)
            #se le indiac que avance es la formula de movimiento en el eje x
            avance=velocidad*segundos
            #se le indica la posicion de la pelota
            pelota1.pos=vector(avance,altura,0)
            #se muestra un label con la altuta de la pelota
            tiempo=label(pos=(200/3,200/2,0), text="Altura: "+str(altura-pelota1.radius)+" m")

            if scene.mouse.clicked : #con esta funciona se da click
                pygame.mixer.music.stop()
                mo = scene.mouse.getclick()
                loc = mo.pos
                vf2=vf(gravedad, segundos)
                dh1=desplazamientox(segundos, velocidad)
                fon=True
                lo=label(pos=loc, text="Altura: "+str(altura-pelota1.radius)+" m\nVelocidad:"+str(vf2)+ " m/s\nDistancia:"+ str(dh1) +"m")
            if altura-(posinicial/50)<=0:
                pygame.mixer.music.stop()
                tiempo.visible=False
                del tiempo
                fon=True
                fin=True
                winsound.PlaySound("1.wav", winsound.SND_FILENAME)            

        if scene.kb.keys : #con esta funciona se da click (Teclado)
            pygame.mixer.music.play(1)
            while not fin:
                rate(100)
        #se le indica que la label llamada tiempo sea invisible para luego eliminarla
                tiempo.visible=False
            #se elimina el label llamado tiempo
                del tiempo
            #se suman los segundos que pasan
                segundos+=dt
            #se le indica que altura es la formula de movimiento en el eje y
                altura=posinicial-(0.5*gravedad*(segundos)**2)
            #se le indiac que avance es la formula de movimiento en el eje x
                avance=velocidad*segundos
            #se le indica la posicion de la pelota
                pelota1.pos=vector(avance,altura,0)
            #se muestra un label con la altuta de la pelota
                tiempo=label(pos=(200/3,200/2,0), text="Altura: "+str(altura-pelota1.radius)+" m")



            #se condiona que cuando este en la posicion cero deje de moverse
                if altura-(posinicial/50)<=0:
                    pygame.mixer.music.stop()
                    tiempo.visible=False
                    del tiempo
                    fon=True
                    fin=True
                    winsound.PlaySound("1.wav", winsound.SND_FILENAME)
        #se muestra el label con el tiempo que esta en movimiento        
    etiqueta=label(pos=(200/3,200,0), text="Tiempo: " + str(segundos)+ " seg")
        #se invoca la funcion vf
    vf1=vf(gravedad, segundos)
        #se muestra el label con la velocida al momento del impacto
    etiqueta1=label(pos=(200,100,0),text="Velocidad al momento del impacto: "+str(vf1)+ " m/s")
        #se invoca la funcion desplazamiento
    dh=desplazamientox(segundos, velocidad)
        #se muestra el label con el desplzamiento horizontal
    etiqueta2=label(pos=(-posinicial,-altura*3,0),text="Desplazamiento horizontal: " + str(dh) + " m")
    dlg = wx.MessageDialog(None, 'Presione OK para salir de la Simulacion','Diálogo de Mensage', wx.OK|wx.ICON_QUESTION)
        
        

    if dlg.ShowModal()==wx.ID_OK:
        scene.visible=False
    dlg.Destroy()

def parabola1(frm):
    velocidad=IngVelocidad(frm)
    posinicial=velocidad*4
    angulo1=angulo(frm)
    tamano=200
    scene = display(title="Simulador de Tiro Parabolico 1", width=500, height=500, x=0, y=0,center=(tamano/4,tamano/2,tamano*3), range=(tamano, tamano, tamano))
    pelota1=sphere(pos=(-tamano/4,tamano+(tamano/50),0),radius=tamano/50, color=color.blue)
    piso=box(pos=(3*(tamano/2),-1,0),size=(tamano*3,2,tamano*3), color=color.white)

        #se asigna el valor de las varibales
    gravedad=9.8
    segundos=0
    dt=0.01
    t=0
        #se convierte los angulos de grados a radianes
    angulo1=angulo1*(pi/180)

        #se asigna el valor de las velocidades en los dos ejes por medio de la formulas
    velocidady=velocidad*sin(angulo1)
    velocidadx=velocidad*cos(angulo1)
    tempo=2*(-velocidady/gravedad)
    
        #se condiona para que se repita hasta que este en la posicion 0
    fin=False
    tiempo=label(pos=(0,posinicial,0), text=str(posinicial-pelota1.radius))
    while not fin:
        
            #se indica las veces que se va a repetir por segundo el proceso
        rate(100)
            #se esconde a label llamado tiempo para luego eliminarlo
        tiempo.visible=False
            #se elimina el label llamado tiempo
        del tiempo
            #se suman los segundos
        segundos+=dt
            #se asigna el valor de altura por medio de una formula
        altura=posinicial/50+velocidady*segundos-0.5*gravedad*segundos**2
            #se asigna el valor de avance por medio de una formula
        avance=velocidadx*segundos
            #se indica la posicion de la pelota
        pelota1.pos=vector(avance,altura,0)
            #se muestra un label con la altura de la pelota
        tiempo=label(pos=(posinicial/3,posinicial/2,0), text="Altura: "+str(altura-pelota1.radius)+" m")

            #se condiona para que se detenga cuando este en la posicio 0
        if altura-(posinicial/50)<=0:
            tiempo.visible=False
            del tiempo
            fin=True
            winsound.PlaySound("1.wav", winsound.SND_FILENAME)
        #se muestra el label con el tiempo de vuelo
    
        
    etiqueta=label(pos=(posinicial/3,-posinicial,0), text="Tiempo: " + str(segundos)+ " seg")
        #se invoca la fucnion vf
    vf1=vf(gravedad, segundos)
        #se muetra un label con el desplzamiento horizontal
    etiqueta1=label(pos=(posinicial/3,posinicial,0), text="Desplazamiento horizontal: " + str(avance)+ " m")

    dlg = wx.MessageDialog(None, 'Presione OK para salir de la Simulacion','Diálogo de Mensage', wx.OK|wx.ICON_QUESTION)
        
        

    if dlg.ShowModal()==wx.ID_OK:
        scene.visible=False
    dlg.Destroy()

def vertical(frm): 
    velocidad=IngVelocidad(frm)
    posinicial=velocidad*4
    tamano=posinicial
    scene = scene = display(title="Simulador de Tiro Vertical", width=500, height=500, x=0, y=0,center=(0,200/2,200), range=(200, 200, 200))
    
    pelota1=sphere(pos=(0,tamano/20,0),radius=tamano/50, color=color.blue)
    #flecha=arrow(pos=(0,tamano/20,0),axis=pelota1.pos, color=color.blue)
    piso=piso=box(pos=(0,-1,0),size=(200,2,200), color=color.white)

        #se asigna el valor de las variables
    gravedad=9.8
    segundos=0
    angulo=90
    dt=0.01
    angulo=angulo*(pi/180)

        #se asigna el valor de las velocidades en x y y por medio de la formula
    velocidady=velocidad*sin(angulo)
    velocidadx=velocidad*cos(angulo)
        #se asigna el valor de fin
    fin=False
        #se muestra un label con la posicion de la pelota
    tiempo=label(pos=(0,posinicial,0), text=str(posinicial-pelota1.radius))
        #se condiona que se repita el proceso hasta que sea la posicion 0
    while not fin:
            #se asigna las veces que se va a repetir el proceso por segundo
        rate(100)
            #se hace invisble el label llamado tiempo para luego eliminarlo
        tiempo.visible=False
            #se elimina el label tiempo
        del tiempo
            #se suma los segundos
        segundos+=dt
            #se asigna el valor de  alura y avance por medio de una formula
        altura=posinicial/50+velocidady*segundos-0.5*gravedad*segundos**2
        avance=velocidadx*segundos

            #se indica la posicion de la pelota
        pelota1.pos=vector(avance,altura,0)
            #se muestra la altura de la pelota
        tiempo=label(pos=(posinicial/3,posinicial/2,0), text="Altura: "+str(altura-pelota1.radius)+" m")

            
        if altura-(posinicial/50)<=0:
            tiempo.visible=False
            del tiempo
            fin=True
            winsound.PlaySound("1.wav", winsound.SND_FILENAME)

        #se muestras los label con el tiempo y la altura maxima    
    etiqueta=label(pos=(200/3,200,0), text="Tiempo de vuelo: " + str(segundos)+ " seg")
    maxima=alturamax(gravedad, velocidad)
##    flecha=arrow(pos=(0,tamano/20,0),axis=pelota1.pos-maxima, color=color.blue)
    etiqueta2=label(pos=(20,10,0), text="Altura Maxima: " + str(maxima)+ " m")
    dlg = wx.MessageDialog(None, 'Presione OK para salir de la Simulacion','Diálogo de Mensage', wx.OK|wx.ICON_QUESTION)
        
        

    if dlg.ShowModal()==wx.ID_OK:
        scene.visible=False
    dlg.Destroy()

def parabola(frm):
    #Se pide al usuario ingresar el angulo del proyectil
        ang=angulo(frm)
        scene = display(title="Simulador de Tiro Parabolico 2", width=500, height=500, autocenter=1)
        print

        #Se pide al usuario ingresar la velocidad del proyectil
        #vel=funciones.velocidad(raw_input("Cual es la velocidad inicial del objeto?: "))
        vel=velocidad(frm)
        print

        #Se pide al usuario ingresar la gravedad a la cual se quiere trabajar
        #grav=funciones.gravedad(raw_input("Cual es la aceleracion de la gravedad?: "))
        grav=gravedad(frm)
        print

        #El programa calcula la velocidad en "y" del proyectil
        vely=vel*math.sin(math.radians(ang))

        #El programa calcula la velocidad en "x" del proyectil
        velx=vel*math.cos(math.radians(ang))

        #El programa calcula el tiempo que pasa el proyectil en el aire
        tiempo=2*(-vely/grav)

        #El programa calcula la altura maxima del proyectil
        altura=vely*(tiempo/2)+(0.5*grav*((tiempo/2)**2))

        #El programa calcula el alcance maximo del proyectil
        alcance=velx*tiempo
        ##piso=box(pos=(50,0,0),size=(100,2,100), color=color.white)
        #Se asigna el valor del tiempo, de la altura y del alcance a otra variable
        #y dicha variable se convierte a un str, para que a la hora de poner un
        #label podamos controlar la cantidad de decimales que se muestran
        ti=tiempo
        ti=str(ti)
        al=altura
        al=str(al)
        alc=alcance
        alc=str(alc)


        #El programa devuelve los valores de todos los valores calculados
        #con el fin de informar al usuario de dichos valores

        #print "La velocidad inicial en el eje y es: ", vely
        #print "La velocidad inicial en el eje x es: ", velx
        #print "El tiempo que se tarda el proyectil en volver a descender es: ",tiempo
        #print "La altura maxima que alcanza el proyectil es: ", altura
        #print "El alcanze el proyectil es: ", alcance

        #Se hacen unas variables vx y vy con un fin estatico. Al poner los labels en
        #la pantalla es necesario agregarles una altura y un corrimiento para que no
        #queden sobre el grafico. Para que estos valores de corrimiento no sean
        #estaticos, se hacen estas variables, para que cambien dependiendo de los valores
        #ingresados por el usuario
        vx=alcance/7
        vy=altura/2

        #Las variable shaft se crea tambien con un fin estatico. Debido a que el grosor
        #de los cilindros depende de su longitud, estos serian demasiado gruesos si los
        #valores ingresados por el usuario son demasiado grandes. Por lo que la variable
        #shaft sirve para regular el grosor de los cilindros.
        shaft=alcance/(alcance+altura)

        #El autocenter sirve para que aunque la grafica se vaya moviendo, esta siga
        #centrada
        
        
        #Hace que todas los graficos se muestren

        #Se hacen los labels, que contienen la informacion del alcance, altura y
        #tiempo
        label(pos=(alcance-vx,-vx,0) , text="Alcance: "+alc[0:6]+"m")
        label(pos=(vy*3,altura+vy,0), text="Altura maxima: "+al[0:6]+"m")
        label(pos=(alcance-vx,altura+vy,0), text="Tiempo de vuelo: "+ti[0:6]+"s")

        #Se definen dos flechas de distintos colores, que son las que van a variar
        #dependiendo de la velocidad en "x" y "y" el proyectil

        
        flechay=arrow(pos=vector(0,0,0), axis=vector(0,0,0),color=color.red)
        flechax=arrow(pos=vector(0,0,0), axis=vector(0,0,0),color=color.blue)

        #Se hace un contador, que servira como el tiempo transcurrido por el proyectil
        t=0
        #Mientras esta variable no sea exactamente igual al tiempo real de vuelo del
        #proyectil, la variable t seguira contando
        while t<tiempo:
            t=t+0.01
            #El rate sirve para restringir al programa la cantidad de operaciones
            #que realize por segundo
            rate(300)

            #Se hacen dos variables de las velocidades "x" y "y" para ir variando
            #la longitud de las flechas que representan las velocidades
            velocidady=vely+(grav*t)
            velocidadx=velx

            #Se hacen dos variables de la posicion en "x" y "y" que tiene el proyectil
            #dependiendo del tiempo
            posicionx=velx*t
            posiciony=vely*t+(0.5*grav*t**2)

            #Se varia la posicion y longitud de las flechas que representan la
            #la velocidad del proyectil en cada eje
            flechay.pos=(posicionx,posiciony,0)
            flechax.pos=(posicionx,posiciony,0)
            flechay.axis=(0,velocidady,0)
            flechax.axis=(velocidadx,0,0)

            #Se varia la posicion de los cilindros que representan un eje de coordenadas
            #"x" y "y"
            a=cylinder(pos=(posicionx,0,0), radius=1)
            b=cylinder(pos=(0,posiciony,0), radius=1)

            #Se varia la posicion de un cilindro que demuestra el camino que recorre
            #el proyectil
            c=cylinder(pos=(posicionx,posiciony,0),radius=1)
        dlg = wx.MessageDialog(None, 'Presione OK para salir de la Simulacion','Diálogo de Mensage', wx.OK|wx.ICON_QUESTION)
        
        

        if dlg.ShowModal()==wx.ID_OK:
            scene.visible=False
        dlg.Destroy()

def roce(frm):
    
    posinicial=10
    tamano=posinicial    
    altura= posinicial
    velocidad=55
    scene = display(title="Simulador de Coeficiente de friccion", width=800, height=800, x=0, y=0,center=(0,200/2,100), range=(300*2, 200*2, 300*2),autocenter=1)
    pelota1=sphere(pos=(0,posinicial/20,0),radius=tamano/50, color=color.blue) # la altura depende del radio de la pelta
    caja=box(pos=(0,posinicial/20,0),size=(70,24,70), color=color.red)    
    piso=box(pos=(0,-1,0),size=(200*5,2,200*5), color=color.white)

           
   



#se asignan el valor de las variables
    gravedad=0 #la gravedad varia la distancia a la que cae el balon
    segundos=0
    dt=0.01
    fin=False
    masa=float(frm.txtmasa.GetValue())
    caja1=frm.cobcaja.GetValue()
    piso1=frm.cobpiso.GetValue()
    coeficiente=0    

#se muestra la posici?n de la pelota
#tiempo=label(pos=(0,posinicial,0), text=str(posinicial-pelota1.radius))
    

#se condiona para que se repita el proceso
    if caja1=="Acero" and piso1=="Acero":
        coeficiente=0.57
    solucion=float(coeficiente*masa)

    if caja1=="Aluminio" and piso1=="Acero":
        coeficiente=0.47
    solucion=float(coeficiente*masa)

    if caja1=="Cobre" and piso1=="Acero":
        coeficiente=0.36
    solucion=float(coeficiente*masa)

    if caja1=="Laton" and piso1=="Acero":
        coeficiente=0.44
    solucion=float(coeficiente*masa)

    if caja1=="Cinc" and piso1=="Hierro Colado":
        coeficiente=0.21
    solucion=float(coeficiente*masa)

    if caja1=="Caucho" and piso1=="Concreto":
        coeficiente=0.8
    solucion=float(coeficiente*masa)

    if caja1=="Madera" and piso1=="Madera":
        coeficiente=0.2
    solucion=float(coeficiente*masa)

    if caja1=="Vidrio" and piso1=="Vidrio":
        coeficiente=0.4
    solucion=float(coeficiente*masa)

    if caja1=="Hielo" and piso1=="Hielo":
        coeficiente=0.03
    solucion=float(coeficiente*masa)

    if caja1=="Teflon" and piso1=="Teflon":
        coeficiente=0.04
    solucion=float(coeficiente*masa)

    if caja1=="Teflon" and piso1=="Acero":
        coeficiente=0.04
    solucion=float(coeficiente*masa)

    while not fin:

#se le indica cuantas veces realizar el proceso
        rate(100)
        #se le indica que la label llamada tiempo sea invisible para luego eliminarla
    #tiempo.visible=False
            #se elimina el label llamado tiempo
    #del tiempo
            #se suman los segundos que pasan
        segundos+=dt
            #se le indica que altura es la formula de movimiento en el eje y
        altura=posinicial-(0.5*gravedad*(segundos)**2)
            #se le indiac que avance es la formula de movimiento en el eje x
        avance=velocidad*segundos
            #se le indica la posicion de la pelota
        pelota1.pos=vector(avance,altura,0)
        caja.pos=vector(avance,altura,0)
            #se muestra un label con la altuta de la pelota
    #tiempo.visible=False
            #se condiona que cuando este en la posicion cero deje de moverse
    
        if scene.kb.keys : #con esta funciona se da click (Teclado)
            
        #tiempo.visible=False
        #del tiempo
            fin=True
            winsound.PlaySound("1.wav", winsound.SND_FILENAME)
        #se muestra el label con el tiempo que esta en movimiento        
            etiqueta=label(pos=(200/3,200,0), text="La fuerza de Roce: " + str(solucion)+ " N")
    etiqueta1=label(pos=(-500,550,-300),text="Calculo de friccion\nMateriales: Caja: " + str(caja1)+ ", Piso:" + str(piso1)+ "\nMasa:" + str(masa)+ "\nCoeficiente de Friccion:" + str(coeficiente)+ "\nFr=U.N\nFr=" + str(coeficiente)+ "*" + str(masa)+ "=" + str(solucion)+ "")    #piso2=box(pos=(200,450,0),size=(80,0,50), color=color.white)
    caja=box(pos=(200,450,0),size=(50,10,10), color=color.red)

    Flechan=box(pos=(200,500,0),size=(0.5,100,5), color=color.white)
    Flechaw=box(pos=(200,400,0),size=(0.5,100,5), color=color.blue)
    Flechafr=box(pos=(250,450,0),size=(100,1,5), color=color.yellow)
    Flechaf=box(pos=(150,450,0),size=(100,1,5), color=color.green)

    N=label(pos=(200,580,0),text="N")
    W=label(pos=(200,340,0),text="M*G")
    FR=label(pos=(315,450,0),text="Fr")
    F=label(pos=(80,450,0),text="F")
    #flecha=arrow(pos=(200,450,0), axis=vector(+1,+3,0),color=color.red) probando
    
    
    dlg = wx.MessageDialog(None, 'Presione OK para salir de la Simulacion','Diálogo de Mensage', wx.OK|wx.ICON_QUESTION)
        
        

    if dlg.ShowModal()==wx.ID_OK:
        scene.visible=False
    dlg.Destroy()
    
