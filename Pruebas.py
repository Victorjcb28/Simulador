import unittest
import sqlite3 as sq3
from time import time
import datetime
global Lista

def conexion():
    con=sq3.connect('Simulacion.s3db')
    cur = con.cursor()
    return con, cur

def desconectar():
    cur.Close()
    con.Close()
    return
    

class tester (unittest.TestCase):
    def test_1(self):
        con,cur=conexion()
        Usu="Victor"
        En=Usu.upper()
        Cla="1234"
        datos=(En,Cla)
    
        con,cur=conexion()
        
        cur.execute("Select * from Usuarios Where Nombre=? and Clave=? and Tipo='ADMINISTRADOR'",datos)
        rs1=cur.fetchone()
        
        if rs1:
            Lista1=[str(rs1[0]),str(rs1[1]),str(rs1[2])]
        else:
            cur.execute("Select * from Usuarios Where Nombre=? and Clave=? and Tipo='PROFESOR'",datos)
            rs2=cur.fetchone()
            if rs2:
                Lista2=[str(rs2[0]),str(rs2[1]),str(rs2[2])]
        
            
            else:
                cur.execute("Select * from Usuarios Where Nombre=? and Clave=? and Tipo='ESTUDIANTE'",datos)
                rs3=cur.fetchone()
                if rs3:
                    Lista1=[str(rs3[0]),str(rs3[1]),str(rs3[2])]

        

        Lista=["VICTOR","1234","ADMINISTRADOR"]
        
        self.assertEqual(Lista,Lista1)

if __name__ == "__main__":
    unittest.main()
