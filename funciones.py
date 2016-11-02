#! /usr/bin/env python
# -*- coding: CP1252-*-
#self.db.execute(SQL_STRING, (dork.decode('utf-8'), ))
import pygame
import sqlite3 as sq3
import wx
import Entrada as E
import PrincipalEstu as PE
import PrincipalProf as P
import PrincipalAdmin as PA
import GuardarAlumno as G
global posinicial
global vel
#from visual import*
import math
from time import time
import datetime
import matplotlib.pyplot as plt
import numpy.numarray as na



#import os



#Conexion base de datos
def conexion():
    con=sq3.connect('Simulacion.s3db')
    cur = con.cursor()
    return con, cur

def desconectar():
    cur.Close()
    con.Close()
    return



def Bitacora(frm):
    Usu=frm.txtUsuario.GetValue()
    En=Usu.upper()
    
    Hora=datetime.datetime.now()
    
    Fecha = datetime.date.today()
    datos=(En,Fecha,Hora)

    con,cur=conexion()


    cur.execute("Insert into Bitacora (Usuario,Fecha,Hora) Values (?,?,?)", (En,Fecha,Hora))
    

    con.commit()
    cur.close()
    con.close()

def Registro(frm): #no se esta usando
    
    Va=frm.txtCedula.GetValue()
    
    Hora=datetime.datetime.now()
    
    Fecha = datetime.date.today()
    #datos=(En,Fecha)

    con,cur=conexion()
    cur.execute("Select min(Usuario) from Bitacora")
    rs=cur.fetchone()
    if rs:
        
        N=(str(rs[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora) Values (?,?,?,?)", (N,Fecha,Va,Hora))
    

        con.commit()
        cur.close()
        con.close()

def Bloquear(frm):
    self=frm
    con,cur=conexion()
    U=frm.txtNombre.GetValue()
    Usu=U.upper()
    dato=Usu
    
    cur.execute("Select Estado from Usuarios where Nombre=:dato",{"dato":dato})
    
    rs=cur.fetchone() 
    N=int(rs[0])
    if N ==1:
        wx.MessageBox('Error, El usuario ya estaba bloqueado', 'Caja de mensaje')
    else:
        cur.execute("Update  Usuarios set Estado= 1 where Nombre=:dato",{"dato":dato})
        wx.MessageBox('Usuario Bloqueado Satisfactoriamente', 'Caja de mensaje')
        con.commit()

        self.txtNombre.Clear()
        self.txtClave.Clear()
        self.cobTipo.Clear()

def Desbloquear(frm):
    self=frm
    con,cur=conexion()
    U=frm.txtNombre.GetValue()
    Usu=U.upper()
    dato=Usu
    cur.execute("Select Estado from Usuarios where Nombre=:dato",{"dato":dato})
    rs=cur.fetchone()
    N=int(rs[0])
    if N ==0:
        wx.MessageBox('Error, El usuario no esta bloqueado', 'Caja de mensaje')
    else:
        cur.execute("Update  Usuarios set Estado= 0 where Nombre=:dato",{"dato":dato})
        wx.MessageBox('Usuario Desbloqueado Satisfactoriamente', 'Caja de mensaje')
        con.commit()

        self.txtNombre.Clear()
        self.txtClave.Clear()
        self.cobTipo.Clear()

    
def Reporte(tp):#no se usa.
    con, cur = conexion()
    t = (tp,)
    cur.execute('Select * from Bitacora order by Usuario')
    rs = cur.fetchall()
    
    return rs


def Entrada(frm):

    Usu=frm.txtUsuario.GetValue()
    En=Usu.upper()
    Cla=frm.txtClave.GetValue()
    datos=(En,Cla)
    
    con,cur=conexion()
    self=frm

    cur.execute("Select Estado from Usuarios where Estado= 1 and Nombre=:En",{"En":En})
    rs=cur.fetchone()
    
    if rs:
        dlg=wx.MessageDialog(self,'Usuario Bloqueado', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    else:
        cur.execute("Select * from Usuarios Where Nombre=? and Clave=? and Tipo='ADMINISTRADOR'",datos)
        rs1=cur.fetchone()
        
        if rs1:
            
            Ventana=PA.Principal(self)
            Ventana.Show()
            self.Hide()
        else:
            cur.execute("Select * from Usuarios Where Nombre=? and Clave=? and Tipo='PROFESOR'",datos)
            rs2=cur.fetchone()
            if rs2:
        
                Ventana=P.Principal(self)
                Ventana.Show()
                self.Hide()
            else:
                cur.execute("Select * from Usuarios Where Nombre=? and Clave=? and Tipo='ESTUDIANTE'",datos)
                rs3=cur.fetchone()
                if rs3:
                    Ventana=PE.Principal(self)
                    Ventana.Show()
                    self.Hide()
                else:
                    dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
                    dlg.ShowModal()
                    dlg.Destroy()
                    

    
def GuardarAlumno(frm):
    #Id=frm.txtId.GetValue()
    self=frm
    No = frm.txtNombre.GetValue()
    Nom=No.upper()
    Ap  = frm.txtApellido.GetValue()
    Ape= Ap.upper()
    Ce= frm.txtCedula.GetValue()
    Se=frm.cobSexo.GetValue()
    Es=frm.cobEstado.GetValue()
    Mu=frm.cobMunicipio.GetValue()
    Pa=frm.cobParroquia.GetValue()
    Di=frm.cobDireccion.GetValue()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Guardar Alumno"
    Car=frm.cobCarrera.GetValue()
    Sec=frm.cobSeccion.GetValue()
    datos1=(Nom,Ape,Ce,Se)
    con, cur = conexion()
    dato=frm.txtCedula.GetValue()
    datos=(Car,Sec)
    cur.execute("select Cedula from Estudiante where Cedula=:dato",{"dato": dato})
    rs=cur.fetchone()
    if rs:
       wx.MessageBox('Cedula Repetida', 'Caja de mensaje') 
    else:
        cur.execute("select id from Direccion where Nombre=:Di",{"Di":Di})
        rs1=cur.fetchone()
        if rs1:
            N=(str(rs1[0]))#codigo pa conseguir el id del campo parroquia pa poder hacer las relaciones entre tablas
            cur.execute("select Seccion.Id from Seccion, Carrera where Seccion.Id_Carrera=Carrera.Id and Carrera.Nombre=? and Seccion.Seccion=?",(datos))
            rs3=cur.fetchone()
            if rs3:
                S=str(rs3[0])
                
                cur.execute('INSERT INTO Estudiante (Nombre,Apellido,Cedula,Sexo,Id_Direccion,Id_Seccion) VALUES (?,?,?,?,?,?)',(Nom,Ape,Ce,Se,N,S))
                wx.MessageBox('Guardado Satisfactoriamente', 'Caja de mensaje')       
                con.commit()

        
                cur.execute("Select min(Usuario) from Bitacora")
                rs2=cur.fetchone()
                if rs2:
        
                    N=(str(rs2[0]))
                    cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Ce,Hora,Op))
                    con.commit()
    self.txtNombre.Clear()
    self.txtApellido.Clear()
    #self.txtCedula.Clear()
    self.cobMunicipio.Clear()
    self.cobParroquia.Clear()
    self.cobDireccion.Clear()
    self.txtNombre.SetFocus()        
    cur.close()
    con.close()
    return

def GuardarProfesor(frm):#no se usa
    
    No = frm.txtNombre.GetValue()
    Ap  = frm.txtApellido.GetValue()
    Ce= frm.txtCedula.GetValue()
    Se=frm.cobSexo.GetValue()
    Es=frm.cobEstado.GetValue()
    Mu=frm.txtMunicipio.GetValue()
    Pa=frm.txtParroquia.GetValue()
    Di=frm.txtDireccion.GetValue()
    
    datos1 = (No,Ap,Ce,Se)
    
    con, cur = conexion()
    
    cur.execute('INSERT INTO Profesor (Nombre,Apellido,Cedula,Sexo) VALUES (?,?,?,?)',(datos1))
    wx.MessageBox('Guardado Satisfactoriamente', 'Caja de mensaje')
        
    cur.close()
    con.close()
    return

def GuardarUsuario(frm):
    No=frm.txtNombre.GetValue()
    Nom=No.upper()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Guardar Usuario"
    Cla=frm.txtClave.GetValue()
    Ti=frm.cobTipo.GetValue()
    Es=0

    datos1=(Nom,Cla,Ti,Es)
    self=frm
    con, cur=conexion()
    # Saber si es menor de 8 caracteres
    if len(Cla)< 8:
        dlg=wx.MessageDialog(self,'La clave debe ser mayor a 8 caracteres', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        self.txtClave.Clear()
        self.txtClave.SetFocus()
    else:#isdigit solo numeros isalpha solo letras.... comparacion alfanumerica
        if Cla.isdigit()or Cla.isalpha() : #isdigit puros numeros, isalpha puras letras
            dlg=wx.MessageDialog(self,'La Clave Debe Contener Datos Alfanumericos', 'Atencion', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
            self.txtClave.Clear()
            self.txtClave.SetFocus()
        
        else:       
            cur.execute('INSERT INTO Usuarios (Nombre,Clave,Tipo, Estado) VALUES (?,?,?,?)',(datos1))
            wx.MessageBox('Guardado Satisfactoriamente', 'Caja de mensaje')
            con.commit()
            
            cur.execute("Select min(Usuario) from Bitacora")
            rs2=cur.fetchone()
            if rs2:
        
                N=(str(rs2[0]))
                cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Nom,Hora,Op))
                con.commit()
                
                dlg = wx.MessageDialog(None, '¿Desea Agregar Otro Usuario?',
                           'Diálogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
                
                if dlg.ShowModal()==wx.ID_OK:
                    pass
                else:
                    
                    Ventana=PA.Principal(self)
                    Ventana.Show()
                    self.Hide()
                dlg.Destroy()
                
            self.txtNombre.Clear()
            self.txtClave.Clear()
            #self.cobTipo.Clear()
            self.txtNombre.SetFocus()
            
            cur.close()
            con.close()
        
    

def Buscar(frm):
    con, cur = conexion()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Buscar Estudiante"
    dato= frm.txtCedula.GetValue()
    cur.execute("Select Estudiante.Nombre,Estudiante.Apellido, Estudiante.Sexo,Estado.Nombre,Munic.Nombre,Parroquia.Nombre,Direccion.Nombre, Seccion.Seccion, Carrera.Nombre from Estudiante,Estado,Munic,Parroquia,Direccion,Seccion,Carrera where  Estudiante.Id_Direccion=Direccion.Id and Direccion.Id_Parroquia=Parroquia.Id  and Parroquia.Id_Munic=Munic.Id and Munic.Id_Estado=Estado.Id and Estudiante.Id_Seccion=Seccion.Id and Seccion.Id_Carrera=Carrera.Id and Estudiante.Cedula=:dato",{"dato": dato})
    rs = cur.fetchone()
    self=frm
    if rs:
        
        self.txtNombre.SetValue(str(rs[0]))
        self.txtApellido.SetValue(str(rs[1]))
        #self.txtCedula.SetValue(int(rs[2]))
        self.cobSexo.SetValue(str(rs[2]))
        self.cobEstado.SetValue(str(rs[3]))
        self.cobMunicipio.SetValue(str(rs[4]))
        self.cobParroquia.SetValue(str(rs[5]))
        self.cobDireccion.SetValue(str(rs[6]))
        self.cobSeccion.SetValue(str(rs[7]))
        self.cobCarrera.SetValue(str(rs[8]))
        self.txtNombre.SetFocus()
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,dato,Hora,Op))
            con.commit()
    else:
        dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

