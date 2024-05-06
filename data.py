import sqlite3 as sql

connexion = sql.connect("bdd.db")
curs = connexion.cursor()

def temperatures(dateDebut : int=1, delta : int=1) -> list :
    curs.execute("SELECT * FROM TEMPERATURE WHERE date BETWEEN " + str(dateDebut) + " AND "+ str(dateDebut + delta) + " ORDER BY idCapteur ASC")
    liste = curs.fetchall()
    dicoList = []
    for i in range(20) :
        newDico = {}
        for i in range(delta):
            newDico.update(liste[i+delta][1], liste[i+delta])

        dicoList.append(newDico)
    return dicoList

print(temperatures())

connexion.close()