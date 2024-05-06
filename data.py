import sqlite3 as sql

connexion = sql.connect("C:\\Users\\conti\\Desktop\\info\\s2\\projet arrosage\\Projet-S2\\bdd test.db")
curs = connexion.cursor()

def temperatures(dateDebut : int=1, delta : int=1) -> list :
    curs.execute("SELECT * FROM TEMPERATURE WHERE date BETWEEN " + str(dateDebut) + " AND "+ str(dateDebut + delta) + " ORDER BY date ASC")
    liste = curs.fetchall()
    dico = {}
    sousliste = []
    for i in range(delta) :
        for elt in liste :
            if elt[1] == dateDebut + i :
                sousliste.append(elt[2])
        dico[dateDebut + i] = sousliste
        sousliste = []
    return dico

print(temperatures())

connexion.close()