def BuscarC(frm):#no lo uso
    
    #self=frm
    #i=0
    #Carreras=["Mantenimiento Naval","Mecanica y Construccion Naval", "Ingenieria Mecanica"]
    #while i<len(Carreras):
        #self.cobCarrera.Append(str(Carreras[i]))
        #i=i+1
    pass

def BuscarS(frm):
    con,cur=conexion()
    dato=frm.cobCarrera.GetValue()
    cur.execute("Select Seccion.Seccion from carrera, seccion where seccion.Id_Carrera=Carrera.Id and Carrera.Nombre=:dato",{"dato":dato})
    rs=cur.fetchall()

    self=frm
    i=0
    while i <len(rs):
        string=unicode(rs,'utf-8')
        self.cobSeccion.Append(string)
        i=i+1
def BuscarU(frm):
    con,cur=conexion()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Buscar Usuario"
    dato1=frm.txtNombre.GetValue()
    dato=dato1.upper()
    cur.execute("Select * from Usuarios where Nombre=:dato",{"dato":dato})
    
    rs=cur.fetchone()
    self=frm
    if rs:
        self.txtNombre.SetValue(str(rs[0]))
        self.txtClave.SetValue(str(rs[1]))
        self.cobTipo.SetValue(str(rs[2]))
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,dato1,Hora,Op))
            con.commit()
    else:
        dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
  
