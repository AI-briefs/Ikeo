import mysql.connector 

class Query():
    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="Ikeo")
        self.cursor = self.mydb.cursor()

    def get_produit_usine(self):
        self.cursor.execute("""SELECT produits.nom_produit, usines.nom_usine FROM produits JOIN usine_produit ON produits.id_produit = usine_produit.id_produit JOIN usines ON usine_produit.id_usine = usines.id_usine""")
        s = self.cursor.fetchall()
        d = {}
        for i in s:
            d[i[0]] = []
        for i in s:
            d[i[0]].append(i[1])
        self.mydb.close()
        return d


