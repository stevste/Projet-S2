import sqlite3 as sql

def getTemperatures(dateDebut : int=1, delta : int=1) -> list :
    connexion = sql.connect("bdd test.db")
    curs = connexion.cursor()
    curs.execute("SELECT * FROM TEMPERATURE WHERE date BETWEEN " + str(dateDebut) + " AND "+ str(dateDebut + delta) + " ORDER BY idCapteur ASC")
    liste = curs.fetchall()
    dicoList = []
    for i in range(20) :
        newDico = {}
        for i in range(delta):
            newDico[liste[i+delta][1]] = liste[i+delta][2]

        dicoList.append(newDico)
    connexion.close()
    return dicoList