def BuscarM(frm):
    
    dato=frm.cobEstado.GetValue()
    
   
    
    self=frm

    
    i=0
    
    Merida=["Alberto Adriani","Andres Bello","Antonio Pinto Salinas","Aricagua","Arzobispo Chacon","Campo Elias","Caracciolo Parra Olmedo","Cardenal Quintero","Guaraque","Julio Cesar","Justo Briceno","Libertador","Miranda","Obispo Ramos de Lora","Padre Noguera","Pueblo Llano","Rangel","Rivas Davila","Santos Marquina","Sucre","Tovar","Tulio Febres Cordero","Zea"]
    Sucre=["Bermudez","Sucre","Benitez","Cruz Salmeron Acosta","Bolivar","Arismendi","Ribero","Valdez","Montes","Mejia","Marino","Libertador","Andres Mata","Andres Eloy Blanco","Cajigal"]
    if dato=="Merida":
        self.cobMunicipio.Clear()
        while i <len(Merida):
            self.cobMunicipio.Append(Merida[i])
            i=i+1
    elif dato=="Sucre":
        self.cobMunicipio.Clear()
        while i <len(Sucre):
            self.cobMunicipio.Append(Sucre[i])
            i=i+1

def materiales(frm):
    dato=frm.cobcaja.GetValue()
    self=frm
    i=0
    Acero=["Acero"]
    Aluminio=["Acero"]
    Cobre=["Acero","Vidrio"]
    Laton=["Acero"]
    Cinc=["Hierro Colado"]
    Caucho=["Concreto"]
    Madera=["Madera"]
    Vidrio=["Vidrio"]
    Hielo=["Hielo"]
    Teflon=["Teflon","Acero"]

    if dato=="Acero":
        self.cobpiso.Clear()
        while i < len(Acero):
            self.cobpiso.Append(Acero[i])
            i=i+1
    if dato=="Aluminio":
        self.cobpiso.Clear()
        while i < len(Aluminio):
            self.cobpiso.Append(Aluminio[i])
            i=i+1
    if dato=="Cobre":
        self.cobpiso.Clear()
        while i < len(Cobre):
            self.cobpiso.Append(Cobre[i])
            i=i+1
    if dato=="Laton":
        self.cobpiso.Clear()
        while i < len(Laton):
            self.cobpiso.Append(Laton[i])
            i=i+1
    if dato=="Cinc":
        self.cobpiso.Clear()
        while i < len(Cinc):
            self.cobpiso.Append(Cinc[i])
            i=i+1
    if dato=="Caucho":
        self.cobpiso.Clear()
        while i < len(Caucho):
            self.cobpiso.Append(Caucho[i])
            i=i+1
    if dato=="Madera":
        self.cobpiso.Clear()
        while i < len(Madera):
            self.cobpiso.Append(Madera[i])
            i=i+1
    if dato=="Vidrio":
        self.cobpiso.Clear()
        while i < len(Vidrio):
            self.cobpiso.Append(Vidrio[i])
            i=i+1
    if dato=="Hielo":
        self.cobpiso.Clear()
        while i < len(Hielo):
            self.cobpiso.Append(Hielo[i])
            i=i+1
    if dato=="Teflon":
        self.cobpiso.Clear()
        while i < len(Teflon):
            self.cobpiso.Append(Teflon[i])
            i=i+1
