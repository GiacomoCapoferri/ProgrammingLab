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

        #inizializzo variabile che mi dice se file è leggibile o meno
        file_leggibile=True

        #inizio il try-except
        try:
            my_file = open(self.name, 'r')
        except:
            print('Errore: non riesco a leggere il file')
            file_leggibile=False

        #se il file è leggibile
        if file_leggibile: 
            for line in my_file:
                elements = line.split(',')
                #elimino l'ultimo elemento che mi da \n
                elements[-1] = elements[-1].strip()
                if elements[0] != 'Date':
                    #date = elements[0]
                    #value = elements[1]
                    list.append(elements)
        return list

class NumericalCSVFile(CSVFile):
    def num_get_data(self):
        try:
            num_list = super().get_data()
            for line in num_list:
                line[1]=float(line[1])
            return num_list
        except Exception as err:
            print ('Ho avuto questo Errore: "{}"'.format(err))
             

#csvfile=NumericalCSVFile('shampoo_sales.csv')
#print(csvfile.num_get_data())