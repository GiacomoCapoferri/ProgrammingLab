#istanzio la classe
class CSVFile():

    #definisco attributo che contenga il nome
    def __init__(self,name):
        #setto il nome
        self.name = name
    
    #definisco metodo per che torni dati csv come lista di liste
    def get_data(self):
        #inizializzo lista
        list = []
        
        my_file = open(self.name, 'r')
        for line in my_file:
            elements = line.split(',')
            #elimino l'ultimo elemento che mi da \n
            elements[-1] = elements[-1].strip()
            if elements[0] != 'Date':
                #date = elements[0]
                #value = elements[1]
                list.append(elements)
        return list

csvfile=CSVFile('shampoo_sales.csv')
print(csvfile.get_data())