def BuscarP(frm):
    
    dato=frm.cobMunicipio.GetValue()

    self=frm
    i=0
    #Listas de las Parroquias (problemas con el unicode)
    Bermudez=["Santa Catalina","Santa Rosa","Santa Teresa", "Bolivar", "Macarapana"]
    Sucre=["San Juan","Altagracia","Ayacucho","Gran Mariscal","Raul Leoni","Valentin Valiente"]
    Benitez=["El Pilar","El Rincon","General Francisco Antonio Vazquez","Guaraunos","Tunapuicito","Union"]
    Cruz_Salmeron_Acosta=["Cruz Salmeron Acosta", "Chacopata","Manicuare"]
    Bolivar=["Mariguitar"]
    Arismendi=["Antonio Jose de Sucre","El Morro de Puerto Santo","Puerto Santo","Río Caribe","San Juan de las Galdonas"]
    Ribero=["Catuaro","Rendon","Santa Cruz","Santa Maria","Villa Frontado"]
    Valdez=["Bideau","Cristobal Colon","Guiria","Punta de Piedras"]
    Montes=["Arenas","Aricagua","Cocollar","Cumanacoa","San Fernando","San Lorenzo"]
    Mejia=["Mejia"]
    Marino=["Irapa","Campo Claro","Maraval","San Antonio de Irapa","Soro"]
    Libertador=["Tunapuy","Campo Elias"]
    Andres_Mata=["San Jose de Aerocuar","Tavera Acosta"]
    Andres_Eloy_Blanco=["Marino","Romulo Gallegos"]
    Cajigal=["Libertad","ElPaujil","Yaguaraparo"]
    
    if dato=="Bermudez":
        self.cobParroquia.Clear()
        while i<len(Bermudez):
            self.cobParroquia.Append(Bermudez[i])
            i=i+1
    if dato=="Sucre":
        self.cobParroquia.Clear()
        while i<len(Sucre):
            self.cobParroquia.Append(Sucre[i])
            i=i+1
    if dato=="Benitez":
        self.cobParroquia.Clear()
        while i<len(Benitez):
            self.cobParroquia.Append(Benitez[i])
            i=i+1
    if dato=="Cruz Salmeron Acosta":
        self.cobParroquia.Clear()
        while i<len(Cruz_Salmeron_Acosta):
            self.cobParroquia.Append(Cruz_Salmeron_Acosta[i])
            i=i+1
    if dato=="Bolivar":
        self.cobParroquia.Clear()
        while i<len(Bolivar):
            self.cobParroquia.Append(Bolivar[i])
            i=i+1
    if dato=="Arismendi":
        self.cobParroquia.Clear()
        while i<len(Arismendi):
            self.cobParroquia.Append(Arismendi[i])
            i=i+1
    if dato=="Ribero":
        self.cobParroquia.Clear()
        while i<len(Ribero):
            self.cobParroquia.Append(Ribero[i])
            i=i+1
    if dato=="Valdez":
        self.cobParroquia.Clear()
        while i<len(Valdez):
            self.cobParroquia.Append(Valdez[i])
            i=i+1
    if dato=="Montes":
        self.cobParroquia.Clear()
        while i<len(Montes):
            self.cobParroquia.Append(Montes[i])
            i=i+1
    if dato=="Mejia":
        self.cobParroquia.Clear()
        while i<len(Mejia):
            self.cobParroquia.Append(Mejia[i])
            i=i+1
    if dato=="Marino":
        self.cobParroquia.Clear()
        while i<len(Marino):
            self.cobParroquia.Append(Marino[i])
            i=i+1
    if dato=="Libertador":
        self.cobParroquia.Clear()
        while i<len(Libertador):
            self.cobParroquia.Append(Libertador[i])
            i=i+1
    if dato=="Andres Mata":
        self.cobParroquia.Clear()
        while i<len(Andres_Mata):
            self.cobParroquia.Append(Andres_Mata[i])
            i=i+1
    if dato=="Andres Eloy Blanco":
        self.cobParroquia.Clear()
        while i<len(Andres_Eloy_Blanco):
            self.cobParroquia.Append(Andres_Eloy_Blanco[i])
            i=i+1
    if dato=="Andres Mata":
        self.cobParroquia.Clear()
        while i<len(Andres_Mata):
            self.cobParroquia.Append(Andres_Mata[i])
            i=i+1
