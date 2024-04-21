import random
import sqlite3 as sql

def generateTEMPERATURE():
    cnx = sql.connect("C:\\Users\\emmal\\Documents\\info\\projet S2\\bdd test.db")
    curseur = cnx.cursor()
    for i in range(1,31,1):
        valueT = random.randint(-5,40)
        valueC = 9
        curseur.execute('insert into TEMPERATURE(idCapteur,date,tempé) values (?,?,?)',(valueC,i,valueT))
    cnx.commit()
    cnx.close()
generateTEMPERATURE()