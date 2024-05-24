import random
import sqlite3 as sql

def generateTEMPERATURE():
    cnx = sql.connect("bdd test.db")
    curseur = cnx.cursor()
    for i in range(1,32,1):
        for j in range(20):
            Temp = random.randint(-5,40)
            curseur.execute('insert into TEMPERATURE(idCapteur,date,temperature) values (?,?,?)',(j+1,i,Temp))
    cnx.commit()
generateTEMPERATURE()