def BuscarD(frm):
    
    dato=frm.cobParroquia.GetValue()
    self=frm
    i=0
    Bermudez=["Santa Catalina","Santa Rosa","Santa Teresa", "Bolivar", "Macarapana"]
    Santa_Catalina=["Los Molinos", "San Jose", "San Roque"]
    Santa_Rosa=["Tio Pedro","Centro"]
    Santa_Teresa=[]
    Bolivar=[]
    Macarapana=["Macarapana"]
    if dato=="Santa Catalina":
        self.cobDireccion.Clear()
        while i<len(Santa_Catalina):
            self.cobDireccion.Append(Santa_Catalina[i])
            i=i+1
    if dato=="Santa Rosa":
        self.cobDireccion.Clear()
        while i<len(Santa_Rosa):
            self.cobDireccion.Append(Santa_Rosa[i])
            i=i+1
    if dato=="Santa Teresa":
        self.cobDireccion.Clear()
    if dato=="Bolivar":
        self.cobDireccion.Clear()
    if dato=="Macarapana":
        self.cobDireccion.Clear()
        while i<len(Macarapana):
            self.cobDireccion.Append(Macarapana[i])
            i=i+1

def ModificarAlumno(frm):
    
    No = frm.txtNombre.GetValue()
    Nom=No.upper()
    Ap  = frm.txtApellido.GetValue()
    Ape=Ap.upper()
    Ce= frm.txtCedula.GetValue()
    Se=frm.cobSexo.GetValue()
    Es=frm.cobEstado.GetValue()
    Mu=frm.cobMunicipio.GetValue()
    Pa=frm.cobParroquia.GetValue()
    Di=frm.cobDireccion.GetValue()
    Car=frm.cobCarrera.GetValue()
    Sec=frm.cobSeccion.GetValue()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Buscar Usuario"
    
    self=frm
    
    con, cur = conexion()
    cur.execute("select id from Direccion where Nombre=:Di",{"Di":Di})
    rs1=cur.fetchone()
    if rs1:
        N=(str(rs1[0]))#codigo pa conseguir el id del campo parroquia pa poder hacer las relaciones entre tablas
        cur.execute("select Seccion.Id from Seccion, Carrera where Seccion.Id_Carrera=Carrera.Id and Carrera.Nombre=? and Seccion.Seccion=?",(Car,Sec))
        rs3=cur.fetchone()
        if rs3:
            S=str(rs3[0])

            cur.execute('UPDATE Estudiante Set Nombre=?, Apellido=?, Sexo=?, Id_Direccion=?, Id_Seccion=? WHERE Cedula=?',(Nom,Ape,Se,N,S,Ce))
            wx.MessageBox('Modificado Satisfactoriamente', 'Caja de mensaje')
            con.commit()

            cur.execute("Select min(Usuario) from Bitacora")
            rs2=cur.fetchone()
            if rs2:
        
                N=(str(rs2[0]))
                cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,Ce,Hora,Op))
                con.commit()
    self.txtNombre.Clear()
    self.txtApellido.Clear()
    self.txtCedula.Clear()
    
    self.cobMunicipio.Clear()
    self.cobParroquia.Clear()
    self.cobDireccion.Clear()
    self.txtCedula.SetFocus()
    cur.close()
    con.close()
    return

