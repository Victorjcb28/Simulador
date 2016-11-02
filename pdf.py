# -*- coding: cp1252 -*-
import os

#Obtenemos de platypus las clases Paragraph, para escribir párrafos Image, para insertar imágenes y SimpleDocTemplate para definir el DocTemplate. Además importamos Spacer, para incluir espacios .

from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.platypus import Table
#Importamos clase de hoja de estilo de ejemplo.

from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet

#Se importa el tamaño de la hoja.

from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import letter, landscape

#Y los colores.

from reportlab.lib import colors
import sqlite3 as sq3

def conexion():
    con=sq3.connect('Simulacion.s3db')
    con.text_factory=str #pa quitar la U
    cur = con.cursor()
    return con, cur

def desconectar():
    cur.Close()
    con.Close()
    return

def pdf(self):
    con, cur = conexion()


#Creamos un PageTemplate de ejemplo.

    estiloHoja = getSampleStyleSheet()

#Inicializamos la lista Platypus Story.

    story = []

#Definimos cómo queremos que sea el estilo de la PageTemplate.

    cabecera = estiloHoja['Heading4']
    #estilo2 = estiloHoja['Normal'] Prueba de Leyenda
#No se hará un salto de página después de escribir la cabecera (valor 1 en caso contrario).

    cabecera.pageBreakBefore=0

#Se quiere que se empiece en la primera página a escribir. Si es distinto de 0 deja la primera hoja en blanco.

    cabecera.keepWithNext=0

#Color de la cabecera.

    cabecera.backColor=colors.cyan

#Incluimos un Flowable, que en este caso es un párrafo.

    parrafo = Paragraph("Reporte Bitacora ",cabecera)
    #parrafo2=Paragraph("HOLA",estilo2) Prueba de leyenda
#Lo incluimos en el Platypus story.

    story.append(parrafo)
    #story.append(parrafo2) prueba de leyenda
#Ahora incluimos una imagen.

    fichero_imagen = "logo2.png"
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=100,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un párrafo. Vamos a crear un texto largo para demostrar cómo se genera más de una hoja.


#Damos un estilo BodyText al segundo párrafo, que será el texto a escribir.
    fila1=["Usuario","Hora"]
    tabla1=Table([fila1],colWidths=150)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('Select count(*) from Bitacora order by Usuario')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :
    
        hola=ol[l]
    
        while i < hola:
            cur.execute('Select Usuario from Bitacora order by Usuario')
            rs=cur.fetchall()
            cur.execute('Select Hora from Bitacora order by Usuario')
            rs1=cur.fetchall()
        
        
            fila4=[str(rs[i]),str(rs1[i])]
        
            i=i+1
            tabla = Table([fila4],colWidths=150)
        
            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])
        
            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("Reporte.pdf",pagesize=A4,showBoundary=1)

#Construimos el Platypus story.

    doc.build(story)


def ReporUsuario(self):
    con, cur = conexion()


#Creamos un PageTemplate de ejemplo.

    estiloHoja = getSampleStyleSheet()

#Inicializamos la lista Platypus Story.

    story = []

#Definimos cómo queremos que sea el estilo de la PageTemplate.

    cabecera = estiloHoja['Heading4']

#No se hará un salto de página después de escribir la cabecera (valor 1 en caso contrario).

    cabecera.pageBreakBefore=0

#Se quiere que se empiece en la primera página a escribir. Si es distinto de 0 deja la primera hoja en blanco.

    cabecera.keepWithNext=0

#Color de la cabecera.

    cabecera.backColor=colors.cyan

#Incluimos un Flowable, que en este caso es un párrafo.

    parrafo = Paragraph("Reporte Usuarios ",cabecera)

#Lo incluimos en el Platypus story.

    story.append(parrafo)

#Ahora incluimos una imagen.

    fichero_imagen = "logo2.png"
    imagen_logo = Image(os.path.realpath(fichero_imagen),width=100,height=100)
    story.append(imagen_logo)

    story.append(Spacer(0,20))

#Definimos un párrafo. Vamos a crear un texto largo para demostrar cómo se genera más de una hoja.


#Damos un estilo BodyText al segundo párrafo, que será el texto a escribir.
    fila1=["Usuario","Clave","Tipo","Estado"]
    tabla1=Table([fila1],colWidths=150)
    tabla1.setStyle([('BACKGROUND',(0,0),(-1,-1),colors.gray)])
    tabla1.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
    tabla1.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
    story.append(tabla1)

#story.append(Spacer(0,20))
#Y lo incluimos en el story.

    cur.execute('Select count(*) from Usuarios order by Nombre')
    rs1=cur.fetchall()
    i=0
    l=0
    j=0
    for ol in rs1 :
    
        hola=ol[l]
    
        while i < hola:
            cur.execute('Select Nombre from Usuarios order by Nombre')
            rs=cur.fetchall()
            cur.execute('Select Clave from Usuarios order by Nombre')
            rs1=cur.fetchall()
            cur.execute('Select Tipo from Usuarios order by Nombre')
            rs2=cur.fetchall()
            cur.execute('Select Estado from Usuarios order by Nombre')
            rs3=cur.fetchall()
            
##            if str(rs3[i])==0:
##                sol="desbloqueado"
                
            #else:
             #   sol="Bloqueado"

            fila4=[str(rs[i]),str(rs1[i]),str(rs2[i]),str(rs3[i])]
        
            i=i+1    
            tabla = Table([fila4],colWidths=150)
        
            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #tabla.setStyle([("TEXTCOLOR",(1,-4),(7,-4),colors.red),("TEXTCOLOR",(0,0),(0,3),colors.blue)])
        
            story.append(tabla)

#Dejamos espacio.



#Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

    doc=SimpleDocTemplate("Reporte Usuarios.pdf",pagesize=landscape(letter),showBoundary=1)

#Construimos el Platypus story.

    doc.build(story)
