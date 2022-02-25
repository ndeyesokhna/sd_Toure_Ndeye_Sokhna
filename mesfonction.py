import csv
import yaml
import xml
import json
import dicttoxml

#########transformation dic to yaml
def dictoyaml(fichieryaml):
    k = open('fichieryaml.yaml' , 'w')
    dico = yaml.dump(fichieryaml, k)
##########tranformation dic to xml    
def dictoxml(fichierxml):
    h = dictoxml(fichierxml)
    k =open('fichierxml.xml' , 'w')
    k.write(k.decode())
    k.close()
##########transformation dic to json
def dictojson(fichierjson):
    j = open('fichierjson.json','w')
    p = json.dump(fichierjson,j)
#######transformation dic to csv
def dictocsv(fichiercsv):  
    g = open('fichiercsv.csv', 'w') 
    field_names = fichiercsv.keys()
    writer = csv.DictWriter(g ,fieldnames= field_names)
    writer.writeheader()
    writer.writerow(fichiercsv)    
      
    
    


  