def EliminarAlumno(frm):
    
    self=frm
    dato= frm.txtCedula.GetValue()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Eliminar Alumno "
    
    con, cur = conexion()
    
   
    cur.execute("Select * from Estudiante where Cedula=:dato",{"dato":dato})
    rs=cur.fetchone()
    if rs:
        cur.execute("Delete  from Estudiante WHERE Cedula=:dato",{"dato": dato})
        wx.MessageBox('Eliminado Satisfactoriamente', 'Caja de mensaje')
        con.commit()

        self.txtNombre.Clear()
        self.txtApellido.Clear()
        self.txtCedula.Clear()
        self.cobSexo.Clear()
        self.cobEstado.Clear()
        self.cobMunicipio.Clear()
        self.cobParroquia.Clear()
        self.cobDireccion.Clear()
        self.cobSeccion.Clear()
        self.cobCarrera.Clear()
        self.txtCedula.SetFocus()
        cur.execute("Select min(Usuario) from Bitacora")
        rs2=cur.fetchone()
        if rs2:
        
            N=(str(rs2[0]))
            cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,dato,Hora,Op))
            con.commit()
    else:
        dlg=wx.MessageDialog(self,'No se encontro el registro', 'Atencion', wx.OK)
        dlg.ShowModal()
        dlg.Destroy()          
    cur.close()
    con.close()
    return
