#fonction verif
from distutils import extension
from posixpath import basename
from mesfonction import dictoyaml
from mesfonction import dictoxml
from mesfonction import dictojson
from mesfonction import dictocsv
import csv
import yaml
import xml
import json
import dicttoxml
import xmltodict
from  posixpath import basename
from os import chdir

def veriffichier(x):
    x = input('entrez url du fichier:')
    k=basename(x)
    chdir('/home/sokhna/Documents/MesProjet/')
    fichier=k.split('.')
    extension=str(fichier[-1])
    extension = extension.lower()
    dico = ''
    if extension == 'json':
        with open(k ,'r') as f :
            dico =  json.load(f)  
    elif  extension == 'yaml' or extension == 'yml': 
        with open(k, 'r') as file:
            dico = yaml.safe_load(file) 
    elif  extension == 'csv':  
        with open(k,'r') as f :
            reader = csv.DictReader(f, delimiter=';')
            lis = []
            cpt = 0
            for i in reader:
               dico= lis.append(i)    
    elif extension == 'xml': 
        g = open(k, 'r')
        dico = xmltodict.parse(g.read())
        dico = json.loads(json.dumps(dico)) 
        g.close()   
                   
    print(dico)
    
    
    cod=['csv','yaml','yml','json','xml']
    if extension in cod:
        print(f"l extension est {extension}: ok")
        if extension in [cod[1],cod[2]] :
            cod.remove('yaml')
            cod.remove('yml')
        else:     
            cod.remove(extension)
        for i in range(len(cod)) :
            print(f"{i+1}.conver en {cod[i]}") 
    exchoice= input(f"choisir l'extension de transformation:")
    if exchoice == 'yaml' or exchoice == 'yml' :
        dictoyaml(dico)
    elif exchoice == 'xml':
        dictoxml(dico) 
    elif exchoice == 'json':
        dictojson(dico)  
    elif exchoice == 'csv':
        dictocsv(dico)         
  
    
y=''
veriffichier(y)
    
       
        
        
        
        
       # /home/sokhna/Documents/MesProjet/diaby.yml
