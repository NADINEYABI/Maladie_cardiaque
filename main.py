
#Importation des modules 
import pandas as pd
import mysql.connector
from mysql.connector import Error

#Chargement des données
cardiaque_data = pd.read_csv('ensemble_de_données_cliniques_de_défaillance_cardiaque.csv')
print(cardiaque_data.columns)

#code pour accepter la casse
colonnes = ['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes','ejection_fraction', 'high_blood_pressure', 'platelets','serum_creatinine', 
            'serum_sodium', 'sex', 'smoking', 'time','DEATH_EVENT']
cardiaque_data.columns = colonnes 

print(cardiaque_data.columns)

# Chargement du dataframe dans MYSQL
try:
    connexion = mysql.connector.connect(host='localhost',
                                       database='db_cardiaque',
                                       user='root',
                                       password='')
    if connexion.is_connected():
        print('Connexion à MySQL réussie')
except Error as e:
    print(f"Erreur lors de la connexion à MySQL: {e}")

try:
    cursor = connexion.cursor()

    for i,row in cardiaque_data.iterrows():
        sql = """INSERT INTO maladie (age,anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,
        serum_sodium,sex,smoking,time,DEATH_EVENT) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        #print(sql)
        cursor.execute(sql, tuple(row))

    connexion.commit()
    connexion.close()
    print("DataFrame chargé dans MySQL avec succès!")
except Exception as e:
    print(f"Erreur lors du chargement du DataFrame dans MySQL: {e}")