def EliminarUsuario(frm):
    self=frm
    dato=frm.txtNombre.GetValue()
    Hora=datetime.datetime.now()
    Fecha = datetime.date.today()
    Op="Eliminar Usuario"
    con,cur=conexion()

    cur.execute("Delete from Usuarios where Nombre=:dato",{"dato":dato})
    wx.MessageBox('Eliminado Satisfactoriamente', 'Caja de mensaje')
    con.commit()
    self.txtNombre.Clear()
    self.txtClave.Clear()
    self.cobTipo.Clear()
    cur.execute("Select min(Usuario) from Bitacora")
    rs2=cur.fetchone()
    if rs2:
        
        N=(str(rs2[0]))
        cur.execute("Insert into Registro (Usuario,Fecha,Variable,Hora,Operacion) Values (?,?,?,?,?)", (N,Fecha,dato,Hora,Op))
        con.commit()  
    cur.close()
    con.close()
    return

def ReporUA(self):
    #conn = sqlite3.connect('Simulacion.s3db')
    #c = conn.cursor()
    con,cur=conexion()
#c.execute('drop table if exists failed_banks')
#c.execute('create table failed_banks(id integer primary key autoincrement, name text, city text, state text, zip integer, close_date text, updated_date text)')

    
# Get failed banks by year, for fun
    cur.execute("Select strftime('%Y',Fecha),count(*) from Bitacora  group by 1;")
    years = []
    failed_banks = []
    for row in cur:
        years.append(row[0])
        failed_banks.append(row[1])

# Plot the data, for fun


    values = tuple(failed_banks)
    ind = na.array(range(len(values))) + 0.5
    width = 0.35
    plt.bar(ind, values, width, color='r')
    plt.ylabel("Cantidad de Usuarios")
    plt.xlabel("Tiempo en Anos")
    plt.title('Reporte de Usuarios por Ano')
    plt.xticks(ind+width/2, tuple(years))
    plt.show()

# Clean up
    cur.close()

def ReporUM(self):
    #conn = sqlite3.connect('Simulacion.s3db')
    #c = conn.cursor()
    con,cur=conexion()
#c.execute('drop table if exists failed_banks')
#c.execute('create table failed_banks(id integer primary key autoincrement, name text, city text, state text, zip integer, close_date text, updated_date text)')

    
# Get failed banks by year, for fun
    cur.execute("Select strftime('%m',Fecha),count(*) from Bitacora  group by 1;")
    years = []
    failed_banks = []
    for row in cur:
        years.append(row[0])
        failed_banks.append(row[1])

# Plot the data, for fun


    values = tuple(failed_banks)
    ind = na.array(range(len(values))) + 0.5
    width = 0.35
    plt.bar(ind, values, width, color='r')
    plt.ylabel("Cantidad de Usuarios")
    plt.xlabel("Tiempo en Meses")
    plt.title('Reporte de Usuarios por Mes')
    plt.xticks(ind+width/2, tuple(years))
    plt.show()

# Clean up
    cur.close()

def ReporUD(self):
    #conn = sqlite3.connect('Simulacion.s3db')
    #c = conn.cursor()
    con,cur=conexion()
#c.execute('drop table if exists failed_banks')
#c.execute('create table failed_banks(id integer primary key autoincrement, name text, city text, state text, zip integer, close_date text, updated_date text)')

    
# Get failed banks by year, for fun
    cur.execute("Select strftime('%d',Fecha),count(*) from Bitacora  group by 1;")
    years = []
    failed_banks = []
    for row in cur:
        years.append(row[0])
        failed_banks.append(row[1])

# Plot the data, for fun


    values = tuple(failed_banks)
    ind = na.array(range(len(values))) + 0.5
    width = 0.35
    plt.bar(ind, values, width, color='r')
    plt.ylabel("Cantidad de Usuarios")
    plt.xlabel("Tiempo en Dias")
    plt.title('Reporte de Usuarios por Dia')
    plt.xticks(ind+width/2, tuple(years))
    plt.show()

# Clean up
    cur.close()
    
